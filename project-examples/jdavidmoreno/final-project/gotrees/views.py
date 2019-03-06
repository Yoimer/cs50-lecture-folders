from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .models import Profiles, Trees, Badges, TreeCodes, Offers
from .helpers import upload_file, get_profile, update_badges
from django.db.models import Q
import time
from time import strftime
from Trees.settings import BASE_DIR
import os
from binascii import a2b_base64
from datetime import datetime

# Create your views here.
def index(request):
    """Index view"""
    last_5 = Trees.objects.order_by('-id')[:5]

    uniques = set()
    feed = []

    for elem in last_5:
        if elem.user not in uniques:
            feed.append(elem)
            uniques.add(elem.user)

    for elem in feed:
        if elem.time.date() == datetime.today().date():
            elem.time = 'Today'
        elem.dedication = (elem.dedication[:150] + '...') if len(elem.dedication) > 150 else elem.dedication

    return render(request, 'gotrees/index.html', {"last": feed})




def register(request):
    """Register view"""
    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        first_name = request.POST["first_name"]


        user = User.objects.create_user(username, email, password, first_name=first_name)
        user.save()
        profile = Profiles.objects.create(user_id=user)
        profile.points = 0
        profile.save()
        badge = Badges.objects.create(user=user)
        badge.save()
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, "gotrees/register.html")

def login_page(request):
    """Login view"""
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('myforest', kwargs={"user_username": user.username}))
        else:
            return render(request, "gotrees/login.html", {"message": "Sorry, your username or password is incorrect"})

    else:
        return render(request, "gotrees/login.html")


def logout_page(request):
    """Logout view"""
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def myforest(request, user_username):
    """Public profile view"""
    update_badges(user_username)
    context = get_profile(user_username)
    return render(request, "gotrees/myforest.html", context)


def edit_profile(request, user_username):
    """Editing profile"""
    # Just granting acces to profile owner
    if request.user.username == user_username:
        if request.method == 'POST':

            try:
                file = request.FILES["profile_image"]
                image = upload_file(file, user_username)
            except KeyError:
                image = True


            name = request.POST["name"]
            last_name = request.POST["last_name"]
            my_phrase = request.POST["my_phrase"]
            country = request.POST["country"]
            region = request.POST["region"]
            my_text = request.POST["my_text"]

            user = User.objects.get(id=request.user.id)
            user.first_name = name
            user.last_name = last_name
            user.save()

            if len(user.profile.all()) == 0:
                profile = Profiles.objects.create(country=country, region=region, my_phrase=my_phrase, my_text=my_text, user_id=user)

                if image == False:
                    profile.save()
                    context = get_profile(user_username)
                    context["message"] = True
                    return render(request, 'gotrees/edit_profile.html', context)
                else:
                    return HttpResponseRedirect(reverse('myforest', kwargs={"user_username": user_username}))
            else:
                Profiles.objects.filter(user_id=user).update(country=country, region=region, my_phrase=my_phrase, my_text=my_text)
                profile = Profiles.objects.get(user_id=user)

                if image == False:
                    context = get_profile(user_username)
                    context["message"] = True
                    return render(request, 'gotrees/edit_profile.html', context)
                else:
                    return HttpResponseRedirect(reverse('myforest', kwargs={"user_username": user_username}))
        else:
            context = get_profile(user_username)
            return render(request, 'gotrees/edit_profile.html', context)
    else:
        return HttpResponseRedirect(reverse('index'))

def new_tree(request, user_username):
    if request.user.username == user_username:
        if request.method == "POST":

            try:
                photo_ascii = request.POST["photo"]
                photo_ascii = photo_ascii.split(',')
                photo_bin = a2b_base64(photo_ascii[1])
                file = strftime("%Y%m%d%H%M%S", time.localtime()) + ".png"
                stamp = 'gotrees/static/gotrees/uploads/' + file

                with open(os.path.join(BASE_DIR, stamp), "wb") as file_obj:
                    file_obj.write(photo_bin)
            except IndexError:
                file = ''


            lat = float(request.POST["lat"])
            lng = float(request.POST["lng"])
            tree_name = request.POST["tree_name"]
            tree_species = request.POST["tree_species"]
            kind = request.POST["kind"]
            tree_dedication = request.POST["tree_dedication"]

            user = User.objects.get(username=user_username)
            profile = Profiles.objects.get(user_id=user)
            tree = Trees.objects.create(image=file, lat=lat, lng=lng, species=tree_species, kind=kind, name=tree_name, dedication=tree_dedication, user=user, profile=profile)
            profile.points += profile.points + 3
            tree.save()
            user.save()

            return HttpResponseRedirect(reverse('myforest', kwargs={"user_username": user_username}))

        else:
            return render(request, 'gotrees/new_tree.html')
    else:
        return HttpResponseRedirect(reverse('index'))

def treecodes(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user = User.objects.get(id=request.user.id)
            number = request.POST["number"]
            c_base = datetime.now()

            # This is for the user
            list_codes = []
            # And this is for the database
            list_objects = []

            for i in range(int(number)):
                code = user.username[:2] + str(c_base.day) + user.username[2:]\
                 + str(c_base.month) + (str(c_base.year))[:2] + str(user.id) + \
                 (str(c_base.year))[2:] + user.first_name + str(c_base.microsecond) + str(i)


                list_objects.append(TreeCodes(code=code, user=user))
                list_codes.append(code)

            TreeCodes.objects.bulk_create(list_objects)

            return render(request, 'gotrees/treecodes.html', {"codes": list_codes})

        else:
            return render(request, 'gotrees/treecodes.html')
    else:
        return HttpResponseRedirect(reverse('index'))

def offer(request, offer_id):
    """Render Offers Page"""
    if request.user.is_authenticated:

        if request.method == 'POST':
            offer = Offers.objects.get(id=offer_id)
            profile = Profiles.objects.get(user_id=request.user)

            if offer in profile.offers.all():
                return render(request, 'gotrees/offer.html', {"offer": offer, "message": "Ey!, You already have this offer. You don't need to have it twice.\
                Remember that you can use your offer as many times you want until the end of the promotion"})
            else:
                if profile.points >= offer.points:
                    offer.user.add(profile)
                    profile.points = profile.points - offer.points
                    offer.save()
                    profile.save()
                    return render(request, 'gotrees/offer.html', {"offer": offer, "message": 'Offer Succesfully Added to your Profile!'})
                else:
                    return render(request, 'gotrees/offer.html', {"offer": offer, "message": "Sorry, You don't have enought points yet"})
        else:
            offer = Offers.objects.get(id=offer_id)
            return render(request, 'gotrees/offer.html', {"offer": offer})
    else:
        return HttpResponseRedirect(reverse('login'))

def myoffers(request):
    """Render all offers for a single user"""
    if request.user.is_authenticated:
        offers = Offers.objects.all()
        profile = Profiles.objects.get(user_id=request.user)

        context = {
        "offers":offers,
        "myoffers": profile.offers.all()
        }
        return render(request, 'gotrees/myoffers.html', context)
    else:
        return HttpResponseRedirect(reverse('login'))

def coupon(request, offer_id):
    """Show an specific coupon"""
    if request.user.is_authenticated:
        profile = Profiles.objects.get(user_id=request.user)
        offer = Offers.objects.get(id=offer_id)

        if offer in profile.offers.all():
            return render(request, 'gotrees/coupon.html', {"offer": offer})
        else:
            offers = Offers.objects.all()
            context = {
            "offers":offers,
            "myoffers": profile.offers.all()
            }
            return render(request, 'gotrees/myoffers.html', context)
    else:
        return HttpResponseRedirect(reverse('index'))

def delete_marker(request):
    """Remove a tree-marker from map"""
    id = request.POST["id"]


    tree_to_remove = Trees.objects.get(id=id)
    tree_to_remove.delete()

    return JsonResponse({"success": True})

def add_old_markers(request):
    """Add all already planted tree-markers to map"""

    user_username = request.POST["user_username"]

    user = User.objects.get(username=user_username)
    trees = Trees.objects.filter(user=user).values()


    feed = list(trees)
    return JsonResponse(feed, safe=False)

def update(request):
    """Show all Trees in map view"""

    ne_lat = request.POST["ne_lat"]
    ne_lng = request.POST["ne_lng"]
    sw_lat = request.POST["sw_lat"]
    sw_lng = request.POST["sw_lng"]

    if sw_lng <= ne_lng:
        feed = Trees.objects.filter(lat__gte = sw_lat, lat__lte = ne_lat, lng__gte = sw_lng, lng__lte = ne_lng)
        list = []
        for elem in feed:

            list.append({"tree_image": elem.image, "lat": elem.lat, "lng": elem.lng, "species": elem.species,"kind": elem.kind, "name": elem.name, "dedication": elem.dedication,
            "time": f"{elem.time.day}/{elem.time.month}/{elem.time.year}", "user": elem.user.username, "first_name": elem.user.first_name,
            "image": elem.profile.image})
    else:
        feed = Trees.objects.filter(Q(lat__gte = sw_lat, lat__lte = ne_lat) | Q(lng__gte = sw_lng, lng__lte = ne_lng))

        list = []
        for elem in feed:
        
            list.append({"tree_image": elem.image, "lat": elem.lat, "lng": elem.lng, "species": elem.species, "kind": elem.kind, "name": elem.name, "dedication": elem.dedication,
            "time": f"{elem.time.day}/{elem.time.month}/{elem.time.year}", "user": elem.user.username, "first_name": elem.user.first_name,
            "image": elem.profile.image})

    return JsonResponse(list, safe=False)

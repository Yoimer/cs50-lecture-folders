from django.contrib.auth.models import User
from .models import Profiles, Trees, Badges, Offers
import os

def upload_file(file, user_username):
    """Upload image to profiles"""
    if file.size < 2500000:
        list = ["jpg", "jpeg", "png"]
        end = (file.name).split(".")[1].lower()

        if end in list:
            user = User.objects.get(username=user_username)
            profile = Profiles.objects.get(user_id=user)
            if profile.image != '':
                os.remove('gotrees/static/gotrees/uploads/' + profile.image)
            name = (file.name).split(".")[0] + "." + end
            with open('gotrees/static/gotrees/uploads/' + name, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            profile.image = name
            profile.save()
            return name
        else:
            return False
    else:
        return False

def get_profile(user_username):
    """Serve context for profile and edit_profile"""
    user = User.objects.get(username=user_username)
    profile = Profiles.objects.get(user_id=user)
    badge = Badges.objects.get(user=user)
    trees = user.trees.count()
    offers = Offers.objects.all()


    context = {
        "user_username": user_username,
        "first_name": user.first_name,
        "last_name":user.last_name,
        "trees": trees,
        "points": profile.points,
        "country": profile.country,
        "region": profile.region,
        "my_phrase": profile.my_phrase,
        "my_text": profile.my_text,
        "image": profile.image,
        "heart": badge.heart,
        "diamont": badge.diamont,
        "flag": badge.flag,
        "basic_cup": badge.basic_cup,
        "golden_cup": badge.golden_cup,
        "star": badge.star,
        "offers":offers
    }

    return context


def update_badges(user_username):
    user = User.objects.get(username=user_username)
    badge = Badges.objects.get(user=user)
    n = user.trees.count()

    if n > 0:
        badge.heart = True
    else:
        badge.heart = False
    if n > 29:
        badge.diamont = True
    else:
        badge.diamont = False
    if n > 59:
        badge.flag = True
    else:
        badge.flag = False
    if n > 99:
        badge.basic_cup = True
    else:
        badge.basic_cup = False
    if n > 149:
        badge.golden_cup = True
    else:
        badge.golden_cup = False
    if n > 199:
        badge.star = True
    else:
        badge.star= False
    badge.save()



if __name__ == "__main__":
    main()

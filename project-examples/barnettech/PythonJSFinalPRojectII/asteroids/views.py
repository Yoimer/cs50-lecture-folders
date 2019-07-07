from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Highscore
from django.db import models
from django.contrib.auth.models import User
from django import forms
from .forms import UserCreateForm
import datetime
import requests

# at the homepage, prompt to either login or register, and
# redirect to the main game page to play when logged in.
def index(request):
    if request.user.username is not None:
      return redirect('play_game')
    return render(request, 'play_game.html', {})

# form to register for the site
def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        # save the registration form.
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('play_game')
    else:
        form = UserCreateForm()
    return render(request, 'signup.html', {'form': form})

# view for the main JS gameplay, the focus of the site.
def play_game(request):
  return render(request, 'JSgame.html')

# after game ends post highscore to the model Highscore, using an ajax call
# from javascript.
def post_highscore(request):
   # save the scores to the database.
   score = request.POST.get('score', 0)
   H = Highscore(besttime=int(score), username=request.user.username)
   H.save()
   return HttpResponse("Success!") # Sending an success response

# page to view the top ten high scores.
def view_highscores(request):
    #will fetch all scores, and will order them in desc order and return the top 10 scores
    highscores=Highscore.objects.all().order_by('-besttime')[:10]
    return render(request, 'highscores.html', {'highscores':highscores})

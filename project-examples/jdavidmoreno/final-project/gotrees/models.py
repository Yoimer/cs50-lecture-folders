from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profiles(models.Model):
    image = models.CharField(max_length=100,blank=True)
    country = models.CharField(max_length=30, blank=True)
    region = models.CharField(max_length=30, blank=True)
    my_phrase = models.CharField(max_length=100, blank=True)
    my_text = models.CharField(max_length=400, blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="profile")
    points = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.user_id.username} - {self.user_id.first_name} - {self.points} - {self.country} - {self.region} - {self.my_phrase} - {self.my_text}"

class Trees(models.Model):
    image = models.CharField(max_length=100, null=True)
    lat = models.DecimalField(max_digits=8 ,decimal_places=5, null=True)
    lng = models.DecimalField(max_digits=8 ,decimal_places=5, null=True)
    species = models.CharField(max_length=30)
    kind = models.CharField(max_length=3, null=True)
    name = models.CharField(max_length=30)
    dedication = models.CharField(max_length=400)
    time = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="trees")
    profile = models.ForeignKey(Profiles, on_delete=models.CASCADE, related_name="trees", null=True)

    def __str__(self):
        return f"Coord[lat:{self.lat}, lng:{self.lng}] - {self.species} - {self.kind} - {self.name} - {self.dedication} - {self.time} - {self.user}"

class Badges(models.Model):
    heart = models.BooleanField( default=False)
    diamont = models.BooleanField( default=False)
    flag = models.BooleanField( default=False)
    basic_cup = models.BooleanField( default=False)
    golden_cup = models.BooleanField( default=False)
    star = models.BooleanField( default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="badges", null=True)

    def __str__(self):
        return f"{self.heart} - {self.diamont} - {self.flag} - {self.basic_cup} - {self.golden_cup} - {self.star}"

class TreeCodes(models.Model):
    code = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='codes')

    def __str__(self):
        return f"{self.code} - {self.time} - {self.user}"

class Offers(models.Model):
    points = models.IntegerField()
    image = models.CharField(max_length=100)
    offer_name = models.CharField(max_length=100)
    description = models.CharField(max_length=300, null=True)
    coupon = models.CharField(max_length=100, null=True)
    company = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now=True)
    user = models.ManyToManyField(Profiles, related_name='offers', blank=True)

    def __str__(self):
        return f"{self.company} - {self.offer_name} - {self.points} - {self.time}"

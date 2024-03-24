from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.gis.db import models as gismodels
from django.contrib.gis.geos import Point
from datetime import *
from django.contrib.auth.models import User



class jobType(models.TextChoices):
    Permanent = 'Permanent'
    Temporary = 'Temporary'
    Intership = 'Intership'

class Education(models.TextChoices):
    Bachelors = 'Bachelors'
    Masters = 'Masters'
    Phd = 'Phd'

class Industry(models.TextChoices):
    Bussiness = 'Bussiness'
    IT = 'IT'
    Banking = 'Banking'
    Education = 'Education'
    Telecommunication = 'Telecommunication'
    Others = 'Others'

class Experience(models.TextChoices):
    No_experience = 'No_experience'
    One_year = '1 year'
    Two_year = '2 years'
    Three_year_plus = '3 years above'

def return_Date_time():
    now = datetime.now()
    return now + timedelta(days=10)

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    email = models.EmailField(null=True)
    address = models.CharField(max_length=100, null=True)
    jobType = models.CharField(
        max_length = 10,
        choices = jobType.choices,
        default = jobType.Permanent 
    )
    Education = models.CharField(
        max_length = 10,
        choices = Education.choices,
        default = Education.Bachelors
    )
    Industry = models.CharField(
        max_length = 30,
        choices = Industry.choices,
        default = Industry.Bussiness 
    )   
    Experience = models.CharField(
        max_length = 20,
        choices = Experience.choices,
        default = Experience.No_experience 
    )
    salary = models.IntegerField(default=1, validators=[MinValueValidator(1)
                                 ,MaxValueValidator(1000000)])
    positions = models.IntegerField(default=1)
    company = models.CharField(max_length=100, null=True)
    point = gismodels.PointField(default=Point(0.0,0.0))
    lastDate = models.DateTimeField(default=return_Date_time)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)

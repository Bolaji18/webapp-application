import random
from django.db import models
from django.utils import timezone
# Create your models here.
# integrate services into laporad, change name from laporad to trustalliance.pro
# CAC registration, Insurance registration, Logistics and transportation, legal and financial services, construction and autocad designs.
class student(models.Model):
     name = models.CharField(max_length=800, null=True, verbose_name="Name")
     email = models.CharField(max_length=50, verbose_name="Email")
     phone = models.CharField(max_length=50, verbose_name="Phone No")
     virtual =  models.BooleanField(default=False, null=True, verbose_name="Virtual")


class teacher(models.Model):
     image = models.ImageField(upload_to='images/', null=True)
     course = models.CharField(max_length=800, null=True, verbose_name="Course")
     username = models.CharField(max_length=80, null=True)
     firstname = models.CharField(max_length=80, verbose_name="FirstName")
     lastname = models.CharField(max_length=80, verbose_name="LastName")
     virtual = models.BooleanField(default=False, null=True)
     email = models.CharField(max_length=50, verbose_name="Email")
     experience = models.CharField(max_length=800, null=True, verbose_name="Years of Experience")
     duration = models.CharField(max_length=80, null=True, verbose_name="Duration")
     price = models.CharField(max_length=20, null=True, verbose_name="Price")


class teacherapplication(models.Model):
     course = models.CharField(max_length=800, null=True, verbose_name="Course")
     username = models.CharField(max_length=80, null=True)
     firstname = models.CharField(max_length=80, verbose_name="FirstName")
     lastname = models.CharField(max_length=80, verbose_name="LastName")
     virtual = models.CharField(max_length=80, null=True, verbose_name="Virtual or physical class")
     email = models.CharField(max_length=50, verbose_name="Email")
     phone = models.CharField(max_length=50, null=True, verbose_name="Phone No")
     experience = models.CharField(max_length=800, null=True, verbose_name="Years of Experience")
     duration = models.CharField(max_length=80, null=True, verbose_name="Duration")
     price = models.CharField(max_length=20, null=True, verbose_name="Price")


class apply(models.Model):
    passport = models.ImageField(upload_to='images/', null=True, verbose_name="Upload Passport Photograph ")
    firstname = models.CharField(max_length=800, verbose_name="FirstName")
    lastname = models.CharField(max_length=8000, verbose_name="LastName")
    email = models.CharField(max_length=50, verbose_name="Email")
    phone = models.IntegerField(verbose_name="PhoneNo")
    speciality = models.CharField(max_length=800, verbose_name="Area of Specialization")
    description = models.TextField(verbose_name="Describe your Work")
    job = models.CharField(max_length=800, verbose_name=" Profession")
    price = models.IntegerField(verbose_name="Price")
    state = models.CharField(max_length=800, verbose_name="State")
    address = models.CharField(max_length=800, verbose_name="Address")
    files = models.FileField(upload_to='images/', null=True, verbose_name="Upload CV ")

class Workercontact(models.Model):
     randoms = models.IntegerField(null=True)
     username = models.CharField(max_length=80, null=True)
     name =  models.CharField(max_length=800, null=True, verbose_name="Fullname")
     email =  models.CharField(max_length=50, verbose_name="Email for Contact", null=True)
     phone= models.IntegerField( null=True, verbose_name="PhoneNo")
     location =  models.CharField(max_length=800, null=True, verbose_name="Address")
     description = models.TextField(verbose_name="Request")
     date = models.DateField()


class Workers(models.Model):
     username = models.CharField(max_length=80, null=True)
     firstname = models.CharField(max_length=800, verbose_name="FirstName")
     lastname = models.CharField(max_length=8000, verbose_name="LastName")
     email = models.CharField(max_length=50, verbose_name="Email")
     phone = models.IntegerField(verbose_name="PhoneNo")
     file = models.FileField(upload_to='static/', null=True, verbose_name="Upload CV ")
     speciality = models.CharField(max_length=800, verbose_name="Area of Specialty")
     description = models.TextField(verbose_name="Describe your Work")
     job = models.CharField(max_length=800, verbose_name="Current Profession")
     price = models.IntegerField(verbose_name="Price per Job")
     state = models.CharField(max_length=800, verbose_name="State")
     address = models.CharField(max_length=800, verbose_name="Address")

class Worker(models.Model):
     randoms = models.IntegerField(null=True)
     username = models.CharField(max_length=80, null=True)
     firstname = models.CharField(max_length=800, verbose_name="FirstName")
     lastname = models.CharField(max_length=8000, verbose_name="LastName")
     email = models.CharField(max_length=50, verbose_name="Email")
     phone = models.IntegerField(verbose_name="PhoneNo")
     passport = models.ImageField(upload_to='images/', null=True, verbose_name="Upload Passport Photograph ")
     speciality = models.CharField(max_length=800, verbose_name="Area of Specialty")
     description = models.TextField(verbose_name="Describe your Work")
     job = models.CharField(max_length=800, verbose_name="Current Profession")
     price = models.IntegerField(verbose_name="Price per Job")
     state = models.CharField(max_length=800, verbose_name="State")
     address = models.CharField(max_length=800, verbose_name="Address")
     verified = models.BooleanField(default=False, null=True)



class verifiedworker(models.Model):
     username = models.CharField(max_length=80, null=True)
     firstname = models.CharField(max_length=800, verbose_name="FirstName")
     lastname = models.CharField(max_length=8000, verbose_name="LastName")
     email = models.CharField(max_length=50, verbose_name="Email")
     phone = models.IntegerField(verbose_name="PhoneNo")
     passport = models.ImageField(upload_to='images/', null=True, verbose_name="Upload Passport Photograph ")
     speciality = models.CharField(max_length=800, verbose_name="Area of Specialty")
     description = models.TextField(verbose_name="Describe your Work")
     job = models.CharField(max_length=800, verbose_name="Current Profession")
     price = models.IntegerField(verbose_name="Price per Job")
     state = models.CharField(max_length=800, verbose_name="State")
     address = models.CharField(max_length=800, verbose_name="Address")

class services(models.Model):
    randoms = models.IntegerField(null=True)
    company = models.CharField(max_length=80, null=True, verbose_name="Name")
    username = models.CharField(max_length=80, null=True)
    title = models.CharField(max_length=800, verbose_name="Description of job")
    price = models.CharField(max_length=80, verbose_name="Price")
    responsible =  models.TextField(max_length=8000, verbose_name="Responsibilities", null=True)
    requirement= models.TextField(max_length=8000, verbose_name="Requirements")
    contact = models.CharField(max_length=80, verbose_name="Phone no +234")
    email = models.CharField(max_length=50, verbose_name="Email")
    address = models.CharField(max_length=800, verbose_name="Address")
    state = models.CharField(max_length=80, verbose_name="State")
    local_govt = models.CharField(max_length =80, verbose_name="Local Govt", null=True)


class Infos(models.Model):
    title = models.CharField(max_length=800)
    price = models.IntegerField()
    content = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    contact = models.CharField(max_length=500)
    joined_date = models.DateField(null=True)

class blog(models.Model):
    username = models.CharField(max_length=900,  verbose_name="Username")
    email =  models.CharField(max_length=50, verbose_name="Email")
    title = models.CharField(max_length=900,  verbose_name="Title of blog")
    content = models.TextField(max_length=8000, verbose_name="Write your content")
    image1 = models.ImageField(upload_to='images/', null=True, verbose_name="Document Image")
    image2 = models.ImageField(upload_to='images/', null=True, verbose_name="Document Image")

class Users(models.Model):
    duration = models.CharField(max_length=50)
    price = models.IntegerField()
    content = models.TextField(max_length=500)
    address = models.CharField(max_length=500)
    contact = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/')
    image3 = models.ImageField(upload_to='images/')

class Userinfos(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    homeaddress = models.CharField(max_length=200)
    phone_no = models.CharField(max_length=50)
    dob = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

class apartment(models.Model):
    duration = models.CharField(max_length=50, verbose_name="Length of stay")
    price = models.IntegerField(verbose_name="Price for room" )
    content = models.TextField(max_length=500, verbose_name="Description of room")
    address = models.CharField(max_length=500, verbose_name="Location")
    contact = models.CharField(max_length=100, verbose_name="Contact Information")
    image1 = models.ImageField(upload_to='images/', verbose_name="Image of Room")
    image2 = models.ImageField(upload_to='images/', verbose_name="Image of Room")
    image3 = models.ImageField(upload_to='images/', verbose_name="Image of Room")


class rent(models.Model):
    apartment_name= models.CharField(max_length=100)
    price_daily = models.IntegerField()
    price_weekly = models.IntegerField()
    price_monthly = models.IntegerField()
    location = models.CharField(max_length=200)
    state = models.CharField(max_length=50)
    date = models.DateField()
    image1 = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/')
    image3 = models.ImageField(upload_to='images/')
    image4 = models.ImageField(upload_to='images/')
    image5 = models.ImageField(upload_to='images/')


class auction(models.Model):
    item_description= models.CharField(max_length=100, null=True)
    item_price = models.IntegerField(null=True)
    item_bid = models.IntegerField(null=True)
    image1 = models.ImageField(upload_to='images/', null=True)
    image2 = models.ImageField(upload_to='images/', null=True)
    image3 = models.ImageField(upload_to='images/', null=True)
    image4 = models.ImageField(upload_to='images/', null=True)
    image5 = models.ImageField(upload_to='images/', null=True)

class auctioned_item(models.Model):
    item_description= models.CharField(max_length=100, verbose_name="Description of Item")
    item_price = models.IntegerField(verbose_name="Price of Item")
    item_bid = models.IntegerField(verbose_name="Your starting bid price")
    email = models.CharField(max_length=100, verbose_name="Email")
    image1 = models.ImageField(upload_to='images/', verbose_name="Image of Item")
    image2 = models.ImageField(upload_to='images/', verbose_name="Image of Item")
    image3 = models.ImageField(upload_to='images/', verbose_name="Image of Item")
    image4 = models.ImageField(upload_to='images/', verbose_name="Image of Item")
    image5 = models.ImageField(upload_to='images/', verbose_name="Image of Item")


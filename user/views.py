from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.core.mail import send_mail

from .models import Infos
from .models import Users
from .models import Userinfos
from .models import apartment
from .models import auctioned_item
from .models import services
from .models import blog
from .models import Worker
from .models import Workers
from .models import verifiedworker
from .models import Workercontact
from .models import apply
from .models import teacherapplication
from .models import teacher
from .models import student


from .forms import theservice
from .forms import apartmented
from .forms import NewUserForm
from .forms import ads
from .forms import rent
from .forms import auction
from .forms import blogs
from .forms import workers_form
from .forms import WorkercontactForm
from .forms import verified_form
from .forms import application
from .forms import Workers_apply
from .forms import student_form
from .forms import teacher_form
from .forms import teacherapplication_form
import uuid
import random
from datetime import datetime

from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
# Create your views here.
# integrate services into laporad, change name from laporad to trustalliance.pro
# CAC registration, Insurance registration, Logistics and transportation, legal and financial services, construction and autocad designs.


@login_required
def teacher_application(request):
      if request.method == "POST":
          course = request.POST.get("course")
          username = request.POST.get("username")
          firstname = request.POST.get("firstname")
          lastname = request.POST.get("lastname")
          mail = request.POST.get("email")
          phone = request.POST.get("phone")
          virtual   = request.POST.get("virtual")
          experience = request.POST.get("experience")
          duration = request.POST.get("duration")
          price = request.POST.get("price")
          worker= teacherapplication(course=course, username=username, firstname=firstname, lastname=lastname, email=mail,phone=phone, virtual=virtual, experience=experience, duration=duration,  price=price)
          worker.save()
          email = "trustallianceng@gmail.com"
          subject = 'Trustallianceng'
          message = 'Someone just applied to become a tutor.'
          from_email = 'trustallianceng@gmail.com'
          recipient_list = [email]
          recipient_name = "someone just applied to be a teacher check it out. "  # Replace with the actual recipient name
          html_message = render(request, 'laporad-email.html', {"welcome":recipient_name}).content.decode('utf-8')
          send_mail(subject, message, from_email, recipient_list, html_message=html_message)
          firm= "you have successfully sent your tutor's profile, you will recieve a response from us considering your request"
          return render(request=request, template_name="laporad-login.html", context={"register_form":firm})


      welcome= f"Apply to become a tutor on TrustallianceNG."
      form = teacherapplication_form
      life="Enter"
      return render(request=request, template_name="laporad-login.html", context={"life":life, "register_form":form,"welcome":welcome})





@login_required
def application(request, id,email, username):
      if request.method == "POST":

          username = username
          firstname = request.POST.get("firstname")
          lastname = request.POST.get("lastname")
          mail = request.POST.get("email")
          phone = request.POST.get("phone")
          file  = request.FILES.get("file")
          speciality = request.POST.get("speciality")
          description = request.POST.get("description")
          job = request.POST.get("job")
          price = request.POST.get("price")
          state = request.POST.get("state")
          address = request.POST.get("address")
          my_worker= Workers( username=username, firstname=firstname, lastname=lastname, email=mail, phone=phone, file=file, speciality=speciality, description=description, job=job, price=price, state=state, address=address)
          my_worker.save()
          person = request.user
          email = email
          subject = 'Trustallianceng'
          message = 'You have a new message.'
          from_email = 'trustallianceng@gmail.com'
          recipient_list = [email]
          recipient_name = f"{person} just sent you a message. "  # Replace with the actual recipient name
          html_message = render(request, 'laporad-email.html', {"welcome":recipient_name}).content.decode('utf-8')
          send_mail(subject, message, from_email, recipient_list, html_message=html_message)
          firm= f"{person} have successfully sent your workers profile, you will recieve a response"
          return render(request=request, template_name="laporad-login.html", context={"register_form":firm})


      welcome= f"you can apply ."
      form = Workers_apply
      life="Enter"
      return render(request=request, template_name="laporad-login.html", context={"life":life, "register_form":form,"welcome":welcome})


def certified(request):
    return render(request=request, template_name="laporad-requirements.html", context={})

@login_required
def userpage(request):
     username = request.user
     service_jobs= Workercontact.objects.all().values()
     work = Workers.objects.all().values()
     return render(request=request, template_name="laporad-userpage.html", context={"job":service_jobs, "work":work})


def contact(request, username, email):
    worker_instance = username
    if request.method == "POST":
           description = request.POST.get("description")
           username = worker_instance
           randoms = random.randint(6288, 7289200298298)
           date = datetime.now()
           mail =  request.POST.get("email")
           my_worker= Workercontact(description=description, username=username, randoms=randoms, date=date, email=mail)
           my_worker.save()
           email=email
           person ="A user"
           subject = 'Trustallianceng'
           message = f'You have a new message. i need {description} please contact me on {mail}'
           from_email = 'trustallianceng@gmail.com'
           recipient_list = [email]
           recipient_name = f"{person} just sent you a message. "  # Replace with the actual recipient name
           html_message = render(request, 'laporad-email.html', {"welcome":recipient_name}).content.decode('utf-8')
           send_mail(subject, message, from_email, recipient_list, html_message=html_message)
           firm= f"{person} have successfully sent your workers request"
           return render(request=request, template_name="laporad-login.html", context={"register_form":firm})


@login_required
def jobsdelete(request, randoms):

     item= services.objects.get(randdoms=randoms)
     item.delete()
     register_form = "you have successfully deleted"
     return render(request=request, template_name="laporad-login.html", context={"register_form":register_form})


@login_required
def delete(request, randoms):

     item= Worker.objects.get(randdoms=randoms)
     item.delete()
     register_form = "you have successfully deleted"
     return render(request=request, template_name="laporad-login.html", context={"register_form":register_form})




def detail_view(request,id):


     forms = WorkercontactForm()

     service_jobs= Worker.objects.get(id=id)
     return render(request=request, template_name="laporad-contact.html", context={"job":service_jobs, "x":service_jobs, 'forms':forms})

def search_workers(request):
      if request.method == "POST":
        speciality = request.POST.get("q")
        state = request.POST.get("q")
        serviced_jobs= Worker.objects.filter(speciality__icontains=speciality).values()
        statement = Worker.objects.filter(state__icontains=speciality).values()
        return render(request=request, template_name="workerinfocontact.html", context={"job":serviced_jobs, "states":statement})


def worker(request):
     if request.method == "POST":
        selected= request.POST.get("query")
        values = Worker.objects.filter(description__icontains=selected).values()
        return render(request=request, template_name="workerinfocontact.html", context={"states":values})

     verified = verifiedworker.objects.all().values()
     service_jobs= Worker.objects.all().values()
     return render(request=request, template_name="workerinfo.html", context={"job":service_jobs, "verified":verified})


def jobs(request):
    if request.method == "POST":
        title = request.POST.get("q")
        state =  request.POST.get("q")
        local = request.POST.get("q")
        serviced_jobs= services.objects.filter(title__icontains=title).values()
        statement = services.objects.filter(state__icontains=state).values()
        locality =  services.objects.filter(local_govt__icontains=local).values()
        return render(request=request, template_name="laporad-workercontact.html", context={"jobs":serviced_jobs, "state":statement, "local":locality})
    service_jobs= services.objects.all().values()
    return render(request=request, template_name="laporad-workers.html", context={"jobs":service_jobs})



@login_required
def work(request):
      if request.method == "POST":

          randoms = random.randint(6288, 7289200298298)
          username = request.user
          firstname = request.POST.get("firstname")
          lastname = request.POST.get("lastname")
          email = request.POST.get("email")
          phone = request.POST.get("phone")
          passport  = request.POST.get("passport")
          speciality = request.POST.get("speciality")
          description = request.POST.get("description")
          job = request.POST.get("job")
          price = request.POST.get("price")
          state = request.POST.get("state")
          address = request.POST.get("address")
          my_worker= Worker( verified=False, randoms=randoms, username=username, firstname=firstname, lastname=lastname, email=email, phone=phone, passport=passport, speciality=speciality, description=description, job=job, price=price, state=state, address=address)
          my_worker.save()
          person = request.user
          firm= f"{person} have successfully saved your workers profile"
          return render(request=request, template_name="laporad-login.html", context={"register_form":firm})


      welcome= "This page will create your worker's profile"
      form = workers_form()
      life="Enter"
      return render(request=request, template_name="laporad-login.html", context={"life":life, "register_form":form,"welcome":welcome})

def workverified(request):
     if request.method == "POST":
            randoms = random.randint(6288, 7289200298298)
            username = request.user
            firstname = request.POST.get("firstname")
            lastname = request.POST.get("lastname")
            email = request.POST.get("email")
            phone = request.POST.get("phone")
            passport  = request.POST.get("passport")
            speciality = request.POST.get("speciality")
            description = request.POST.get("description")
            job = request.POST.get("job")
            price = request.POST.get("price")
            state = request.POST.get("state")
            address = request.POST.get("address")
            my_worker= Worker( verified=True, randoms=randoms, username=username, firstname=firstname, lastname=lastname, email=email, phone=phone, passport=passport, speciality=speciality, description=description, job=job, price=price, state=state, address=address)
            my_worker.save()
            person = request.user
            firm= f"{person} have successfully saved your verified workers profile. Thank you for joining us"
            return render(request=request, template_name="laporad-login.html", context={"register_form":firm})
     if request.user.username == "bolajiolu":
       username = request.user
       welcome= f"you are logged in as {username}."
       form = workers_form()
       life="Enter"
       return render(request=request, template_name="laporad-login.html", context={"life":life, "register_form":form,"welcome":welcome})

     else:
        welcome= f"you are not autorised to view this page"
        return render(request=request, template_name="laporad-login.html", context={"welcome":welcome})



@login_required
def logout(request):
     life="You have successfully Logout"
     create = "login/"
     used = "Go back to Login"
     return render(request=request, template_name="laporad-login.html", context={"register_form":life, "create":create, "used":used})

@login_required
def content(request):
      if request.method == "POST":
         username = request.user
         title = request.POST.get('title')
         content = request.POST.get('content')
         email = request.POST.get('email')
         image1 = request.FILES.get('image1')
         image2 = request.FILES.get('image2')
         my_model = blog(username=username, title=title, content=content, email=email, image1=image1, image2=image2)
         my_model.save()
         return HttpResponseRedirect('/')


      username = request.user
      welcome= f"you are logged in as {username}."
      form = blogs()
      life="Enter"
      return render(request=request, template_name="laporad-login.html", context={"life":life, "register_form":form,"welcome":welcome})


@login_required
def servicepage(request):
     if request.method == "POST":
        randoms = random.randint(6288, 7289200298298)
        username = request.user
        company = request.POST.get('company')
        responsible = request.POST.get('responsible')
        title = request.POST.get('title')
        price = request.POST.get('price')
        requirement = request.POST.get('requirement')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        address = request.POST.get('address')
        state = request.POST.get('state')
        local_govt = request.POST.get('local_govt')
        my_model = services( company=company,responsible=responsible, randoms=randoms, username=username,price=price, title=title, requirement=requirement,email=email, contact=contact, address=address, state=state, local_govt=local_govt)
        my_model.save()
        firm= "you have successfully created a job, you will be contacted once we get a suitable worker for your job"
        return render(request=request, template_name="laporad-login.html", context={"register_form":firm})



     welcome= "This page will create your Job posting"
     form = theservice()
     life=  "Enter"
     return render(request=request, template_name="laporad-login.html", context={"life":life, "register_form":form, "welcome":welcome})



@login_required
def auction_page(request):
     if request.method == "POST":
        item_bid = request.POST.get('item_bid')
        item_price = request.POST.get('item_price')
        item_description = request.POST.get('item_description')
        email = request.POST.get('email')
        image1 = request.FILES.get('image1')
        image2 = request.FILES.get('image2')
        image3 = request.FILES.get('image3')
        image4 = request.FILES.get('image4')
        image5 = request.FILES.get('image5')

        my_model = auctioned_item(item_price=item_price,  item_description=item_description, item_bid=item_bid, email=email, image1=image1, image2=image2, image3=image3, image4=image4, image5=image5)
        my_model.save()
        return HttpResponseRedirect('/')

     username = request.user
     form = auction()
     life=  "Enter"
     return render(request=request, template_name="laporad-login.html", context={"life":life, "register_form":form, "welcome":username})

@login_required
def house_rent(request):
     if request.method == "POST":
       price = request.POST.get('price')
       duration = request.POST.get('duration')
       content =  request.POST.get('content')
       address =  request.POST.get('address')
       contact =  request.POST.get('contact')
       image1 = request.FILES.get('image1')
       image2 = request.FILES.get('image2')
       image3 = request.FILES.get('image3')
       my_model = apartment(price=price, duration=duration, content=content, address=address, contact=contact, image1=image1, image2=image2, image3=image3)
       my_model.save()
       return HttpResponseRedirect('/')

     life=  "Save"
     form= apartmented()
     return render(request=request, template_name="laporad-login.html", context={"register_form":form, "life":life,})

def rent_login(request):
    return HttpResponseRedirect('/login')

def nonusers(request):
    User = Users.objects.all().values()
    User = Users.objects.all()
    link = "login/"
    login = "login here"
    return render(request, 'index1.html', {'Users': User, 'link':link,'login':login })


def laropad(request):
    service_jobs= Worker.objects.all().values()
    return render(request, 'laporad-index.html', {"User":"Logout", "job":service_jobs})

def laropad_login(request):
  return render(request, 'laporad-about.html', {})


def about(request):

    return render(request, 'about.html', {})

def log(request):
    style = "we offer logistics and planning offers for easy and secure trading"

@login_required
def desired_page_view(request):
    # Your view logic here

     form = ads()
     return render(request=request, template_name="laporad-login.html", context={"register_form":form,})


def new(request):
   if request.method == "POST":
       form = NewUserForm(request.POST)
       if form.is_valid():
           name= request.POST.get('username')
           email = request.POST.get('email')
           user = form.save()
           description = f"Welcome {name} to TrustallianceNg, Nigeria's freelancer site. You can add your worker profile, advertise your profession and gain work. you can also choose to learn a new skills here"
           username = name
           randoms = random.randint(6288, 7289200298298)
           date = datetime.now()
           my_worker= Workercontact(description=description, username=username, randoms=randoms, date=date, email=email)
           my_worker.save()
           subject = 'Trustallianceng New Request'
           message = 'You have a new message.'
           from_email = 'trustallianceng@gmail.com'
           recipient_list = [email]
           recipient_name = name  # Replace with the actual recipient name
           html_message = render(request, 'laporad-email.html', {"welcome":recipient_name}).content.decode('utf-8')
           send_mail(subject, message, from_email, recipient_list, html_message=html_message)
           return HttpResponseRedirect('userpage')
       else:
            form = "Your username is currently registered by another user or your password doesn't match, return to registration"
            return render(request=request, template_name="laporad-login.html", context={"register_form":form})



   form= NewUserForm()
   life= "Create"
   return render(request=request, template_name="laporad-forms.html", context={"register_form":form, 'life':life})


def user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                welcome = f"you are now logged in as {username}."
                homeplace = "rent"
                ego = "Create an ad"
                ser = Users.objects.all().values()
                ser = Users.objects.all()
                context = {
                    'Users': ser,
                    'welcome': welcome,
                    'homeplace': homeplace,
                    'ego':ego,

                }
                if request.method == "POST":
                    form = ads(request.POST)
                    if form.is_valid():
                        user = form.save
                        return HttpResponse('saved')
                welcome = f" {username}."
                form = ads()
                return HttpResponseRedirect('/')

                return HttpResponse(template.render(context, request))
            else:
                 form = "Invalid Username or Password"
                 return render(request=request, template_name="laporad-login.html", context={"register_form":form})

        else:
             form = "Invalid Username or Password"
             return render(request=request, template_name="laporad-login.html", context={"register_form":form})
    form = AuthenticationForm()
    create = "newaccount/"
    used = "Create New User"
    life = "Login"
    return render(request, "laporad-forms.html", {"register_form":form,  'create':create, 'used':used, 'life':life})

def advertisement(request, id):
    User = Users.objects.get(id=id)
    return render(request, 'adpage.html', {'Users': User})

def create_ad(request,id):
    if user is not None:
        login(request, user)
        welcome = f"you are now logged in ."
        homeplace = "Rent"
        ego = "Create an ad"
        ser = Users.objects.all().values()
        ser = Users.objects.all()
        template = loader.get_template('index1.html')
        context = {
            'Users': ser,
            'welcome': welcome,
            'homeplace': homeplace,
            'ego': ego,

        }

def employee(request):
    if request.method == "POST":
       form = AuthenticationForm(request, data=request.POST)
       if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
    form = AuthenticationForm()
    used = "login as an employee, use the password and username created by your employer to login to this page"
    life = "login"
    return render(request, "laporad-about.html", {"register_form":form, 'used':used, 'life':life})
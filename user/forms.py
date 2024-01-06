from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Users
from .models import rent
from .models import auction
from .models import auctioned_item
from .models import apartment
from .models import services
from .models import blog
from .models import Worker
from .models import Workercontact
from .models import apply
from .models import Workers
from .models import teacherapplication
from .models import teacher
from .models import student


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class student_form(forms.ModelForm):
    class Meta:
        model = student
        fields = "__all__"


class teacher_form(forms.ModelForm):
    class Meta:
        model = teacher
        fields = "__all__"

class teacherapplication_form(forms.ModelForm):
    class Meta:
        model = teacherapplication
        fields = "__all__"





class blogs(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = blog
        fields = ("title", "email", "content", "image1", "image2")

class Workers_apply(forms.ModelForm):
    class Meta:
        model = Workers
        fields = "__all__"

class application(forms.ModelForm):
    class Meta:
        model = apply
        fields = "__all__"

class WorkercontactForm(forms.ModelForm):
    class Meta:
        model = Workercontact
        fields = "__all__"
        exclude = ['randoms', 'username', 'date']

class workers_form(forms.ModelForm):

    class Meta:
        model = Worker
        fields ="__all__"
        exclude = ['randoms', 'username','verified']

class verified_form(forms.ModelForm):

    class Meta:
        model = Worker
        fields ="__all__"
        exclude = ['randoms', 'verified']

class ads(forms.ModelForm):

    class Meta:
        model = Users
        fields ="__all__"



class theservice(forms.ModelForm):

    class Meta:
        model = services
        fields = "__all__"
        exclude = ['randoms',  'username']

class rent(forms.ModelForm):

    class Meta:
        model = rent
        fields ="__all__"

def formfield_for_dbfield(db_field, **kwargs):
    if db_field.name == "email":
        return NewUserForm()
        return db_field.formfield(**kwargs)

class auction(forms.ModelForm):

    class Meta:
        model = auctioned_item
        fields ="__all__"


class apartmented(forms.ModelForm):

    class Meta:
        model = apartment
        fields ="__all__"


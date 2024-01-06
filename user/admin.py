from django.contrib import admin
from .models import Users
from .models import services
from .models import Worker
from .models import Workers
from .models import verifiedworker
from .models import Workercontact
from .models import teacherapplication
from .models import teacher
from .models import student

# Register your models here.
admin.site.register(Users)
admin.site.register(services)
admin.site.register (Worker)
admin.site.register (Workers)
admin.site.register (verifiedworker)
admin.site.register (Workercontact)
admin.site.register(teacherapplication)
admin.site.register(teacher)
admin.site.register(student)



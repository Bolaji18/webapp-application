from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns =[
    path('', views.laropad, name='home'),
    path('logged/', views.laropad_login, name='login'),
    path('login/', views.user, name='log'),
    path('login/auction/', views.auction_page, name='auction_page'),
    path('login/newaccount/', views.new, name='newacc'),
    path('login/newaccount/userpage', views.userpage, name='newacc'),
    path('newaccount/', views.new, name='newaccount'),
    path('employee/', views.employee, name='employee'),
    path('ads/<int:id>', views.advertisement, name='advertisement'),
    path('nonuser/', views.nonusers, name="nonuser"),
    path('user/', views.desired_page_view, name="user"),
    path('user/login/', views.user, name='loge'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('services/', views.servicepage, name='service'),
    path('services/login/', views.rent_login, name='serve'),
    path('work/', views.work, name='work'),
    path('jobs/', views.jobs, name='jobs'),
    path('jobs/<int:id>/<str:email>/<str:username>', views.application, name='application'),
    path('jobs/delete/<int:randoms>/', views.jobsdelete, name='delete_jobs'),
    path('workers/', views.worker, name='worker'),
    path('workers/search', views.search_workers, name='search_worker'),
    path('workers/<int:id>', views.detail_view, name='view'),
    path('workers/delete/<int:randoms>/', views.delete, name='delete_item'),
    path('workers/<str:email>/<str:username>', views.contact, name='contactspage'),
    path('contact/<str:username>/<str:email>', views.contact, name='contact'),
    path('userpage', views.userpage, name='userpage'),
    path('verified', views.workverified, name='verified'),
    path('certification', views.certified, name='certified'),
    path('tutorapplication', views.teacher_application, name='tutor'),
]


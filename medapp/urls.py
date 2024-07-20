from django.urls import path,include
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('haqqimizda',about,name='about'),
    path('xidmetler',services,name='services'),
    path('xidmet/<slug>',service,name='service'),
    path('bloqlar',blogs,name='blogs'),
    path('bloq/<slug>',blog,name='blog'),
    path('elaqe',contact,name='contact'),
    path('message',message,name='message'),
    path('dmessage',d_message,name='dmessage'),
    path('comment',comment,name='comment'),
    path('hekimler',team,name='team'),
    path('hekim/<slug>',doctor,name='doctor'),
]
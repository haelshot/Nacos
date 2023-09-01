from .views import *
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('service', service, name='service'),
    path('album/', photo_list, name='album'),
    path('level/<str:level>/', level_materials, name='level_materials'),
    path('send_comment', send_comment, name='send_comment'),
]


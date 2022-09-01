from django.urls import path
from . import views


urlpatterns = [
    #path('activate/<slug:uidb64>/<slug:token>/', activate, name='activate'),
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('services', views.services, name="services"),
    path('main', views.main, name="main"),
    path('contact', views.contact, name="contact"),
    path('birthday', views.birthday, name="birthday"),
    path('event', views.event, name="event"),
    path('wedding', views.wedding, name="wedding"),
    path('fashion', views.fashion, name="fashion"),
    path('beautiful', views.beautiful, name="beautiful"),
    path('testimony', views.testimony, name="testimony"),
    path('subadmin', views.subadmin, name="subadmin")
]

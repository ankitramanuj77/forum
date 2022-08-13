from django.contrib import admin
from django.urls import path
from mysite import views
from django.conf.urls.static import static,serve
from django.conf import settings

urlpatterns = [
    path('',views.index, name='index'),
    path('home/',views.home, name='home'),
    path('userlogout/',views.userlogout, name="userlogout"),
    path('updateprofile/',views.updateprofile, name='updateprofile'),
    path('about/',views.about, name="about"),
    path('contact/',views.contact, name="contact"),
    # path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
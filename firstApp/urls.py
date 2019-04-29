from django.urls import path
from . import views
# '' path represents the root of the app
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('archive/', views.archive, name='archive'),
    path('premium/', views.premium, name='premium'),
    path('contact/', views.contact, name='contact'),
    path('coolWebsites/', views.coolWebsites, name='coolWebsites'),
    path('getpremium/', views.getpremium,  name='getpremium'),
    path('premiumtab/', views.premiumtab, name='premiumtab'),
    path('premiumLogin/', views.premiumLogin, name='premiumLogin')
]

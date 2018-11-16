from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.homepage_view, name='home'),
    path('contact', views.contactpage_view, name='contact'),
    path('about', views.aboutpage_view, name='about'),
    # path('social', views.socialpage_view, name='social'),
]
from django.urls import path
from .views import *


app_name = 'frontend'

urlpatterns = [
    path("", HomeView, name="home"),
    path("about", AboutView, name="about"),
    path("services", ServicesView, name="services"),
    # path("faq", faq_view, name="faq"),
    path("contact", ContactView, name="contact"),
    # path("privacy-policy", privacy_view, name="privacy"),
]
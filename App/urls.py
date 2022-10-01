from django.urls import path
from App import views
urlpatterns = [
    path("",views.index,name="index"),
    path("Analyzer",views.analyzer,name="analyze"),
    path("about/",views.aboutus,name="about"),
    path("contact/",views.contactus,name="contact")

]

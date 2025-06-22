from django.urls import path
from .views import *

urlpatterns = [
    path("",home),
    path("applied_user/", applicants),
    path("get_applicants/", get_applicants),
    path("save_message/", save_message),
]

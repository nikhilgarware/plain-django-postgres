from accounts import api
from django.urls import path

urlpatterns = [
    path("create-account/", api.Accounts.as_view(), name="create-account")
]

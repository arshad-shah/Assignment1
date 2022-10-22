from django.urls import path

from .views import SignUpView, UpdateDetailsView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("update_details/", UpdateDetailsView.as_view(), name="update_details"),
]

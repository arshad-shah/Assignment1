from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


# an update details view that updates the auth_user table's first_name, last_name, email using the username
class UpdateDetailsView(generic.UpdateView):
    model = User
    fields = ["first_name", "last_name", "email"]
    template_name = "registration/update_details.html"
    success_url = reverse_lazy("home")

    def get_object(self):
        return self.request.user
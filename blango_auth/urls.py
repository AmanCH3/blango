import blango_auth.views
from django_registration.backends.activation.views import RegistrationView
from blango_auth.forms import BlangoRegistrationForm


urlpatterns = [
  path('accounts/', include('django_registration.backends.activation.urls')),
  path("accounts/profile/", blango_auth.views.profile, name="profile") ,
  path(
    "accounts/register/",
    RegistrationView.as_view(form_class=BlangoRegistrationForm),
    name="django_registration_register",
)
]
  
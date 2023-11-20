from django.contrib import admin
from django.urls import path, include
from registrationapp import views as rv

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("chat.urls")),
    path('signup/', rv.SignUp, name="register"),
    path("", include("django.contrib.auth.urls")),
]

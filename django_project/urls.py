from django.contrib import admin
from django.urls import path, include
from registrationapp import views as rv

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("chatapp.urls")),
    path('signup/', rv.SignUp, name="register"),
    path("", include("django.contrib.auth.urls")),
]

from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from filmyweb.views import user_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('filmy/', include('filmyweb.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


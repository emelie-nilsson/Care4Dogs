"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from django.shortcuts import render  # For test-404 view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    # path('dogcare/', include('dogcare.urls')),
    # path("accounts/", include("allauth.urls")),

    # Log-out view that shows logout.html instead of returning to homepage
    path("accounts/logout/", LogoutView.as_view(template_name="allauth/account/logout.html"), name="account_logout"),
    path('dogcare/', include('dogcare.urls')),
    path("accounts/", include("allauth.urls")),


    # Test route for 404 page
    path("test-404/", lambda request: render(request, '404.html', status=404)),
]

# Serve static and media files during development only
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=os.path.join(settings.BASE_DIR, 'static'))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
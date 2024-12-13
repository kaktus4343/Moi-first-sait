"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from mainapp.views import mai1,mai2,mai3,contact_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", mai1),
    path('contact', contact_view, name='contact'),
    path("contact", mai2),
    path("works", mai3),
    path('contact/', contact_view, name='contact'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




# urls



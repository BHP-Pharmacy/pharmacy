"""pharmacy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls.conf import path, include
from django.contrib.auth.views import LogoutView
from django.views.generic.base import RedirectView

from pharma_subject.admin_site import pharma_subject_admin
from .views import HomeView, AdministrationView

urlpatterns = [
    path('accounts/', include('edc_base.auth.urls')),
    path('admin/', include('edc_base.auth.urls')),
    
    path('admin/', admin.site.urls),
    path('admin/', pharma_subject_admin.urls),
    
    path('administration/', AdministrationView.as_view(),
         name='administration_url'),
    path('admin/pharma_subject/',
         RedirectView.as_view(url='admin/pharma_subject/'),
         name='pharma_subject_models_url'),
    
    path('edc_base/', include('edc_base.urls')),
    path('edc_device/', include('edc_device.urls')),
    path('edc_label/', include('edc_label.urls')),
    path('pharma_subject/', include('pharma_subject.urls')),
    path('subject/', include('pharma_dashboard.urls')),

    path('switch_sites/', LogoutView.as_view(next_page=settings.INDEX_PAGE),
         name='switch_sites_url'),
    path('home/', HomeView.as_view(), name='home_url'),
    path('', HomeView.as_view(), name='home_url'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from hospital.views import home, HospitalDetailView
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',home, name='homepage'),
    path('hospital/<int:pk>',HospitalDetailView.as_view(), name='hospital_detail')
    ]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

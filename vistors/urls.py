from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'visitors'

urlpatterns = [
    path('event_list/', views.event_list, name='event_list'),
    path('participate/<int:id>/', views.participate, name='participate'),
    path('event_details/<int:id>/', views.event_details, name='event_details')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

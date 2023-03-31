from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'student'

urlpatterns = [
    path('events/', views.event_list, name='events'),
    path('p_events/', views.past_events, name='p_event'),
    path('p_det/<int:id>/', views.past_details, name='p_det'),
    path('participate/<int:id>/', views.participate, name='participate'),
    path('volunteer/<int:id>/', views.volunteer, name='volunteer'),
    path('event_details/<int:id>/', views.event_details, name='event_details'),
    path('manage_profile/', views.manage_profile, name='manage_profile'),
    path('password/', views.change_password, name='change_password'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

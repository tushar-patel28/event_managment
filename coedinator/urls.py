from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'coedinator'

urlpatterns = [
    path('add_event/', views.add_event, name='add_event'),
    path('event_list/', views.event_list, name='event_list'),
    path('edit_event/<int:id>/', views.event_edit, name="event_edit"),
    path('delete_event/<int:id>/', views.event_delete, name='delete_event'),
    path('add_speaker/', views.add_speaker, name='add_speaker'),
    path('event_details/<int:id>/', views.event_details, name='event_details'),
    path('visitors_list/', views.visitors_list, name='visitors_list'),
    path('delete_visitors/<int:id>/', views.visitors_delete, name='delete_visitors'),
    path('edit_visitors/<int:id>/', views.edit_visitors, name='edit_visitors'),

    path('student_list/', views.students_list, name='student_list'),
    path('cordinator_list/', views.cordinator_list, name='cordinator_list'),
    path('edit_student/<int:id>/', views.edit_student, name='edit_student'),
    path('delete_student/<int:id>/', views.student_delete, name='delete_student'),
    path('past_event/', views.post, name='past_event'),
    path('p_events/', views.past_events, name='p_event'),
    path('p_det/<int:id>/', views.past_details, name='p_det'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
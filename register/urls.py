from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'register'

urlpatterns = [
    path('', views.index, name='index'),
    path('s_register/', views.student_register, name='s_register'),
    path('c_register/', views.cordinator_register, name='c_register'),
    path('a_register/', views.admin_register, name='a_register'),
    path('v_register/', views.visitor_register, name='v_register'),
    path('user_login/', views.user_login, name='user_login'),
    path('visitor_login/', views.visitor_login, name='visitor_login'),
    path('student_login/', views.student_login, name='student_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('student_logout/', views.student_logout, name='student_logout')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

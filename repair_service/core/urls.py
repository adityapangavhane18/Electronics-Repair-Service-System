from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('submit-request/', views.submit_request, name='submit_request'),
    path('all-requests/', views.view_requests, name='view_requests'),
    path('update-status/<int:request_id>/', views.update_status, name='update_status'),
    path('chatbot/', views.chatbot_response, name='chatbot_response'),
    path('track-status/', views.track_status, name='track_status'),
    
]


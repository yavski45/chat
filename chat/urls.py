from django.urls import path
from . import views

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('chat/<int:user_id>/', views.chat_room, name='chat_room'),
]

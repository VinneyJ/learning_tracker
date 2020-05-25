#url oatterns for learning logs
from django.urls import path

from . import views

app_name = 'learning_logs'

urlpatterns = [
    #Homepage
    path('', views.index, name = 'index'),
    path('topics/', views.topics, name = 'topics'),
    #Details page
    path('topics/<int:topic_id>/', views.topic, name = 'topic'),
    #To new topic page
    path('new_topic/', views.new_topic, name = 'new_topic'),
    path('new_topic/<int:topic_id>/', views.new_entry, name = 'new_entry'),
    #Edit entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry')
]
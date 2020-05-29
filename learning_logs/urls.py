#url oatterns for learning logs
from django.urls import path

from . import views
from .views import EntryDeleteView

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
    path('edit_topic/<int:topic_id>/', views.edit_topic, name='edit_topic'),
    #Edit entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    #Delete entry
    path('topic/<int:pk>/delete', EntryDeleteView.as_view(), name='delete_entry')
]
"""Defines URL patterns for learning_logs."""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
        # Home Page:
        path('', views.index, name='index'),

        # Page that shows all topics:
        path('topics/', views.topics, name='topics'),

        # Detail for single Topic page:
        # NOTE: <int:topic_id>
        path('topics/<int:topic_id>', views.topic, name='topic'),

        # Page for adding a new topic:
        path('new_topic/', views.new_topic, name='new_topic'),

        # Path for adding a new entry:
        path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),

        # Path for edting an entry:
        path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry'),
]

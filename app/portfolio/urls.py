from django.urls import path
from .views import (HomeView, ProjectView, ContactView, AboutView)
#  ContactView, AboutView,
#                     ProjectView, ProjectsView, WorkHistoryView)
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact', ContactView.as_view(), name='contact'),
    path('about', AboutView.as_view(), name='about'),
    path('project/<str:project_name>', ProjectView.as_view(), name='project'),
    # path('projects', ProjectsView.as_view(), name='projects'),
    # path('work-history', WorkHistoryView.as_view(), name='work-history'),
]

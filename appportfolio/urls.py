#urls.py portfolio
from django.urls import path

from .views import main,  download_resume ,project_details
urlpatterns = [
    path('',main, name="main"),
    path('download-resume/<int:profile_id>/', download_resume, name='download_resume'),
    path('project-details/<int:project_id>/', project_details, name='project_details'),
]

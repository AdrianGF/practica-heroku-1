from django.urls import path
from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from .views import ProjectListView
from .views import ProjectsFavoriteAPIView;

app_name = 'projects'

router = DefaultRouter()
router.register('projects', ProjectListView)

projects_list = ProjectListView.as_view({
    'get': 'list',
    'post': 'create'
})

projects_details = ProjectListView.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    path('projects/', projects_list, name='project_list'),
    path('projects/<slug>', projects_details, name='project_details'),
    path('projects/<slug>/favorite/',ProjectsFavoriteAPIView.as_view()),    
]
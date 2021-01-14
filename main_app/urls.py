from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('developers/', views.developers_index, name='index'),
    path('developers/<int:developer_id>/', views.developers_detail, name='detail'),
    path('developers/create/', views.DeveloperCreate.as_view(), name='developers_create'),
    path('developers/<int:pk>/update/', views.DeveloperUpdate.as_view(), name='developers_update'),
    path('developers/<int:pk>/delete/', views.DeveloperDelete.as_view(), name='developers_delete'),
    path('developers/<int:developer_id>/assoc_project/<int:project_id>/', views.assoc_project, name='assoc_project'),
    path('projects/', views.projects_index, name='projects_index'),
    path('projects/<int:pk>/', views.ProjectDetail.as_view(), name='projects_detail'),
    path('projects/<int:pk>/update/', views.ProjectUpdate.as_view(), name='projects_update'),
    path('projects/<int:pk>/delete/', views.ProjectDelete.as_view(), name='projects_delete'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
]

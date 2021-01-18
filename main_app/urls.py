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
    path('projects/', views.projects_index, name='projects_index'),
    path('projects/<int:pk>/', views.ProjectDetail.as_view(), name='projects_detail'),
    path('projects/create/', views.ProjectCreate.as_view(), name='projects_create'),
    path('projects/<int:pk>/update/', views.ProjectUpdate.as_view(), name='projects_update'),
    path('projects/<int:pk>/delete/', views.ProjectDelete.as_view(), name='projects_delete'),
    path('profile/', views.user_profile, name='user_profile'),
    # goes to projects page
    path('developers/<int:developer_id>/projects/', views.dev_projects, name='dev_projects'),
    # associate project with developer
    path('developers/<int:developer_id>/assoc_project/<int:project_id>/', views.assoc_project, name='assoc_project'),
    #remove a project from developer
    path('developers/<int:developer_id>/unassoc_project/<int:project_id>/', views.unassoc_project, name='unassoc_project'),
    path('profile/update/', views.update_profile, name='update_profile'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
]

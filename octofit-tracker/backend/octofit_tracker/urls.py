"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from .views import UserListView, UserDetailView, TeamListView, TeamDetailView, ActivityListView, ActivityDetailView, LeaderboardListView, LeaderboardDetailView, WorkoutListView, WorkoutDetailView, api_root

urlpatterns = [
    path('', api_root, name='api-root'),
    path('admin/', admin.site.urls),
    path('api/users/', UserListView.as_view(), name='user-list'),
    path('api/users/<str:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('api/teams/', TeamListView.as_view(), name='team-list'),
    path('api/teams/<str:pk>/', TeamDetailView.as_view(), name='team-detail'),
    path('api/activities/', ActivityListView.as_view(), name='activity-list'),
    path('api/activities/<str:pk>/', ActivityDetailView.as_view(), name='activity-detail'),
    path('api/leaderboard/', LeaderboardListView.as_view(), name='leaderboard-list'),
    path('api/leaderboard/<str:pk>/', LeaderboardDetailView.as_view(), name='leaderboard-detail'),
    path('api/workouts/', WorkoutListView.as_view(), name='workout-list'),
    path('api/workouts/<str:pk>/', WorkoutDetailView.as_view(), name='workout-detail'),
]

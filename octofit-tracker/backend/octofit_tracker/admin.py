from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout

# Removed all admin.site.register calls as mongoengine models are not compatible with Django's admin interface.
from mongoengine.errors import DoesNotExist
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, Team, Activity, Leaderboard, Workout

def get_document_or_404(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except DoesNotExist:
        raise status.HTTP_404_NOT_FOUND

class UserListView(APIView):
    def get(self, request):
        users = User.objects.all()
        return Response(users)

    def post(self, request):
        user = User(**request.data)
        user.save()
        return Response(user, status=status.HTTP_201_CREATED)

class UserDetailView(APIView):
    def get(self, request, pk):
        user = get_document_or_404(User, id=pk)
        return Response(user)

    def put(self, request, pk):
        user = get_document_or_404(User, id=pk)
        for key, value in request.data.items():
            setattr(user, key, value)
        user.save()
        return Response(user)

    def delete(self, request, pk):
        user = get_document_or_404(User, id=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ApiRootView(APIView):
    def get(self, request):
        base_url = "https://cautious-doodle-5vv5qv74wpv25rq-8000.app.github.dev/"
        return Response({
            'users': base_url + 'api/users/',
            'teams': base_url + 'api/teams/',
            'activities': base_url + 'api/activities/',
            'leaderboard': base_url + 'api/leaderboard/',
            'workouts': base_url + 'api/workouts/'
        })

# Similar views for Team, Activity, Leaderboard, and Workout can be added here.
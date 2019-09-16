from django.db.models import Model
from rest_framework.serializers import ModelSerializer
from drf_model_pusher.backends import PusherBackend, PrivatePusherBackend
from .serializers import ToDoSerializer

class ToDoPusherBackend(PusherBackend):
    serializer_class = ToDoSerializer

class ToDoPusherPrivateBackend(PrivatePusherBackend):
    serializer_class = ToDoSerializer

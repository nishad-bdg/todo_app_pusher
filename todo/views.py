from rest_framework import viewsets, generics
from drf_model_pusher.views import ModelPusherViewMixin
from .serializers import ToDoSerializer
from .models import ToDo

# Create your views here.


class ToDoList(ModelPusherViewMixin, generics.ListCreateAPIView):
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()

    def get_pusher_channels(self):
        return["channel"]


class ToDoDetail(ModelPusherViewMixin, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()

    def get_pusher_channels(self):
        return["channel"]

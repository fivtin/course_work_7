from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from habit.models import Habit
from habit.paginators import HabitPagination
from habit.serializers import HabitSerializer


# Create your views here.

class HabitListAPIView(ListAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = HabitPagination

    def get_queryset(self):
        queryset = Habit.objects.filter(user=self.request.user)
        return queryset


class PublicHabitListAPIView(ListAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]
    queryset = Habit.objects.filter(is_public=True)

from rest_framework.generics import ListAPIView, CreateAPIView, \
    UpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from habit.models import Habit
from habit.paginators import HabitPagination
from habit.permissions import IsOwner
from habit.serializers import HabitSerializer, HabitCreateSerializer


# Create your views here.

class HabitListAPIView(ListAPIView):
    """View a list of self habits."""

    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = HabitPagination

    def get_queryset(self):
        queryset = Habit.objects.filter(user=self.request.user)
        return queryset


class PublicHabitListAPIView(ListAPIView):
    """View a list of public habits."""

    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]
    queryset = Habit.objects.filter(is_public=True)
    pagination_class = None


class HabitCreateAPIView(CreateAPIView):
    """Create habit."""

    serializer_class = HabitCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        habit = serializer.save(user=self.request.user)
        habit.save()


class HabitUpdateAPIView(UpdateAPIView):
    """Update habit data."""

    serializer_class = HabitCreateSerializer
    permission_classes = [IsOwner]
    queryset = Habit.objects.all()


class HabitRetrieveAPIView(RetrieveAPIView):
    """View habit detail."""

    serializer_class = HabitCreateSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]


class HabitDestroyAPIView(DestroyAPIView):
    """Destroy habit."""

    queryset = Habit.objects.all()
    permission_classes = [IsOwner]

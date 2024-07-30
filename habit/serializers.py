from rest_framework.serializers import ModelSerializer

from habit.models import Habit
from habit.validators import RelatedRewardValidator, \
    TimeDurationValidator, RelatedIsPleasantValidator, \
    PleasantNotRewardAndRelatedValidator, PeriodValidator


class HabitSerializer(ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'


class HabitCreateSerializer(ModelSerializer):
    """Habit create/update/detail serializer."""

    class Meta:
        model = Habit
        exclude = ('user', )
        validators = [
            RelatedRewardValidator('related_to', 'reward'),
            TimeDurationValidator('duration'),
            RelatedIsPleasantValidator('related_to'),
            PleasantNotRewardAndRelatedValidator(
                'is_pleasant',
                'related_to',
                'reward'),
            PeriodValidator('period'),
        ]

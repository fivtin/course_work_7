from rest_framework.exceptions import ValidationError


class RelatedRewardValidator:
    """Checking the incompatibility of "associated habit" and “reward”."""

    def __init__(self, field_1, field_2):
        self.field_1 = field_1
        self.field_2 = field_2

    def __call__(self, value):
        message = \
            "You can’t choose a related habit and a reward at the same time."
        if value.get(self.field_1) and value.get(self.field_2):
            raise ValidationError(message)


class TimeDurationValidator:
    """Checking the execution time of the “action” of a habit."""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if value.get(self.field) is not None:
            if value.get(self.field) < 1 or value.get(self.field) > 120:
                raise ValidationError(
                    "The action should not take more than 120 seconds."
                )


class RelatedIsPleasantValidator:
    """Checking that the established habit is pleasant."""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if value.get(self.field):
            related_habit = value.get(self.field)
            if related_habit and not related_habit.is_pleasant:
                raise ValidationError(
                    "The associated habit can only be pleasant."
                )


class PleasantNotRewardAndRelatedValidator:
    """
    Checking that a pleasant habit
    does not have a reward or habit associated with it.
    """

    def __init__(self, field_1, field_2, field_3):
        self.field_1 = field_1
        self.field_2 = field_2
        self.field_3 = field_3

    def __call__(self, value):
        if (value.get(self.field_1)
                and (value.get(self.field_2) or value.get(self.field_3))):
            raise ValidationError(
                "A pleasant habit cannot have a reward or an associated habit."
            )


class PeriodValidator:
    """Check that the habit interval is in the range from 1 to 7 days."""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        print(value.get(self.field))
        if value.get(self.field) is not None:
            if value.get(self.field) < 1 or value.get(self.field) > 7:
                raise ValidationError(
                    "The frequency of the habit should be from 1 to 7 days."
                )

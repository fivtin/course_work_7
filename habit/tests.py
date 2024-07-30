from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from habit.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    """Test habit API."""

    def setUp(self):
        self.user = User.objects.create(email="test@example.com")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(
            user=self.user,
            action="action",
            when="14:00",
            place="place",
            is_pleasant=False,
            related_to=None,
            reward=None,
            period=5,
            duration=120,
            is_public=True,
        )

    def test_habit_create(self):
        """Testing adding a habit."""

        url = reverse("habit:habit_create")
        data = {
            "action": "action",
            "place": "place",
            "when": "9:25"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)
        self.assertEqual(response.json()['when'], '09:25:00')

    def test_habit_wrong_create(self):
        """Testing adding a habit."""

        url = reverse("habit:habit_create")
        data = {
            "action": "action",
            "place": "place",
            "related_to": 1,
            "reward": "reward"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_habit_update(self):
        """Testing a partial habit update."""

        url = reverse("habit:habit_update", args=(self.habit.pk,))
        data = {
            "reward": "reward",
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("reward"), "reward")

    def test_habit_delete(self):
        """Habit removal testing."""

        url = reverse("habit:habit_delete", args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)

    def test_habit_list(self):
        """Testing getting a list of habits."""

        url = reverse("habit:habit_list")
        response = self.client.get(url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Habit.objects.all().count(), 1)

    def test_habit_is_public_list(self):
        """Testing getting a list of public habits."""

        url = reverse("habit:public_habit_list")
        response = self.client.get(url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Habit.objects.all().count(), 1)

from django.urls import path

from habit.apps import HabitConfig
from habit.views import HabitListAPIView

app_name = HabitConfig.name

urlpatterns = [
    # path('lessons/', LessonListAPIView.as_view(), name='lesson_list'),
    # path('lessons/create', LessonCreateAPIView.as_view(), name='lesson_create'),
    # path('lessons/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_detail'),
    # path('lessons/<int:pk>/update', LessonUpdateAPIView.as_view(), name='lesson_update'),
    # path('lessons/<int:pk>/delete', LessonDestroyAPIView.as_view(), name='lesson_delete'),
    # path('payments/', PaymentListAPIView.as_view(), name='payment_list'),
    # path("subscribe/", CourseSubscriberAPIView.as_view(), name="subscribe"),

    path('', HabitListAPIView.as_view(), name='habit_list'),
    path('public/', PublicHabitListAPIView.as_view(), name='public_habit_list'),
    path('create/', HabitCreateAPIView.as_view(), name='habit_create'),
    path('<int: pk>/update/', HabitUpdateAPIView.as_view(), name='habit_update'),
    path('<int: pk>/delete', HabitDestoyAPIView.as_view(), name='habit_delete'),

] # + router.urls

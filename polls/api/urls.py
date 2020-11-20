from django.urls import path

from .api_views import PollListAPIView, QuestionListAPIView, PollDetailAPIView, QuestionDetailAPIView

urlpatterns = [
    path('polls/', PollListAPIView.as_view(), name='polls_list'),
    path('polls/<str:id>/', PollDetailAPIView.as_view(), name='polls_detail'),
    path('questions/', QuestionListAPIView.as_view(), name='questions_list'),
    path('questions/<str:id>/', QuestionDetailAPIView.as_view(), name='questions_details'),
]

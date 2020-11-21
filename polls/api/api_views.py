from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from .serializers import PollSerializer, QuestionSerializer
from ..models import Poll, Question


class PollListAPIView(ListAPIView):
    serializer_class = PollSerializer
    queryset = Poll.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['expiration_date']


class PollDetailAPIView(RetrieveAPIView):
    serializer_class = PollSerializer
    queryset = Poll.objects.all()
    lookup_field = 'id'


class QuestionPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_pages_size = 10


class QuestionListAPIView(ListAPIView):
    serializer_class = QuestionSerializer
    pagination_class = QuestionPagination
    queryset = Question.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['answer_type']


class QuestionDetailAPIView(RetrieveAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    lookup_field = 'id'

from . import views
from django.urls import path
from .views import Quiz, RandomQuestion, QuizQuestion, get_question_with_answers, question_page, result_view
from django.conf import settings
from django.conf.urls.static import static


app_name='quiz'

urlpatterns = [
    path('', views.Quiz.as_view(), name='home'),
    path('question/<int:question_id>/', views.get_question_with_answers, name='question_with_answers'),
    path('quiz/<int:quiz_id>/', question_page, name='question_page'),
    path('quiz/result/', result_view, name='quiz_result'),
    path('quiz/submit-answer/', views.submit_answer, name='submit-answer'),
    path('submit-answer/', views.submit_answer, name='submit_answer'),
    path('r/<str:topic>', views.RandomQuestion.as_view(), name='random'),
    path('q/<str:topic>', views.QuizQuestion.as_view(), name='questions'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
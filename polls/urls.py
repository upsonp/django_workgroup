from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    path('list/question', views.QuestionsList.as_view(), name='question_list'),
    path('new/question', views.QuestionCreate.as_view(), name='question_create'),
    path('update/question/<int:pk>', views.QuestionUpdate.as_view(), name='question_update'),

    path('new/choice', views.add_choice, name='add_choice'),
    path('remove/choice', views.remove_choice, name='remove_choice'),
]
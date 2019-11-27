<<<<<<< HEAD
from django.http import HttpResponse
from django.views.generic import ListView
=======
from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.http import JsonResponse
>>>>>>> bb8578f2125789cb74aeba0d6f40b3096b933124

from datetime import datetime

from . import models


def add_choice(request):
    qid = request.GET.get('qid')
    choice_text = request.GET.get('choice_text')

    question = models.Question.objects.get(pk=qid)

    choice = models.Choice(question=question, choice_text=choice_text, votes=0)
    choice.save()

    return JsonResponse({})


def remove_choice(request):
    cid = request.GET.get('cid')

    choice = models.Choice.objects.get(pk=cid)
    choice.delete()

    return JsonResponse({})


class IndexView(TemplateView):
    template_name = "polls/index.html"


class QuestionsList(ListView):
    model = models.Question


class QuestionCreate(CreateView):
    model = models.Question
    fields = ["pub_date", "question_text"]
    success_url = reverse_lazy("polls:question_list")

    def get_initial(self):
        return {
            'pub_date': datetime.now()
        }


class QuestionUpdate(UpdateView):
    model = models.Question
    fields = ["pub_date", "question_text"]
    success_url = reverse_lazy("polls:question_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["choices"] = models.Choice.objects.filter(question=self.object)

        return context

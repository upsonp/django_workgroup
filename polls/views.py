from django.http import HttpResponse
from django.views.generic import ListView

from polls import models


def index(request):
    return HttpResponse("Hello World!")


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    que = models.Question.objects.get(pk=question_id)
    res = models.Choice.objects.filter(question=question_id)

    response = "You're looking at the results of question %s.<br><br>"

    response = response + str(que) + "<br>"
    response = response + "<table style=\"border-style: solid; border-color: red;\"><tr><th>CHOICE</th><th>VOTES</th></tr>"
    for r in res:
        response = response + "<tr><td>" +str(r.choice_text) + "</td><td>" + str(r.votes) + "</td></tr>"

    response = response + "</table>"
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


class PollsList(ListView):
    pass
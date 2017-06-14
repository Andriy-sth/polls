from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import Question
from django.http import HttpResponse
from django.template import loader, RequestContext


def index(request):
    latest_questions = Question.objects.order_by('pub_date')[:5]
    template = 'polls/index.html'
    context = {'latest_questions': latest_questions}
    return render(request, template, context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except:
        return render(request, 'polls/detail.html', {'question': question, 'error_message': 'select a choice'})
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return redirect(reverse('polls:results', args=(question.id,)))

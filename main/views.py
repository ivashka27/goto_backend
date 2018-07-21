from django.http import *
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from datetime import datetime


from main.models import Choice, Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'main/index.html', context)


def detail(request):
    try:
        sel_choice = request.POST['choice']
        pab_dat = request.POST['pub_date']
        summ = request.POST['summary']
        aut = request.POST['author']
    except (KeyError, Choice.DoesNotExist):
        sel_choice = ""
        aut = ""
        summ = ""
        pab_dat = '2018-08-08'
    q = Question()
    q.summary = summ
    q.question_text = sel_choice
    q.pub_date = pab_dat
    q.save()
    return render(request, 'main/detail.html', {'sel_choice': sel_choice})


def results(request, question_id):

    response = "You're looking at the results of question %s."
    return HttpResponse(response % (question_id))

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'main/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('results', args=(question.id,)))

def long_test_form(request):
    if request.method == 'POST':
        question_text = request.POST['question_text']
        summary = request.POST['summary']

        q = Question()
        q.summary = summary
        q.question_text = question_text
        q.pub_date = datetime.now()

        q.save()
        return HttpResponseRedirect(reverse('detail', args=(q.id,)))

    return render(request, 'main/form.html', {})
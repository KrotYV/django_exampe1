from django.shortcuts import render
from django.http import HttpResponse

from poll.models import Question, Choice
# from django.utils import timezone


def index(request):
    resp = ''
    n = Question.objects.count()

    for i in range(n):
        q = Question.objects.get(id=i+1)
        resp += '<b>Quastion:</b> {1:%d-%m-%Y %H:%M} - {0}<br>'\
            .format(q, q.pub_date)
        # resp += f'<b>Quastion:</b> {q} --> {q.pub_date} - ' \
        #         f'{q.pub_date:%d.%m.%Y %H:%M} <br>'
        choice_count = q.choice_set.count()
        a = ' '
        for j in range(choice_count):
            resp += f'........{a:<10} ' \
                    f'Votes = {q.choice_set.all()[j].votes:02}; ' \
                    f'{q.choice_set.all()[j]} <br>'

    resp += '<br><br>список вопросов созданных в текущем году: <br>'
    # current_year = timezone.now().year
    # cur = Choice.objects.filter(question__pub_date__year=current_year)
    return HttpResponse(resp)


def index_1(request):
    return HttpResponse('Test hello world 1')
# Create your views here.

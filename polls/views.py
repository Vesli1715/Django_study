from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# ВІДОБРАЖЕННЯ НА СТОРІНЦІ

#def index(request):
#    return HttpResponse("Hello, world. youre at the polls index") просте відображення тексту

from .models import Question

def index(request):# відображення в html сторінці через шаблонізатор
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    template = loader.get_template('polls/index.html')# відображення html шаблона
    context ={
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context))

def detail(request, question_id):
    return HttpResponse("Your looking at question test %s." % question_id) # відображення в html сторінці

def results(request, question_id):
    response = "Youre looking at the results of question%s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Youre voting on question%s." % question_id)







    # output = " , ".join([q.question_text for q in latest_question_list]) відображення через генератор списку
    # return HttpResponse(output)

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def print_easy_text(request):
    return HttpResponse("print easy text on page")
   # return render(request,'mainApp/homePage.html')



from django.template import loader

def show_html_1(reqest):
    template = loader.get_template('mainApp/test_html_page1.html')  # відображення html шаблона

    return HttpResponse(template.render())

def show_html_2(reqest):
    template = loader.get_template('mainApp/test_html_page2.html')  # відображення html шаблона

    return HttpResponse(template.render())

def show_html_3(reqest):
    template = loader.get_template('mainApp/test_html_page3.html')  # відображення html шаблона

    return HttpResponse(template.render())

def mainPage(request):

    list_of_links = [show_html_1(request),2,3,4]
    template = loader.get_template('mainApp/html_mainPage.html')  # відображення html шаблона
    context = {
        'list_of_links': list_of_links,
    }
    return HttpResponse(template.render(context))

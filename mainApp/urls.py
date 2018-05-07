from django.conf.urls import include, url
from . import views

urlpatterns = [

    #url(r'^$', views.print_easy_text),#
    url(r'^links', views.mainPage),
    url(r'^1/', views.show_html_1),
    url(r'^2/', views.show_html_2),
    url(r'^3/', views.show_html_3),

]
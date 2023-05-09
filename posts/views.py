from datetime import date

from django.shortcuts import HttpResponse, redirect

# Create your views here.
""" MVC - Model View Controller """

""" Controller's """


def hello_view(request):
    if request.method == 'GET':
        return HttpResponse('Hello, its my first view! :)')


def redirect_to_youtube_view(request):
    if request.method == 'GET':
        return redirect('https://www.youtube.com/')


def redirect_to_google(request):
    if request.method == 'GET':
        return redirect('https://www.google.com/')


def redirect_to_github(request):
    if request.method == 'GET':
        return redirect('https://www.github.com/')


def helloview(request):
    if request.method == 'GET':
        return HttpResponse('Hello! Its my project')


def now_date(request):
    if request.method == 'GET':
        today = date.today()
        return HttpResponse(str(today))


def now_date_v2(request):
    if request.method == 'GET':
        return redirect('https://www.calendardate.com/todays.htm')


def goodby(request):
    if request.method == 'GET':
        return HttpResponse('Goodby user!')


from django.shortcuts import render
from django.http import HttpResponse
from .models import Board

def boards(request):
    boards = Board.objects.all()
    return render(request, 'boards.html', {'boards':boards})

def index(request):
    return HttpResponse('Bye!!')

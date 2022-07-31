from django.shortcuts import render

rooms = [
    {'id': 1, 'name': 'Learn Python'},
    {'id': 2, 'name': 'Learn Design'},
    {'id': 3, 'name': 'Frontend Devs Assemble'},
]


def home(request):
    context = {'rooms': rooms}
    return render(request, 'home.html', context)


def room(request):
    return render(request, 'room.html')

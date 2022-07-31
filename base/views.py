from django.shortcuts import render

rooms = [
    {'id': 1, 'name': 'Learn Python'},
    {'id': 2, 'name': 'Learn Design'},
    {'id': 3, 'name': 'Frontend Devs Assemble'},
]


def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, id):
    found_room = None
    for room in rooms:
        if room['id'] == int(id):
            found_room = room
    context = {'room': found_room}
    return render(request, 'base/room.html', context)

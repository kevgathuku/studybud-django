from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Room, Topic
from .forms import RoomForm


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Invalid credentials')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')

    context = {}
    return render(request, 'base/login_register.html', context)


def logout_user(request):
    logout(request)
    return redirect('home')


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    # icontains -> case insensitive
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )
    topics = Topic.objects.all()
    room_count = rooms.count()
    context = {'rooms': rooms, 'topics': topics, 'room_count': room_count}
    return render(request, 'base/home.html', context)


def room(request, id):
    room = Room.objects.get(id=id)
    context = {'room': room}
    return render(request, 'base/room.html', context)


@login_required(login_url='login')
def create_room(request):
    form = RoomForm()

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)


@login_required(login_url='login')
def update_room(request, id):
    room = Room.objects.get(id=id)
    form = RoomForm(instance=room)

    if request.user != room.host:
        return HttpResponse('Not allowed to do that')

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)


@login_required(login_url='login')
def delete_room(request, id):
    room = Room.objects.get(id=id)

    if request.user != room.host:
        return HttpResponse('Not allowed to do that')

    if request.method == 'POST':
        room.delete()
        return redirect('home')

    context = {'obj': room}
    return render(request, 'base/delete.html', context)

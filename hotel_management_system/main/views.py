from django.shortcuts import render, redirect

from accounts.forms import StaffRegistrationForm

from django.contrib.auth.decorators import login_required

from .models import *
from accounts.models import Staff

from django.contrib import messages

# Create your views here.


@login_required()
def index(request):

    applicable_rm = Rooms.objects.filter(reserved=False)

    available_rooms = applicable_rm.count()
    standard_rooms = applicable_rm.filter(room_type="Standard").count()
    deluxe_rooms = applicable_rm.filter(room_type="Deluxe").count()
    suite = applicable_rm.filter(room_type="Suite").count()

    if Staff.objects.filter(user=request.user):
        is_staff_user = True
    else:
        is_staff_user = False

    context = {
        'available_rooms': available_rooms,
        'standard_rooms': standard_rooms,
        'deluxe_rooms': deluxe_rooms,
        'suite': suite,
        'is_staff_user': is_staff_user
    }

    return render(request, 'home/index.html', context=context)


@login_required()
def reserve(request):
    applicable_rm = Rooms.objects.filter(reserved=False)

    if request.method == 'POST':
        print(request.POST)
        quantity = request.POST.get('quantity')
        room_type = request.POST.get('room_type')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        if request.POST.get('smoking') == 'on':
            smoking = True
        else:
            smoking = False

        rooms = applicable_rm.filter(capacity=quantity).filter(
            room_type=room_type).filter(smoking=smoking).order_by('rate')
        return render(request, 'home/reserve.html', context={'data': rooms})

    available_rooms = applicable_rm.count()
    standard_rooms = applicable_rm.filter(room_type="Standard").count()
    deluxe_rooms = applicable_rm.filter(room_type="Deluxe").count()
    suite = applicable_rm.filter(room_type="Suite").count()

    context = {
        'available_rooms': available_rooms,
        'standard_rooms': standard_rooms,
        'deluxe_rooms': deluxe_rooms,
        'suite': suite,
    }
    return render(request, 'home/reserve.html', context=context)


@login_required()
def book_room(request, room_id):
    context = {
        "data": Rooms.objects.filter(room_id=room_id),
    }
    return render(request, "home/book.html", context=context)


@login_required()
def confirm_booking(request):
    if request.method == "POST":
        print(request.POST)
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        room = request.POST.get('room')

        res = Reserve(
            user=request.user,
            room=Rooms.objects.get(room_id=room),
            start_date=start_date,
            end_date=end_date,
            additional_fees=0
        )

        res.save()

        Rooms.objects.filter(room_id=room).update(reserved=True)

        messages.info(request, "Room Booked Successfully!")
        return redirect('/')


@login_required()
def my_rooms(request):
    data = Reserve.objects.filter(user=request.user)
    return render(request, 'profile/my_rooms.html', context={'data': data})

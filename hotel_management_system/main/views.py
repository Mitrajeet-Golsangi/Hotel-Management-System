from django.shortcuts import render, redirect


from django.contrib.auth.decorators import login_required

from .models import *
from accounts.models import Staff

from django.contrib import messages

from django.http import JsonResponse
import json
from django.core.serializers import serialize


# Create your views here.


@login_required()
def index(request):

    applicable_rm = Rooms.objects.filter(reserved=False)

    available_rooms = applicable_rm.count()
    standard_rooms = applicable_rm.filter(room_type="Standard").count()
    deluxe_rooms = applicable_rm.filter(room_type="Deluxe").count()
    suite = applicable_rm.filter(room_type="Suite").count()

    data = Reserve.objects.all()

    if Staff.objects.filter(user=request.user):
        is_staff_user = True
    else:
        is_staff_user = False

    context = {
        'available_rooms': available_rooms,
        'standard_rooms': standard_rooms,
        'deluxe_rooms': deluxe_rooms,
        'suite': suite,
        'is_staff_user': is_staff_user,
        'data': data
    }

    return render(request, 'home/index.html', context=context)


# ------------------------------------------------ Staff Views ------------------------------------------------ #

@login_required()
def change_reservation_status(request, id):
    room = Rooms.objects.get(room_id=id)
    data = Reserve.objects.filter(room=room)

    context = {
        "data": data
    }

    return render(request, 'home/staff/change_reservation.html', context=context)


@login_required()
def update_reservation(request):
    if request.method == "POST":
        room = request.POST.get('room')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        # print(request.POST)
        return redirect('home')
    return redirect(request, 'home/index.html')


@login_required()
def delete_reservation(request):
    data = json.loads(request.body)
    room = Rooms.objects.get(room_id=data['room'])
    Reserve.objects.filter(room=room).delete()
    Rooms.objects.get(room_id=data['room']).update(reserved=False)
    return render(request, 'home/index.html')

# ------------------------------------------------ Guest Views ------------------------------------------------ #


@login_required()
def reserve(request):
    applicable_rm = Rooms.objects.filter(reserved=False)

    if request.method == 'POST':
        data = json.loads(request.body)
        quantity = data['quantity']
        smoking = data['smoking']

        rooms = applicable_rm.filter(capacity=quantity).filter(
            smoking=smoking)
        serialized_rooms = serialize('json', rooms)

        return JsonResponse({'data': serialized_rooms})
    else:
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
        return render(request, 'reservation/reserve.html', context=context)


@login_required()
def book_room(request, room_id):
    context = {
        "data": Rooms.objects.filter(room_id=room_id),
    }
    return render(request, "home/book.html", context=context)


@login_required()
def confirm_booking(request):
    if request.method == "POST":
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

from django.shortcuts import render

from accounts.forms import StaffRegistrationForm

from django.contrib.auth.decorators import login_required

from .models import *

# Create your views here.


@login_required()
def index(request):
    return render(request, 'home/index.html')


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

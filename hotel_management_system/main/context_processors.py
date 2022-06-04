from accounts.models import Staff


def base_context_provider(request):
    is_staff_user = False

    if request.user.is_authenticated:
        if Staff.objects.filter(user=request.user):
            is_staff_user = True

    return {
        "is_staff_user": is_staff_user
    }

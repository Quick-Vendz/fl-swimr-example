from django.shortcuts import render

def front_view(request):
    context = {
        'page': 'front_view',
    }
    return render(request, 'a_FRONT/front_view.html', context)

def classes_view(request):
    section = request.GET.get('section', None)
    context = {
        'page': 'classes_view',
        'highlight_section': section,
    }
    return render(request, 'a_FRONT/classes_view.html', context)

def instructors_view(request):
    context = {
        'page': 'instructors_view',
    }
    return render(request, 'a_FRONT/instructors_view.html', context)

def my_bookings_view(request):
    context = {
        'page': 'my_bookings_view',
    }
    return render(request, 'a_FRONT/my_bookings_view.html', context)

def weekly_schedule_view(request):
    context = {
        'page': 'schedule_view',
    }
    return render(request, 'a_FRONT/schedule_view.html', context)

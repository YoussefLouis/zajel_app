from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .models import DimHub
from django.contrib import messages

# Mock data for uavs
uavs = [
    {
        'id': 1203,
        'production_date': '01-01-2024',
        'last_maintained_at': '01-01-2024',
        'is_flying': True,
        'is_in_service': True,
        'flight_hours': 5,
        'weight': 5.5
    },
]
# Mock data for flights
flights = [
    {
        'id': 1,
        'from': 'Dahab',
        'to': 'Nuweiba',
        'partner': 'Partner A',
        'status': 'In Progress',
        'uav': 'UAV Model X',
        'payload': 'Medical Supplies',
        'coordinates': [[28.484482, 34.494616], [29.034460, 34.659305]]
    },
    {
        'id': 2,
        'from': 'Dahab',
        'to': 'Sharm El Sheikh',
        'partner': 'Partner B',
        'status': 'Completed',
        'uav': 'UAV Model Y',
        'payload': 'Vaccines',
        'coordinates': [[28.484482, 34.494616], [27.881931, 34.299885]]
    },
    # Add more mock flights as needed
]


def login_view(request):
    if request.session.get('hub_id'):
        return redirect('flights')  # Redirect to flights page if already logged in

    error_message = None

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            hub = form.cleaned_data['username']
            password = form.cleaned_data['password']
            if hub.password == password:  # Note: This is not secure. Use hashed passwords in production.
                request.session['hub_id'] = hub.hub_id
                request.session['hub_name'] = hub.name_en
                return redirect('/')  # Redirect to the home page or dashboard
            else:
                error_message = 'Invalid username or password.'
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form, 'error_message': error_message})

def flights_view(request):
    if not request.session.get('hub_id'):
        return redirect('login')  # Redirect to login if not logged in
    return render(request, 'flights.html', {'flights': flights})  # Render the flights template

def uavs_view(request):
    if not request.session.get('hub_id'):
        return redirect('login')
    return render(request, 'uavs.html', {'uavs': uavs})

def maintenance_view(request):
    if not request.session.get('hub_id'):
        return redirect('login')
    return render(request, 'maintenance.html')

def settings_view(request):
    if not request.session.get('hub_id'):
        return redirect('login')
    return render(request, 'settings.html')

def logout_view(request):
    request.session.flush()  # Clear all session data
    return redirect('login')
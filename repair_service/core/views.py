from django.shortcuts import render
from .models import *

from django.contrib.auth.decorators import login_required
# Create your views here.

from django.shortcuts import render
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from .forms import RegisterForm, ServiceRequestForm, UpdateStatusForm

from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, 'core/home.html')
    
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            role = form.cleaned_data.get('role')
            group, created = Group.objects.get_or_create(name=role)
            user.groups.add(group)
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'core/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(request, username=uname, password=pwd)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'core/login.html', {'error': 'Invalid credentials'})
    return render(request, 'core/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
    
    from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    if request.user.groups.filter(name='external').exists():
        return render(request, 'core/dashboard_external.html')

    elif request.user.groups.filter(name='internal').exists():
        return render(request, 'core/dashboard_internal.html')

    else:
        return render(request, 'core/dashboard_generic.html')  # fallback


from .forms import ServiceRequestForm

from django.utils import timezone
from .sheets_sync import push_to_sheet  # Import the function

@login_required
def submit_request(request):
    if not request.user.groups.filter(name='external').exists():
        return redirect('dashboard')

    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.user = request.user
            service_request.save()

            #push data to Google Sheets
            push_to_sheet({
                'name': request.user.username,
                'serial_number': service_request.serial_number,
                'product_name': service_request.product_name,
                'date_of_purchase': str(service_request.date_of_purchase),
                'fault_description': service_request.fault_description,
                'status': service_request.status,
                'submitted_at': str(timezone.now())
            })

            return render(request, 'core/request_success.html')
    else:
        form = ServiceRequestForm()

    return render(request, 'core/service_request.html', {'form': form})
    
@login_required
def view_requests(request):
    if not request.user.groups.filter(name='internal').exists():
        return redirect('dashboard')  # Block others

    requests = ServiceRequest.objects.all().order_by('-submitted_at')
    return render(request, 'core/view_requests.html', {'requests': requests})    
    
@login_required
def update_status(request, request_id):
    if not request.user.groups.filter(name='internal').exists():
        return redirect('dashboard')

    sr = ServiceRequest.objects.get(id=request_id)
    if request.method == 'POST':
        form = UpdateStatusForm(request.POST, instance=sr)
        if form.is_valid():
            form.save()
            return redirect('view_requests')
    else:
        form = UpdateStatusForm(instance=sr)

    return render(request, 'core/update_status.html', {'form': form, 'service_request': sr})    
    



from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import FAQ

@csrf_exempt
def chatbot_response(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_msg = data.get('message', '').lower()

        # Search in all FAQ entries
        faqs = FAQ.objects.all()

        reply = "Sorry, I didn’t understand. Please rephrase your question."

        for faq in faqs:
            if all(word in user_msg for word in faq.question.lower().split()):
                reply = faq.answer
                break

        return JsonResponse({'reply': reply})
        
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ServiceRequest
import json

@csrf_exempt
def track_status(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        serial = data.get('serial_number')

        try:
            request_obj = ServiceRequest.objects.get(serial_number=serial, user=request.user)
            return JsonResponse({'success': True, 'status': request_obj.status})
        except ServiceRequest.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'No service request found for that serial number'})        
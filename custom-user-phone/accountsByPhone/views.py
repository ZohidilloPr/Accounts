from django.shortcuts import redirect, render
from .forms import RegisterUser
from .models import UserByPhoneNumber
from django.views.generic import CreateView
# Create your views here.

# def register(request):
#     if request.method == 'POST':
#         form = RegisterUser(request.POST)
#         if form.is_valid():
#             form.save()
#            login(request, user)
#             return redirect('Home')
#     form = RegisterUser
#     return render(request, 'register/register.html', {'form':form})

class RegisterCreateView(CreateView):
    model = UserByPhoneNumber
    form_class = RegisterUser
    template_name = 'register/register.html'
    success_url = '/'
from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth import get_user_model
from user.forms import UserForm
from django.views import View
User = get_user_model()


# Create your views here.

# def signup(request):
#     if request.POST:
#         # username = request.POST.get('user')
#         password1 = request.POST.get('password1')
#         password2 = request.POST.get('password2')
#         email = request.POST.get('email')
#         kwargs ={"password":password1,"email":email}
#         user = User.objects.create_user(**kwargs)
#         if user:
#             return redirect('user:login')
#     return render(request,template_name='user/signup.html')

# def login_user(request):
#     if request.POST:
#         email = request.POST.get('email')
#         password = request.POST.get('password1')
#         user = authenticate(email= email, password=password)
#         if user is not None:
#             messages.success(request, "Login Successful")
#             login(request, user)
#             return redirect('home:home')
#         else:
#             messages.error(request, 'Invalid Credentials')
#             return redirect('user:login')
#     return render(request, template_name='user/signin.html')


# def logout_user(request):
#     logout(request)
#     return redirect('home:home')

class SignupView(View):
    template_name="user/signup.html"

    def get(self, request, *args, **kwargs):
        form = UserForm()
        return render(request, self.template_name,context={'form':form})

    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST)
        print(form.as_p())
        print(request.POST)
        if form.is_valid():
            # form.clean_password()
            # form.save()
            User.objects.create_user(email=form.cleaned_data.get('email'), password=form.cleaned_data.get('password'))
            return redirect('user:login')
        messages.error(request, "Email already exists")
        return redirect('user:signup')


class SignInView(View):
    template_name = "user/signin.html"

    def get(self, request, *args, **kwargs):
        
        return render(request, self.template_name,context={"next": request.GET.get("next")})

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password1')
        next = request.POST.get("next")
        # print("EMAIL_________",email , "PASSWORD:",password)
        user = authenticate(email= email, password=password)
        if user is not None:
            messages.success(request, "Login Successful")
            login(request, user)
            
            if next:
                return redirect(next)
            return redirect('ecom:home')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('user:login')

class SignOutView(View):
    # template_name = "home/logout.html"

    def get(self, request):
        logout(request)
        return redirect('ecom:home')
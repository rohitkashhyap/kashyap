from django.shortcuts import render, redirect,HttpResponseRedirect
from django.views.generic import TemplateView, CreateView
from ecom.models import Category
from django.contrib.auth.mixins import LoginRequiredMixin
from urllib.parse import urlencode
from ecom.forms import CategoryForm
from django.conf import settings

# Create your views here.


class HomeView(TemplateView):
    template_name = "ecom/home.html"


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    template_name = "ecom/category.html"
    login_url = settings.LOGIN_URL
    redirect_url = "/"

    fields = ['name','image']

    # def get(self, request, *args, **kwargs):
    #     if not request.user.is_authenticated:
            # url = f"/users/login?{urlencode({'next':request.path})}"
    #         return redirect(url)
    #     categoryform = CategoryForm()
    #     return render(request,template_name=CategoryCreateView.template_name,context={'form':categoryform})



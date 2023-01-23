from django.shortcuts import render, HttpResponse, redirect
from home.forms import ContactForm
from django.views import View
from django.contrib import messages
from django.core.mail import send_mail
from home.utils import handle_uploaded_file
# User = get_user_model()

def home(request):
    return render(request,template_name='home/logout.html')

class ContactView(View):
    template_name="home/contactus.html"

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        return render(request, self.template_name,context={'form':form})

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['image'])
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            message=form.cleaned_data.get('message')
            phone = form.cleaned_data.get('phone')
            image = form.cleaned_data.get('image')
            subject = "Contact Us Form Submission"
            final_message = f'''
            Name: {name}
            Email: {email}
            Message: {message}'''
            if phone!="":
                phone_number = f"Phone: {phone}"
                final_message+=phone_number
            
            # output = send_mail(subject=subject,message=final_message,from_email="rohit444546@gmail.com",recipient_list=["rohit444546@gmail.com"])
            # if output:
            #     messages.success(request, "Your message has been sent successfully. We will get back to you soon.")
            #     return redirect('home:contact')
            values = {"name":name, "email": email, "message":message, "phone":phone,"image":image}
            messages.error(request, "Your message was not sent. Try again")
            form = ContactForm(initial=values)
            return render(request, self.template_name, context={'form':form})
        messages.error(request, "Form was not submitted successfully.")
        return redirect('home:contact')


def about(request):
    return render(request, template_name='home/aboutus.html')    
    

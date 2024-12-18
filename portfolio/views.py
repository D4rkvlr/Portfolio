from django.shortcuts import render, redirect
from .models import ContactMassage
# Create your views here.

def main(request):
    return render(request, 'index.html')

def contact_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        massage = request.POST['massage']
        
        ContactMassage.objects.create(name=name, email=email, subject=subject, massage=massage)
        return redirect('contact')
    
    
    return render(request, 'contact.html')
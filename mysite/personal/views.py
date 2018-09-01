from django.shortcuts import render

def index(request):
    return render(request, 'personal/home.html')

def contact(request):
    return render(request, 'personal/contact.html', {'content':['if you would like to contact me, Send an email to ','devebeme@gmail.com']})

def blog(request):
    return render(request, 'personal/blog.html', {})

from django.shortcuts import render

# FBVs ------------------


def home(request):
    context = {'title': 'Home'}
    return render(request, 'home.html', context)


def about(request):
    context = {'title': 'About'}
    return render(request, 'about.html', context)


def contact(request):
    context = {'title': 'Contact Us'}
    return render(request, 'contact.html', context)


def info(request):
    context = {'title': 'Information'}
    return render(request, 'info.html', context)

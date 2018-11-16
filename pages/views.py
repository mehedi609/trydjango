from django.shortcuts import render

# Create your views here.


def homepage_view(request):
    return render(request, 'pages/home.html', )


def aboutpage_view(request):
    return render(request, 'pages/about.html', )


def contactpage_view(request):
    return render(request, 'pages/contact.html', )


# def socialpage_view(request):
#     return render(request, '', )
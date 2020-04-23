from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {'my_text':  'this is a dummy text', 'my_list': [12, 34, 56],
                                         'my_number': 12345}
                  )


# Create your views here.
def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})
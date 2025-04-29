from django.http import HttpResponse


from django.shortcuts import render
def home(request):
    # return HttpResponse("Hello, World. Learning Django")
    return render(request, 'index.html')

def about(request):
    return HttpResponse("Hello, World. Learning Django.. about")


def contact(request):
    return HttpResponse("Hello, World. Learning Django.. contact")

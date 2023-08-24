from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "html/index.html")


def users_list(request):
    return render(request, "")

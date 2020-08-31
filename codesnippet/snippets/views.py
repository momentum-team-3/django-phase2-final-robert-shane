from django.shortcuts import render

# Create your views here.
def snippet_test(request):
    return render(request, "base.html")
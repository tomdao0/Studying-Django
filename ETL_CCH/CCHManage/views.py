from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    # return HttpResponse("CCH Manage apps")
    return render(
        request,
        template_name="index.html",
        context={"name": "Tom Dao", "appname": "CCH Manage"},
    )

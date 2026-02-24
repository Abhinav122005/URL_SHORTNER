from django.shortcuts import render,redirect,get_object_or_404
from .models import URL

def home(request):
    if request.method=="POST":
        original_url=request.POST.get('original_url')
        url=URL(original_url=original_url)
        url.save()
        short_url=request.build_absolute_uri('/')+url.short_code
        return render(request,'home.html',{'short_url':short_url})
    return render(request,'home.html')
def redirect_url(request,short_code):
    url=get_object_or_404(URL,short_code=short_code)
    return redirect(url.original_url)

# Create your views here.

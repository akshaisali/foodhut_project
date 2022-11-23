from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User


def index(request):
    return render (request,"index.html")

def signup(request):
	if request.method == 'POST':
		uname = request.POST.get('uname')
		pwd = request.POST.get('pwd')
		phn= request.POST.get('phn')
		address=request.POST.get('address')
		# print(uname, pwd)
		if User.objects.filter(username=uname).count()>0:
			return HttpResponse('Username already exists.')
		else:
			user = User(username=uname, password=pwd,phoneno=phn,address=address)
			user.save()
			return render(request,'login.html')
	else:
		return render(request, 'signup.html')
def login(request):
	if request.method == 'POST':
		uname =request.POST.get('uname')
		pwd = request.POST.get('pwd')
		check_user = User.objects.filter(username=uname, password=pwd)
		if check_user:
			request.session['user'] = uname
			request.session['pwd'] = pwd
			return render(request,'ourmenu.html')
		else:
			return HttpResponse('Please enter valid Username or Password.')

	return render(request, 'login.html')
def salad(request):
    return render( request,'order.html')
def pizza(request):
    return render( request,'order.html')
def burger(request):
    return render( request,'order.html')
def drinks(request):
    return render( request,'order.html')
def seafood(request):
    return render( request,'order.html')
def dessert(request):
    return render( request,'order.html')

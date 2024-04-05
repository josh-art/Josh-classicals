from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login as dj_login
from django.http.response import JsonResponse, HttpResponse
from django.contrib.auth import authenticate, logout
from django.contrib import messages, auth


def signup(request):
    return render(request, "register.html")


# view for rendering login page
def login(request):
    return render(request, "login.html")


def handlesignup(request):
    if request.method == 'POST':
        # get the post parameters
        username = request.POST["uname"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        phone = request.POST["phone"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        # check for errors in input
        if request.method == 'POST':
            try:
                user_exists = User.objects.get(username=request.POST['uname'])
                messages.error(
                    request, " Username already taken, Try another username!!!")
                return redirect("/signup")
            except User.DoesNotExist:
                if len(username) > 15:
                    messages.error(
                        request, " Username must be max 15 characters, Please try again")
                    return redirect("/signup")
                if not username.isalnum():
                    messages.error(
                        request, " Username should only contain letters and numbers, Please try again")
                    return redirect("/signup")
                if password1 != password2:
                    messages.error(
                        request, " Password do not match, Please try again")
                    return redirect("/signup")
        # create the user
        user = User.objects.create_user(username, email, password1)
        user.first_name = fname
        user.last_name = lname
        user.phone = phone
        user.save()
        messages.success(
            request, " Your account has been successfully created<br>Please login below")
        return redirect("user:login")
    else:
        return HttpResponse('404 - NOT FOUND ')


# view for rendering data from login page
def handlelogin(request):
    if request.method == 'POST':
        # get the post parameters
        name = request.POST["uname"]
        password = request.POST["password1"]
        user = authenticate(username=name, password=password)
        # cheching for valid login
        if user is not None:
            dj_login(request, user)
            messages.success(request, "")
            return redirect("shops:Home")
        else:
            messages.error(request, " Invalid Credentials, Please try again")
            return redirect("user:login")
    return HttpResponse('404 - NOT FOUND ')


# view for rendering logout
def handlelogout(request):
    logout(request)
    messages.success(request, " Successfully logged out")
    return redirect('/')

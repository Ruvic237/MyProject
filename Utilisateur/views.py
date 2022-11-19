from django.contrib import messages, auth
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from Utilisateur.forms import Signing_up


def logini(request):
    error = ''
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            error = 'password or username is incorrect'

    return render(request, 'login.html', {'error': error})


# Creating a view for registration page
def register(request):

        # Determine if user submitted the form
        if request.method == 'POST':

            # Create an instance of django form class with submitted form as argument
            form = Signing_up(request.POST)

            # Determine if submitted form is valid or not
            if form.is_valid():
                # Save valid objects in user table
                form.save()

                # username = form.cleaned_data['username']
                # A flash message to display in login page
                # messages.success(request, f"Hey {username} your account is created successfully! ")

                return redirect('login')

        # If user don't submit show empty form
        else:
            form = Signing_up()

        context = {
            "form": form,
        }
        return render(request, 'reg.html', context)


def student(request):
    return render(request, 'student.html')


def teacher(request):
    return render(request, 'teacher.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def logout(request):
    return redirect('logini')


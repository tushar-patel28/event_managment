from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.urls import reverse

# Create your views here.


def index(request):
    return render(request, 'register/index.html', {})


def admin_register(request):

    registered = False

    if request.method == 'POST':

        form_p = UserForm(request.POST)
        form = RegisterForm(request.POST, request.FILES)

        if form.is_valid() and form_p.is_valid():

                user = form_p.save()
                user.set_password(user.password)
                user.save()

                form_r = form.save(commit=False)
                form_r.user = user  # here connected OneToOneField with user table

                form_r.save()
                messages.info(request, "Registered Successfully")
                return redirect('register:user_login')
        else:
            print(form_p.errors, form.errors)
    else:
        form_p = UserForm()
        form = RegisterForm()

    return render(request, 'register/a_register.html', {'form': form,
                                                               'form_p': form_p,
                                                               'registered': registered})
def cordinator_register(request):

    registered = False

    if request.method == 'POST':

        form_p = CUserForm(request.POST)
        form = CRegisterForm(request.POST, request.FILES)

        if form.is_valid() and form_p.is_valid():

            user = form_p.save()
            user.set_password(user.password)
            user.save()

            form_r = form.save(commit=False)
            form_r.user = user  # here connected OneToOneField with user table
            form_r.save()
            messages.info(request, "Registered Successfully")
            return redirect('university:cordinator_list')
        else:
            print(form_p.errors, form.errors)
    else:
        form_p = CUserForm()
        form = CRegisterForm()

    return render(request, 'university/c_register.html', {'form': form,
                                                               'form_p': form_p,
                                                               'registered': registered})

def student_register(request):

    registered = False

    if request.method == 'POST':

        form_p = SUserForm(request.POST)
        form = SRegisterForm(request.POST, request.FILES)

        if form.is_valid() and form_p.is_valid():

            user = form_p.save()
            user.set_password(user.password)
            user.save()

            form_r = form.save(commit=False)
            form_r.user = user  # here connected OneToOneField with user table
            form_r.save()
            messages.info(request, "Registered Successfully")
            return redirect('coedinator:event_list')
        else:
            print(form_p.errors, form.errors)
    else:
        form_p = SUserForm()
        form = SRegisterForm()

    return render(request, 'coedinator/s_register.html', {'form': form,
                                                               'form_p': form_p,
                                                               'registered': registered})

# login page view


def visitor_register(request):

    registered = False

    if request.method == 'POST':

        form_p = VUserForm(request.POST)
        form = VRegisterForm(request.POST, request.FILES)
        print(True)

        if form.is_valid() and form_p.is_valid():

            user = form_p.save()
            user.set_password(user.password)
            user.save()

            form_r = form.save(commit=False)
            form_r.user = user  # here connected OneToOneField with user table
            form_r.save()
            messages.info(request, "Registered Successfully")
            return redirect('register:visitor_login')
        else:
            print(form_p.errors, form.errors)
    else:
        form_p = VUserForm()
        form = VRegisterForm()

    return render(request, 'register/v_register.html', {'form': form,
                                                               'form_p': form_p,
                                                               'registered': registered})


def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            try:  # Check it the account is active
                type = AdminRegister.objects.get(user__password=user.password, user__username=user.username)
                if user.is_active and type.is_uni == True:
                    # Log the user in.
                    login(request, user)
                    # Send the user back to some page.
                    # In this case their homepage.
                    return HttpResponseRedirect(reverse('register:c_register'))
                else:
                    # If account is not active:
                    messages.info(request, 'Your Account is Not Active Please Contact Admin')
                    return HttpResponseRedirect(reverse('register:user_login'))
            except:

                type3 = CordinatorRegister.objects.get(user__password=user.password)
                if user.is_active and type3.is_cordinator == True:
                    # Log the user in.
                    login(request, user)
                    # Send the user back to some page.
                    # In this case their homepage.
                    return HttpResponseRedirect(reverse('coedinator:add_event'))
                else:
                    # If account is not active:
                    messages.info(request, 'Your Account is Not Active Please Contact Admin')
                    return HttpResponseRedirect(reverse('register:user_login'))

                # type2 = StudentRegister.objects.get(user__password=user.password)
                # if user.is_active and type2.is_student == True:
                #     # Log the user in.
                #     login(request, user)
                #     # Send the user back to some page.
                #     # In this case their homepage.
                #     return HttpResponseRedirect(reverse('student:events'))
                # else:
                #     # If account is not active:
                #     messages.info(request, 'Your Account is Not Active Please Contact Admin')
                #     return HttpResponseRedirect(reverse('register:user_login'))

        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            messages.info(request, 'Invalid Login Details')
            return HttpResponseRedirect(reverse('register:user_login'))

    else:
        # Nothing has been provided for username or password.
        return render(request, 'register/login.html', {})


def visitor_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:

            type = VisitorRegister.objects.get(user__password=user.password, user__username=user.username)
            if user.is_active and type.is_visitor == True:
                # Log the user in.
                #                     login(request, user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse('visitors:event_list'))
            else:
                # If account is not active:
                messages.info(request, 'Your Account is Not Active Please Contact Admin')
                return HttpResponseRedirect(reverse('register:visitor_login'))

        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            messages.info(request, 'Invalid Login Details')
            return HttpResponseRedirect(reverse('register:user_login'))

    else:
        # Nothing has been provided for username or password.
        return render(request, 'register/login.html', {})

def student_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            type2 = StudentRegister.objects.get(user__password=user.password)
            if user.is_active and type2.is_student == True:
                # Log the user in.
                login(request, user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse('student:events'))
            else:
                # If account is not active:
                messages.info(request, 'Your Account is Not Active Please Contact Admin')
                return HttpResponseRedirect(reverse('register:user_login'))

        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            messages.info(request, 'Invalid Login Details')
            return HttpResponseRedirect(reverse('register:visitor_login'))

    else:
        # Nothing has been provided for username or password.
        return render(request, 'register/v_login.html', {})

def student_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('register:student_login'))

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('register:user_login'))

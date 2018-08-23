from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import (EditProfileForm, RegisterForm)
from django.contrib.auth.models import User
from .models import UserInformation, Country, City
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponseRedirect


def home(request):
    return render(request, 'polls/home.html')

    
def register(request):
    user_form = RegisterForm()
    country = Country.objects.all()
    city = City.objects.all()

    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid(): 
            
            user = User.objects.create_user(username=user_form.cleaned_data['username'],
                                 first_name=user_form.cleaned_data['first_name'],
                                 last_name=user_form.cleaned_data['last_name'],
                                 password=user_form.cleaned_data['password1'],
                                 email=user_form.cleaned_data['email'])

            UserInformation.objects.create(user=user, country=user_form.cleaned_data['country'], city=user_form.cleaned_data['city'])
            return redirect('/login/')

    args = {'user_form': user_form, 'country': country, 'city': city}
    return render(request, 'polls/reg_form.html', args)


@login_required(login_url='/login')
def profile(request):
    data = UserInformation.objects.get(user = request.user)
    args = {'user': request.user, 'data': data}
    return render(request, 'polls/profile.html', args)


@login_required(login_url='/login')
def profile_edit(request):
    country = Country.objects.all()
    city = City.objects.all() 
    edit_form = EditProfileForm()
    if request.method == 'POST':
        edit_form = EditProfileForm(request.POST)
        if edit_form.is_valid():
            
            User.objects.filter(username=request.user.username).update(first_name=edit_form.cleaned_data['first_name'],
                                                          last_name=edit_form.cleaned_data['last_name'],
                                                          email=edit_form.cleaned_data['email'])
            UserInformation.objects.filter(user=request.user).update(country=edit_form.cleaned_data['country'], city=edit_form.cleaned_data['city'])
            return redirect('profile')

    args = {'edit_form': edit_form, 'country': country, 'city': city}
    return render(request, 'polls/profile_edit.html', args)


@login_required(login_url='/login')
def change_password(request):
    form = PasswordChangeForm(user=request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('profile')

    args = {'change_password_form': form}
    return render(request, 'polls/change_password.html', args)


@login_required(login_url='/login')
def friendlist(request):
    users = User.objects.select_related('userinformation').filter(~Q(id=request.user.id))
    args = {'users': users}
    return render(request, 'polls/friendlist.html', args)


@login_required(login_url='/login')
def other_profiles(request):
    if request.method == 'POST':
        srch = request.POST['srch']

        if srch:
            match = User.objects.filter(Q(email__iexact=srch) & ~Q(email__iexact=request.user.email) | 
                                        Q(username__istartswith=srch) & 
                                        ~Q(username__icontains=request.user.username)
                                     )   
            if match:
                return render(request, 'polls/other_profiles.html', {'found': match})
            else:
                messages.error(request, 'No result found')
        else:
            return HttpResponseRedirect('/other_profiles/')

    return render(request, 'polls/other_profiles.html')


@login_required(login_url='/login')
def delete_profile(request):
    request.user.delete() 
    return render(request, 'polls/delete_profile.html')


def cities(request):
    country = request.GET.get('country', None)

    cities = City.objects.filter(country__name=country)

    data = serializers.serialize('json', cities)
    
    return JsonResponse(data, content_type="application/json", safe=False)




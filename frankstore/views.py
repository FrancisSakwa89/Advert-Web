from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import Q
from django.shortcuts import get_object_or_404
from .models import Profile, Advert,Category
from .forms import ProfileForm,NewAdvertForm,RegisterForm,UserUpdateForm, ProfileUpdateForm
from django.views.generic import (ListView,DetailView,CreateView,UpdateView,)
# Create your views here.

@login_required(login_url='/accounts/login/')
def welcome(request):
  id = request.user.id
  profile = Profile.objects.get(user=id)

  return render(request, 'index.html', {'profile':profile})

@login_required(login_url='/accounts/login/')
def searchme(request):
    return render(request, 'searchme.html')

@login_required(login_url='/accounts/login/')
def adverts(request):
  id = request.user.id
  profile = Profile.objects.get(user=id)
  adverts = Advert.objects.all().order_by()
    
  return render(request, 'advert.html', {'adverts':adverts})


@login_required(login_url='/accounts/login/')
def profile(request, id):
  frank = request.user.id
  profile = Profile.objects.get(user=frank)

  user = request.user
  

  adverts = Advert.objects.filter(email=frank).order_by()
  advertscount=adverts.count()


  return render(request, 'profile.html',{'profile':profile,'user':user,'advertscount':advertscount,'adverts':adverts})


@login_required(login_url='/accounts/login/')
def newprofile(request):
  frank = request.user.id
  profile = Profile.objects.get(user=frank)
  # current_user = request.user
  # current_username = request.user.username
  
  if request.method == 'POST':
    instance = get_object_or_404(Profile, user=frank)
    form = ProfileForm(request.POST, request.FILES,instance=instance)
    if form.is_valid():
      form.save()
      # u_profile = form.save(commit=False)
      # u_profile.user = current_user
      # u_profile.save()

    return redirect('profile', frank)

  else:
    form = ProfileForm()

  return render(request, 'newprofile.html',{'form':form,'profile':profile})


@login_required(login_url='/accounts/login/')
def newadvert(request):
  frank = request.user.id
  profile = Profile.objects.get(user=frank)

  current_user = request.user
  current_username = request.user.username

  if request.method == 'POST':
    form = NewAdvertForm(request.POST, request.FILES)
    if form.is_valid():
      adverts = form.save(commit=False)
      adverts.owner = current_user
      adverts.adverts = current_username
      adverts.save()
    return redirect('adverts')

  else:
    form = NewAdvertForm()
# current_user = request.user
  # current_username = request.user.username
  
  return render(request, 'newadvert.html',{'form':form,'profile':profile})


@login_required(login_url='/accounts/login/')
def search(request):
  frank = request.user.id
  profile = Profile.objects.get(user=frank)


  if 'advert' in request.GET and request.GET['advert']:
    search_term = request.GET.get('advert')
    message = f'{search_term}'
    title = 'Search Results'

    try:
      no_ws = search_term.strip()
      searched_advert = Advert.objects.filter(name__icontains = no_ws)
      searched_adverts = searched_advert.filter()

    except ObjectDoesNotExist:
      searched_adverts = []

    return render(request, 'search.html',{'message':message ,'title':title, 'searched_adverts':searched_adverts,'profile':profile})

  else:
    message = 'You haven\'t searched for any advert'
    
    title = 'Search Error'
    return render(request,'search.html',{'message':message,'title':title,'profile':profile})


@login_required(login_url='/accounts/login/')
def advert_remove(request, pk):
    advert = get_object_or_404(Advert, pk=pk)
    advert.delete()
    return HttpResponseRedirect('adverts')
  
    return render(request, 'advert.html')


@login_required(login_url='/accounts/login/')
def myadvert(request, id):
  frank = request.user.id
  profile = Profile.objects.get(user=frank)
  
  myadverts = Myadvert.objects.get(pk=id)

  return render(request, 'store.html',{'profile':profile,'myadverts':myadverts})

@login_required(login_url='/accounts/login/')
def mpesa(request):
    return render(request, 'mpesa.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!,You can now login')
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'registration/registration_form.html',{'form': form})

def category(request,category):

  categories = Category.objects.all()

  if category.objects.get(pk=category):
    adverts = Advert.filter_by_category(category)
    title = (category.objects.get(pk=category)).category

  else:
    raise Http404()

  return render(request,'cat.html',{'title':title,'adverts':adverts, 'categories':categories})

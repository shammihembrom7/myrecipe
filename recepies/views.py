# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from .models import Recipe, Review
from .forms import PostForm, ReviewForm

@login_required(login_url='/login/')
def recipe_create(request):
    u = request.user
    form = PostForm(request.POST or None)
    if form.is_valid():
        title = form.cleaned_data.get('title')
        recipe = form.cleaned_data.get('recipe')
        author = {
            'id': u.id,
            'name': u.username
        }
        instance = Recipe.objects.create(
            title=title,
            recipe=recipe,
            author=author
        )
        instance.save()
        return redirect('/')
    context = {
        "form": form
    }
    return render(request, "post_form.html", context)

def recipe_detail(request, id=None):
    instance = get_object_or_404(Recipe, id=id)
    u = request.user
    form = ReviewForm(request.POST or None)
    if form.is_valid():
        review = form.cleaned_data.get('review')
        user = { 'user_id' : u.id, 'name': u.username}
        inst = Review.objects.create(
            review = review,
            user = user
        )
        inst.save()
        instance.reviews.append(Review(review = review, user = user))
        instance.save()


    content = {
        'form': form,
        "obj" : instance
    }
    return render(request, "detail.html", content)

@login_required(login_url='/login/')
def recipe_list(request):
    if request.user.is_authenticated():
        u = request.user.username
    else:
        u = "login please!"
    queryset = Recipe.objects.all()
    content = {
        "objList": queryset,
        "user": u
    }

    return render(request, "base.html", content)
    #return HttpResponse("<h1>list</h1>")

def recipe_update(request):
    return HttpResponse("<h1>update</h1>")

def recipe_delete(request):
    return HttpResponse("<h1>delete</h1>")

#===================================================================

from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)
from django.contrib.auth.models import User
from .forms import UserLoginForm, UserRegForm


def login_view(request):
    if request.user.is_authenticated():
        return redirect('/')
    title = "login"
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')

    return render(request, "form.html",{'form':form, 'title':title})

def register_view(request):
    title = "register"
    next = request.GET.get('next')
    form = UserRegForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        email = form.cleaned_data.get('email')

        user = User.objects.create_user(username, email, password)
        user.save()

        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect("/")

    context = {
        "form": form,
        "title":title
    }
    return render(request, "form.html", context)

def logout_view(request):
    logout(request)
    next = request.GET.get('next')
    if next:
        return redirect(next)
    return redirect('/')

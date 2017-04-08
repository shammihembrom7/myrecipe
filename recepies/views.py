# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Recipe
from .forms import PostForm

def recipe_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    context = {
        "form": form
    }
    return render(request, "post_form.html", context)

def recipe_detail(request, id=None):
    instance = get_object_or_404(Recipe, id=id)
    content = {
        "obj" : instance
    }
    return render(request, "detail.html", content)

def recipe_list(request):
    # if request.user.is_authenticated():
    #     content = {
    #         "title": "My Recipe List"
    #         }
    # else:
    #     content = {
    #         "title": "List"
    #     }
    queryset = Recipe.objects.all()
    content = {
        "objList": queryset
    }

    return render(request, "index.html", content)
    #return HttpResponse("<h1>list</h1>")

def recipe_update(request):
    return HttpResponse("<h1>update</h1>")

def recipe_delete(request):
    return HttpResponse("<h1>delete</h1>")

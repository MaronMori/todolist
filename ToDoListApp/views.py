from django.shortcuts import render, redirect
from .models import ToDoList
from .forms import add_task

# Create your views here.


def homepage(request):
    todo = ToDoList.objects
    return render(request, "homepage.html", {"tasks": todo})


def new_task(request):
    if request.method == "POST":
        filled_form = add_task(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            return redirect("home")
    else:
        form = add_task()
        return render(request, "task_add.html", {"form": form})


def delete_task(request, pk):
    task = ToDoList.objects.get(pk=pk)
    task.delete()
    return redirect('home')

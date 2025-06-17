from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login
from .models import Task
from .forms import TaskForm, UserRegisterForm, ProfileForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

# Custom login form for design
class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Enter your username',
            'class': 'border-gray-300 rounded w-full px-3 py-2 focus:outline-none focus:ring focus:border-blue-300'
        })
        self.fields['password'].widget.attrs.update({
            'placeholder': 'Enter your password',
            'class': 'border-gray-300 rounded w-full px-3 py-2 focus:outline-none focus:ring focus:border-blue-300'
        })

def register(request):
    # Already logged in hole register page dekhabe na
    if request.user.is_authenticated:
        return redirect('todo_list')  # Or 'home' if your home view is named 'home'
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully! Please login.")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'tasks/register.html', {'form': form})

@login_required(login_url='login')
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'tasks/profile.html', {'form': form})

@login_required(login_url='login')
def todo_list(request):
    tasks = Task.objects.filter(user=request.user).order_by('-created_at')
    pending_count = tasks.filter(is_completed=False).count()
    completed_count = tasks.filter(is_completed=True).count()
    form = TaskForm()
    return render(request, "tasks/todo_list.html", {
        "tasks": tasks,
        "pending_count": pending_count,
        "completed_count": completed_count,
        "form": form,
    })

@login_required(login_url='login')
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, 'Task added!')
        else:
            messages.error(request, 'Please correct the error below.')
    return redirect('todo_list')

@login_required(login_url='login')
def complete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.is_completed = not task.is_completed
    task.save()
    return redirect('todo_list')

@login_required(login_url='login')
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.delete()
    messages.success(request, 'Task deleted!')
    return redirect('todo_list')

@login_required(login_url='login')
def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            if 'complete' in request.POST:
                task.is_completed = True
            task.save()
            return redirect('todo_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/todo_form.html', {'form': form, 'task': task})

def profile_detail(request, username):
    profile_user = get_object_or_404(User, username=username)
    return render(request, 'tasks/profile_detail.html', {'profile_user': profile_user})
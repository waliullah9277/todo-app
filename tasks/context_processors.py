from .forms import TaskForm

def todo_form(request):
    # shob somoy form pathao, authenticated user hole blank form, na hole None
    if request.user.is_authenticated:
        return {'todo_form': TaskForm()}
    else:
        return {'todo_form': None}
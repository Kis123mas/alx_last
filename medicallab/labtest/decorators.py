from django.shortcuts import redirect
from django.urls import reverse

def prevent_logged_in_user(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('dashboard'))  # Redirect to the 'home' URL
        return view_func(request, *args, **kwargs)
    return wrapper

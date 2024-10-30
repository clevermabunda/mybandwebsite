from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.

def user_login(request):
    """
    Render the login page for users.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered login page.
    """
    return render(request, 'authentication/login.html')

def authenticate_user(request):
    """
    Authenticate the user based on provided credentials.

    This view checks the username and password from the POST request.
    If authentication fails, it redirects back to the login page.
    If successful, it logs in the user and redirects to the band list page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponseRedirect: Redirects to the login page or the band list page.
    """
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(reverse('user_auth:login'))
    else:
        login(request, user)
        return HttpResponseRedirect(reverse('band_list'))

def show_user(request):
    """
    Display the currently logged-in user's information.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered user information page.
    """
    print(request.user.username)  # Debugging line
    return render(request, 'authentication/user.html', {
        "username": request.user.username,
        "password": request.user.password  # Note: This is not secure; avoid displaying passwords.
    })

class SignUpView(generic.CreateView):
    """
    View for user registration.

    This view handles user sign-up using the Django UserCreationForm.
    On successful registration, it redirects to the login page.

    Attributes:
        form_class: The form used for user registration.
        success_url: The URL to redirect to after a successful registration.
        template_name: The template used for rendering the sign-up page.
    """
    form_class = UserCreationForm
    success_url = reverse_lazy("user_auth:login")
    template_name = "authentication/signup.html"

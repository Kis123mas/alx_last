# ------------------------------------------------------------
# Django Web Application for Laboratory or Medical Testing System
# ------------------------------------------------------------

# This Django code defines views, models, and forms for a web application
# that appears to be related to a laboratory or medical testing system.

# It uses Django's built-in features as well as the Django REST framework
# for creating API endpoints. The code is structured into several classes
# and functions for different purposes, such as user registration, login,
# dashboard, staff management, customer management, and test management.

# It also includes functionality for generating PDF reports using pdfkit,
# and it configures pdfkit with the path to wkhtmltopdf.

# The code follows good practices by separating concerns into different
# components and utilizing Django's class-based views for reusability.
# It employs authentication and authorization mechanisms for user access control.

# Notable components include user registration, login, staff and customer
# management, test creation and viewing, and PDF generation.

# Proper documentation and comments would make it even more maintainable
# and understandable. The code can be further improved with comprehensive
# documentation and comments for each function, class, and important logic.

from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer, CustomerSerializer, TestSerializer
from django.contrib.auth import login
from django.contrib.auth import logout
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from .models import *
from .forms import UserProfileForm, CustomerForm, TestForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


import pdfkit
config = pdfkit.configuration(wkhtmltopdf=r"C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")




class LandingAPI(generics.GenericAPIView):
    """
    LandingAPI class handles the GET request for rendering a landing page.

    This class defines a GET method that renders an HTML template ('labtest/landing.html')
    and returns it as a response to the client.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: An HTTP response containing the rendered HTML content.
    """
    
    def get(self, request):
        context = {}  # Define your context data here if needed
        return render(request, 'labtest/landing.html', context)



def generatePDF(request):
    """
    generatePDF function generates a PDF document from a web page and returns it as a download response.

    This function uses the 'pdfkit' library to convert a web page into a PDF document.
    It then creates an HTTP response containing the PDF content for download.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: An HTTP response containing the generated PDF for download.
    """
    pdf = pdfkit.from_url(request.build_absolute_uri(reverse('download')), False, configuration=config)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="result.pdf"'

    return response




# Create your views here.
def download(request):
    return render(request, 'labtest/download.html')


class RegisterAPI(LoginRequiredMixin, generics.GenericAPIView):
    """
    RegisterAPI class handles user registration.

    This class inherits from LoginRequiredMixin to ensure that only authenticated users can access it.
    It defines both GET and POST methods for displaying the registration form and processing form submissions.

    Attributes:
        serializer_class (class): The serializer class used for registration data.

    Methods:
        get(self, request, *args, **kwargs): Renders the registration form for GET requests.
        post(self, request, *args, **kwargs): Handles form submission and user registration for POST requests.

    Template:
        'labtest/register.html' - The HTML template for the registration form.

    Redirects:
        'staff-list' - Redirects to the staff list page after successful registration.
    """
    
    serializer_class = RegisterSerializer

    # get request (for displaying the registration form)
    def get(self, request, *args, **kwargs):
        form = UserProfileForm()
        context = {'form': form}
        return render(request, 'labtest/register.html', context)  # Render the registration form template

    # post request (for processing form submission)
    def post(self, request, *args, **kwargs):
        form = UserProfileForm(request.POST)

        if form.is_valid():
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()

            # Redirect to the login page after successful registration
            return redirect('staff-list')

        # If the form is not valid, re-render the registration form with errors
        context = {
            'form': form,
        }
        return render(request, 'labtest/register.html', context)




# LoginAPI class handles user login and authentication.

class LoginAPI(KnoxLoginView):
    """
    LoginAPI class provides user authentication and login functionality.

    This class inherits from KnoxLoginView, a view designed for token-based authentication.
    It supports both GET and POST requests for displaying the login form and processing login attempts.

    Attributes:
        permission_classes (tuple): Specifies permissions for accessing this view.
            In this case, it allows any user (permissions.AllowAny).

    Methods:
        get(self, request, *args, **kwargs): Renders the login form for GET requests.
        post(self, request, format=None): Handles user login for POST requests.

    Template:
        'labtest/login.html' - The HTML template for the login form.

    Redirect:
        After a successful login, the user is redirected to the 'dashboard' page with their user information.
    """
    permission_classes = (permissions.AllowAny,)

    def get(self, request, *args, **kwargs):
        return render(request, 'labtest/login.html')

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return render(request, 'labtest/dashboard.html', {'user': user})



# DashboardAPI class handles user dashboard display.

class DashboardAPI(LoginRequiredMixin, generics.GenericAPIView):
    """
    DashboardAPI class provides the user dashboard view.

    This class inherits from LoginRequiredMixin, ensuring that only authenticated users can access it.
    It defines a GET method for rendering the user dashboard page.

    Methods:
        get(self, request): Renders the user dashboard page for authenticated users.

    Template:
        'labtest/dashboard.html' - The HTML template for the user dashboard.

    """
    
    def get(self, request):
        context = {}  # Define your context data here if needed
        return render(request, 'labtest/dashboard.html', context)



# StaffListView class displays a list of staff members with test count.

class StaffListView(LoginRequiredMixin, ListView):
    """
    StaffListView class displays a list of staff members with a count of related tests.

    This class inherits from LoginRequiredMixin, ensuring that only authenticated users can access it.
    It uses the 'UserProfile' model and the 'labtest/stafflist.html' template to render the staff list.

    Attributes:
        model (model): Specifies the model used for retrieving staff members (UserProfile).
        template_name (str): Specifies the HTML template used for rendering the staff list.
        context_object_name (str): Specifies the name of the context variable containing the staff list.

    Methods:
        get_queryset(self): Annotates each staff member with the count of related tests and returns the queryset.
        get_context_data(self, **kwargs): Retrieves and returns the context data for rendering the template.

    """
    model = UserProfile
    template_name = 'labtest/stafflist.html'
    context_object_name = 'staff_list'

    def get_queryset(self):
        # Annotate each staff member with the count of related tests
        queryset = UserProfile.objects.annotate(test_count=models.Count('test'))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



# staff_tests function displays a list of tests associated with a specific staff member.

def staff_tests(request, staff_id):
    """
    staff_tests function retrieves and displays a list of tests associated with a specific staff member.

    Args:
        request (HttpRequest): The HTTP request object.
        staff_id (int): The unique identifier of the staff member.

    Returns:
        HttpResponse: An HTTP response containing the staff member's information and associated tests.

    Raises:
        Http404: If the staff member with the specified ID does not exist.

    Template:
        'labtest/staff_tests.html' - The HTML template for displaying the staff member's tests.

    Context:
        'staff' (UserProfile): The staff member whose tests are being displayed.
        'tests' (QuerySet): The list of tests associated with the staff member.

    """
    staff = get_object_or_404(UserProfile, id=staff_id)
    tests = Test.objects.filter(user=staff)
    
    context = {
        'staff': staff,
        'tests': tests,
    }
    
    return render(request, 'labtest/staff_tests.html', context)




# UserProfileDetailView class provides details and editing functionality for a user profile.

class UserProfileDetailView(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    """
    UserProfileDetailView class allows viewing and updating user profiles.

    This class inherits from LoginRequiredMixin to ensure that only authenticated users can access it.
    It provides views for retrieving, updating, and deleting user profiles.

    Attributes:
        queryset (QuerySet): Specifies the queryset containing all user profiles.
        serializer_class (class): The serializer class used for serializing user profiles.
        template_name (str): Specifies the HTML template used for rendering user profile details.

    HTTP Methods:
        - GET: Retrieves and displays the user profile details.
        - PUT: Allows authenticated users to update their profile information.
        - DELETE: Allows authenticated users to delete their profile.

    Template:
        'labtest/staffdetail.html' - The HTML template for displaying and editing user profile details.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
    template_name = 'labtest/staffdetail.html'  # Specify the custom template



# CreateCustomerView class handles the creation of customer records.

class CreateCustomerView(LoginRequiredMixin, CreateView):
    """
    CreateCustomerView class provides a view for creating customer records.

    This class inherits from LoginRequiredMixin, ensuring that only authenticated users can access it.
    It utilizes the 'Customer' model and 'CustomerForm' to facilitate the creation of new customer records.

    Attributes:
        model (model): Specifies the model used for creating customer records (Customer).
        form_class (class): The form class used for input validation and data entry (CustomerForm).
        template_name (str): Specifies the HTML template for rendering the customer registration form.
        success_url (str): The URL to redirect to after successful record creation.
            Assumes you have a named URL pattern ('create-customer') for this purpose.

    HTTP Methods:
        - GET: Renders the customer registration form.
        - POST: Processes form submissions and creates customer records.

    Template:
        'labtest/customerregform.html' - The HTML template for displaying the customer registration form.
    """
    model = Customer
    form_class = CustomerForm
    template_name = 'labtest/customerregform.html'
    success_url = reverse_lazy('create-customer')  # Assuming you have a named URL for this view



# CustomerListView class displays a list of customer details.

class CustomerListView(LoginRequiredMixin, ListView):
    """
    CustomerListView class provides a view for displaying a list of customer details.

    This class inherits from LoginRequiredMixin, ensuring that only authenticated users can access it.
    It utilizes the 'Customer' model to retrieve and display customer records.

    Attributes:
        model (model): Specifies the model used for retrieving customer records (Customer).
        template_name (str): Specifies the HTML template used for rendering the customer details.
        context_object_name (str): Defines the name of the context variable containing the list of customers.
        paginate_by (int): Sets the number of items displayed per page (you can change this value).

    HTTP Method:
        - GET: Renders the customer details page, displaying a list of customers.

    Template:
        'labtest/customerdetail.html' - The HTML template for displaying the list of customer details.
    """
    model = Customer
    template_name = 'labtest/customerdetail.html'  # Specify the template name
    context_object_name = 'customers'  # Define the context variable name for the customer list
    paginate_by = 10  # Set the number of items per page (you can change this value)




# CustomerDetailView class displays detailed information about a specific customer.

class CustomerDetailView(LoginRequiredMixin, DetailView):
    """
    CustomerDetailView class provides a view for displaying detailed information about a specific customer.

    This class inherits from LoginRequiredMixin, ensuring that only authenticated users can access it.
    It utilizes the 'Customer' model to retrieve and display detailed customer information.

    Attributes:
        model (model): Specifies the model used for retrieving customer records (Customer).
        template_name (str): Specifies the HTML template used for rendering the customer's detailed view.
        context_object_name (str): Defines the name of the context variable containing the customer object.

    HTTP Method:
        - GET: Renders the customer's detailed view, displaying information about the specified customer.

    Template:
        'labtest/customerdetail.html' - The HTML template for displaying the detailed customer view.
    """
    model = Customer
    template_name = 'labtest/customerdetail.html'  # Specify the template name
    context_object_name = 'customer'  # Define the context variable name for the customer object




# CreateTestView class handles the creation of test records.

class CreateTestView(LoginRequiredMixin, CreateView):
    """
    CreateTestView class provides a view for creating test records.

    This class inherits from LoginRequiredMixin, ensuring that only authenticated users can access it.
    It utilizes the 'Test' model and 'TestForm' to facilitate the creation of new test records.

    Attributes:
        model (model): Specifies the model used for creating test records (Test).
        form_class (class): The form class used for input validation and data entry (TestForm).
        template_name (str): Specifies the HTML template for rendering the test creation form.
        success_url (str): The URL to redirect to after successful record creation.

    HTTP Methods:
        - GET: Renders the test creation form.
        - POST: Processes form submissions and creates test records.

    Template:
        'labtest/testform.html' - The HTML template for displaying the test creation form.
    """
    model = Test
    form_class = TestForm
    template_name = 'labtest/testform.html'
    success_url = reverse_lazy('create-test')



# TestListView class displays a list of test records.

class TestListView(LoginRequiredMixin, ListView):
    """
    TestListView class provides a view for displaying a list of test records.

    This class inherits from LoginRequiredMixin, ensuring that only authenticated users can access it.
    It utilizes the 'Test' model to retrieve and display test records.

    Attributes:
        model (model): Specifies the model used for retrieving test records (Test).
        template_name (str): Specifies the HTML template used for rendering the test records.
        context_object_name (str): Defines the name of the context variable containing the list of test records.
        paginate_by (int): Sets the number of items displayed per page (you can change this value).

    HTTP Method:
        - GET: Renders the test records page, displaying a list of test records.

    Template:
        'labtest/testview.html' - The HTML template for displaying the list of test records.
    """
    model = Test
    template_name = 'labtest/testview.html'
    context_object_name = 'test'
    paginate_by = 10




# TestDetailView class displays detailed information about a specific test.

class TestDetailView(LoginRequiredMixin, DetailView):
    """
    TestDetailView class provides a view for displaying detailed information about a specific test.

    This class inherits from LoginRequiredMixin, ensuring that only authenticated users can access it.
    It utilizes the 'Test' model to retrieve and display detailed information about a test record.

    Attributes:
        model (model): Specifies the model used for retrieving test records (Test).
        template_name (str): Specifies the HTML template for rendering the detailed test view.
        context_object_name (str): Defines the name of the context variable containing the test object.

    HTTP Method:
        - GET: Renders the detailed test view, displaying information about the specified test.

    Template:
        'labtest/download.html' - The HTML template for displaying the detailed test view.

    Context Data Processing:
        The 'get_context_data' method wraps the 'tes' object in a list to make it iterable in the template.
    """
    model = Test
    template_name = 'labtest/download.html'  # Specify the template name
    context_object_name = 'tes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Wrap the 'tes' object in a list to make it iterable
        context['tes'] = [context['tes']]
        
        # Now, 'tes' is iterable in your template
        return context




# user_logout function handles user logout and redirects to the landing page.

def user_logout(request):
    """
    user_logout function logs out the current user and redirects to the landing page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponseRedirect: Redirects the user to the landing page after successful logout.
    """
    logout(request)
    return redirect(reverse('landing'))

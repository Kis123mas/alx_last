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
    
    def get(self, request):
        context = {}  # Define your context data here if needed
        return render(request, 'labtest/landing.html', context)

def generatePDF(request):
    pdf = pdfkit.from_url(request.build_absolute_uri(reverse('download')), False, configuration=config)
    response = HttpResponse(pdf, content_type= 'application/pdf')
    response['Content-Disposition'] = 'attachment; filename="result.pdf"'

    return response


# Create your views here.
def download(request):
    return render(request, 'labtest/download.html')


class RegisterAPI(LoginRequiredMixin, generics.GenericAPIView):

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



# user login 
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, *args, **kwargs):

        return render(request, 'labtest/login.html')

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return render(request, 'labtest/dashboard.html', {'user': user})


class DashboardAPI(LoginRequiredMixin, generics.GenericAPIView):
    
    def get(self, request):
        context = {}  # Define your context data here if needed
        return render(request, 'labtest/dashboard.html', context)


class StaffListView(LoginRequiredMixin, ListView):
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

def staff_tests(request, staff_id):
    staff = get_object_or_404(UserProfile, id=staff_id)
    tests = Test.objects.filter(user=staff)
    
    context = {
        'staff': staff,
        'tests': tests,
    }
    
    return render(request, 'labtest/staff_tests.html', context)

class UserProfileDetailView(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
    template_name = 'labtest/staffdetail.html'  # Specify the custom template


class CreateCustomerView(LoginRequiredMixin, CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'labtest/customerregform.html'
    success_url = reverse_lazy('create-customer')  # Assuming you have a named URL for this view


# customer details and view
class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    template_name = 'labtest/customerdetail.html'  # Specify the template name
    context_object_name = 'customers'  # Define the context variable name for the customer list
    paginate_by = 10  # Set the number of items per page (you can change this value)

class CustomerDetailView(LoginRequiredMixin, DetailView):
    model = Customer
    template_name = 'labtest/customerdetail.html'  # Specify the template name
    context_object_name = 'customer'  # Define the context variable name for the customer object



class CreateTestView(LoginRequiredMixin, CreateView):
    model = Test
    form_class = TestForm
    template_name = 'labtest/testform.html'
    success_url = reverse_lazy('create-test')

class TestListView(LoginRequiredMixin, ListView):
    model = Test
    template_name = 'labtest/testview.html'
    context_object_name = 'test'
    paginate_by = 10

class TestDetailView(LoginRequiredMixin, DetailView):
    model = Test
    template_name = 'labtest/download.html'  # Specify the template name
    context_object_name = 'tes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Wrap the 'tes' object in a list to make it iterable
        context['tes'] = [context['tes']]
        
        # Now, 'tes' is iterable in your template
        return context



def user_logout(request):
    logout(request)
    return redirect(reverse('landing'))
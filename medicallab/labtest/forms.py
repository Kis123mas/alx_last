from django import forms
from django.forms import ModelForm
from .models import UserProfile, Customer, Test

class UserProfileForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({
            'required':'',
            'name': 'name',
            'type':'text',
            'class':'form-control',
            'placeholder':'Your Name',
        })
        self.fields["email"].widget.attrs.update({
            'required':'',
            'name': 'email',
            'type':'text',
            'class':'form-control',
            'placeholder':'Your Email-Address',
        })
        self.fields["password"].widget.attrs.update({
            'required':'',
            'type':'text',
            'name':'password',
            'class':'form-control',
            'placeholder':'Enter your password',
        })
    class Meta:
        model = UserProfile
        exclude = ['is_active', 'is_staff']

class CustomerForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["staff_name"].widget.attrs.update({
            'required':'',
            'name': 'staff_name',
            'type':'text',
            'class':'form-control',
        })
        self.fields["firstname"].widget.attrs.update({
            'required':'',
            'name': 'firstname',
            'type':'text',
            'class':'form-control',
            'placeholder':'Your Firstname',
        })
        self.fields["lastname"].widget.attrs.update({
            'required':'',
            'type':'text',
            'name':'lastname',
            'class':'form-control',
            'placeholder':'Enter lastname',
        })
        self.fields["othernames"].widget.attrs.update({
            'required':'',
            'name': 'othernames',
            'type':'text',
            'class':'form-control',
            'placeholder':'Enter Othernames',
        })
        self.fields["email"].widget.attrs.update({
            'required':'',
            'name': 'email',
            'type':'text',
            'class':'form-control',
            'placeholder':'Your Email-Address',
        })
        self.fields["phone"].widget.attrs.update({
            'required':'',
            'type':'text',
            'name':'phone',
            'class':'form-control',
            'placeholder':'Enter phone number',
        })
        self.fields["sex"].widget.attrs.update({
            'required':'',
            'type':'text',
            'name':'sex',
            'class':'form-control',
            'placeholder':'Enter Sex',
        })
        self.fields["referralsname"].widget.attrs.update({
            'required':'',
            'name': 'referralsname',
            'type':'text',
            'class':'form-control',
            'placeholder':'Enter Referralsname',
        })
    class Meta:
        model = Customer
        exclude = ['is_active', 'date']

    

class TestForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["user"].widget.attrs.update({
            'required':'',
            'name': 'user',
            'type':'text',
            'class':'form-control',
        })
        self.fields["customername"].widget.attrs.update({
            'required':'',
            'name': 'customername',
            'type':'text',
            'class':'form-control',
            'placeholder':'Enter Customer Name',
        })
        self.fields["typeoftest"].widget.attrs.update({
            'required':'',
            'type':'text',
            'name':'typeoftest',
            'class':'form-control',
            'placeholder':'Enter Type Of Test',
        })
        self.fields["clinicaldiagnosis"].widget.attrs.update({
            'required':'',
            'name': 'clinicaldiagnosis',
            'type':'text',
            'class':'form-control',
            'placeholder':'Enter Clinical Diagnosis',
        })
        self.fields["natureofspecimen"].widget.attrs.update({
            'required':'',
            'name': 'natureofspecimen',
            'type':'text',
            'class':'form-control',
            'placeholder':'Your Nature Of Specimen',
        })
        self.fields["typesofinvestigation"].widget.attrs.update({
            'required':'',
            'type':'text',
            'name':'typesofinvestigation',
            'class':'form-control',
            'placeholder':'Enter Type Of Investigation',
        })
        self.fields["bloodgroup"].widget.attrs.update({
            'required':'',
            'type':'text',
            'name':'bloodgroup',
            'class':'form-control',
            'placeholder':'Enter Bloodgroup',
        })
        self.fields["genotype"].widget.attrs.update({
            'required':'',
            'name': 'genotype',
            'type':'text',
            'class':'form-control',
            'placeholder':'Enter Genotype',
        })
        self.fields["rvs"].widget.attrs.update({
            'required':'',
            'name': 'rvs',
            'type':'text',
            'class':'form-control',
            'placeholder':'Enter RVS',
        })
    class Meta:
        model = Test
        exclude = ['date']

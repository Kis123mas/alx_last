from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager



# Create your models here.
class UserProfileManager(BaseUserManager):
    """helps django to work with our custom user model"""

    def create_user(self, email, name, password=None):
        """ creates a new user profile object"""
        if not email:
            raise ValueError('Users must have an email address.')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """ create  and save a new superuser with given detail"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user



class UserProfile(AbstractBaseUser, PermissionsMixin):
    """respresent  a user profile inside our system"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """used to get a usetr full name"""

        return self.name

    def get_short_name(self):
        """used to get a user short name"""

        return self.name

    def __str__(self):
        """ uses this to convert the obkect to a string"""

        return self.name




# customer table
class Customer(models.Model):
    SEX = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Prefer Not To Say', 'Prefer Not To Say')
    )
    staff_name = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=200, null=True, blank=True, db_index=True)
    lastname = models.CharField(max_length=200, null=True, blank=True, db_index=True)
    othernames = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=255, unique=True, null=True, db_index=True)
    phone = models.IntegerField(null=True)
    sex = models.CharField(max_length=200, null=True, choices=SEX, blank=True)
    referralsname = models.CharField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(default=datetime.now, editable=False)


    
    def __str__(self):
        return self.firstname +' '+ self.lastname



# test table
class Test(models.Model):
    TYPEOFTEST = (
        ('Blood Count Tests', 'Blood Count Tests'),
        ('Genetic Testing', 'Genetic Testing'),
        ('Kidney Tests', 'Kidney Tests'),
        ('Laboratory Tests', 'Laboratory Tests'),
        ('Prenatal Testing', 'Prenatal Testing'),
        ('Thyroid Tests', 'Thyroid Tests'),
        ('Urinalysis', 'Urinalysis')
    )
    GENOTYPE = (
        ('AA', 'AA'),
        ('AS', 'AS'),
        ('SS', 'SS')
    )
    BLOODGROUP = (
        ('A', 'A'),
        ('B', 'B'),
        ('AB', 'AB'),
        ('O', 'O')
    )
    user = models.ForeignKey(UserProfile, null=True, on_delete= models.SET_NULL)
    customername = models.ForeignKey(Customer, on_delete=models.CASCADE)
    typeoftest = models.CharField(max_length=200, null=True, choices=TYPEOFTEST, blank=True)
    clinicaldiagnosis = models.CharField(max_length=200, null=True, blank=True)
    natureofspecimen = models.CharField(max_length=200, null=True, blank=True)
    typesofinvestigation = models.CharField(max_length=200, null=True, blank=True)
    bloodgroup = models.CharField(max_length=200, null=True, choices=BLOODGROUP, blank=True)
    genotype = models.CharField(max_length=200, null=True, choices=GENOTYPE, blank=True)
    rvs = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateTimeField(default=datetime.now, editable=False)

    def __str__(self):
        return str(self.user) +' | '+ str(self.customername) + ' | ' + str(self.typeoftest)
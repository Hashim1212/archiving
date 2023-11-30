from django.db import models

# Import AbstractUser
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    GENDER_TYPE = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

    name = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    phone_num = models.CharField(max_length=11, null=True, blank=True)
    avatar = models.ImageField(default="avatar.svg", null=True, blank=True)
    employee_num = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=50, choices=GENDER_TYPE, null=True, blank=True)
    nationality = models.CharField(max_length=150, null=True, blank=True)
    occupation = models.CharField(max_length=150, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.username

class Attainment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    year_attended = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user

class Memorandum(models.Model):
    memo_no = models.CharField(max_length=10, primary_key=True)
    memo_date = models.DateField(null=True, blank=True)
    memo_file = models.FileField(null=True, blank=True)
    memo_subject = models.CharField(max_length=255, null=True, blank=True)
    memo_content = models.TextField(null=True, blank=True)
    memo_to = models.CharField(max_length=100, null=True, blank=True)
    memo_to_pos = models.CharField(max_length=100, null=True, blank=True)
    memo_thru = models.CharField(max_length=100, null=True, blank=True)
    memo_thru_pos = models.CharField(max_length=100, null=True, blank=True)
    memo_from = models.CharField(max_length=100, null=True, blank=True)
    memo_from_pos = models.CharField(max_length=100, null=True, blank=True)
    memo_recomm_by = models.CharField(max_length=100, null=True, blank=True)
    memo_approved_by = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, null=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.CharField(max_length=100, null=True, blank=True)
    is_backup = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.memo_no

class SpecialOrder(models.Model):
    so_no = models.CharField(max_length=10, primary_key=True)
    so_date = models.DateField(null=True, blank=True)
    so_file = models.FileField(null=True, blank=True)
    so_subject =  models.CharField(max_length=255, null=True, blank=True)
    so_content = models.TextField(null=True, blank=True)
    so_for = models.CharField(max_length=100, null=True, blank=True)
    so_signedby = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, null=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.CharField(max_length=100, null=True, blank=True)
    is_backup = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.so_no

class CommLetter(models.Model):
    letter_no = models.CharField(max_length=10, primary_key=True)
    letter_file = models.FileField(null=True, blank=True)
    letter_subject = models.CharField(max_length=255, null=True, blank=True)
    letter_to = models.CharField(max_length=100, null=True, blank=True)
    letter_from = models.CharField(max_length=100, null=True, blank=True)
    letter_received_by = models.CharField(max_length=100, null=True, blank=True)
    letter_received_date = models.DateField(null=True, blank=True)
    letter_noted_by = models.CharField(max_length=100, null=True, blank=True)
    letter_recom_approval = models.CharField(max_length=100, null=True, blank=True)
    letter_approved_by = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, null=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.CharField(max_length=100, null=True, blank=True)
    is_backup = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.letter_no

class Moau(models.Model):
    TYPE = (
        ('MOA', 'Memorandum of Agreement'),
        ('MOU', 'Memorandum of Understanding'),
        ('MOC', 'Memorandum of Commitment')
    )

    moau_no = models.CharField(max_length=10, primary_key=True)
    moau_file = models.FileField(null=True, blank=True)
    moau_title = models.CharField(max_length=255, null=True, blank=True)
    moau_type = models.CharField(max_length=100, choices=TYPE, null=True, blank=True)
    moau_objective = models.TextField(null=True, blank=True)
    moau_approve_date = models.DateField(null=True, blank=True)
    moau_notarized_by = models.CharField(max_length=100, null=True, blank=True)
    moau_notarized_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, null=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.CharField(max_length=100, null=True, blank=True)
    is_backup = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return self.moau_no


class MoauParties(models.Model):
    moau = models.ForeignKey(Moau, on_delete=models.CASCADE)
    agency = models.CharField(max_length=100, null=True, blank=True)
    represented_by = models.CharField(max_length=100, null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    referred_to_as = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, null=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        ordering = ['created_at']
        
    def __str__(self):
        return self.moau

class MoauSignatories(models.Model):
    moau = models.ForeignKey(Moau, on_delete=models.CASCADE)
    signed_by = models.CharField(max_length=100, null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)
    agency = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, null=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        ordering = ['created_at']
        
    def __str__(self):
        return self.moau


class Event(models.Model):
    event_name = models.CharField(max_length=100, null=True, blank=True)
    event_agenda = models.CharField(max_length=100, null=True, blank=True)
    event_date = models.DateField(null=True, blank=True)
    event_venue = models.CharField(max_length=100, null=True, blank=True)
    no_participants = models.CharField(max_length=100, null=True, blank=True)
    impl_agency = models.CharField(max_length=100, null=True, blank=True)
    attendance_file = models.FileField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, null=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.CharField(max_length=100, null=True, blank=True)
    is_backup = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return self.event_name


class Agency(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Agency'
        verbose_name_plural = 'Agencies'

    def __str__(self):
        return self.name


class EventAgencies(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    agency_id = models.CharField(max_length=100, null=True, blank=True)
    agency_role = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, null=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return self.event
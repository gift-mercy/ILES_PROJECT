from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLES = [
        ('student',"Student"),
        ('workplace','Workplace Supervisor'),
        ('academic','Academic Supervisor'),
        ('admin', 'Administrator')
        ]
    
    role = models.CharField(
        max_length=20, 
        choices=ROLES, 
        default='student'
        )
    department = models.CharField(
        max_length=150, 
        blank=True, 
        null=True
        )
    staff_number = models.CharField(
        max_length=20, 
        blank=True, 
        null=True, 
        unique=True
        )
    student_number = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        unique=True
        )



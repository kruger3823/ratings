from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class review(models.Model):
    instructor = models.CharField(max_length=100)
    assignedTeacherId = models.PositiveIntegerField(null=True)
    assignedSubId = models.CharField(max_length=100, choices=(
    ('1', 'Maths'), ('2', 'Chemistry'), ('3', 'Physics'), ('4', 'Biology'), ('4', 'Hindi')))
    ratings = models.IntegerField()
    comments = models.TextField(verbose_name="CLEANLINESS")
    comments1 = models.TextField(verbose_name="PARTIALITY")
    comments2 = models.TextField(verbose_name="PUNCTUALITY")
    comments3 = models.TextField(verbose_name="SECURITY")
    comments4 = models.TextField(verbose_name="TRANSPARENCY")
    comments5 = models.TextField(verbose_name="FEE")
    comments6 = models.TextField(verbose_name="EXTRACURICULUMS")
    course = models.CharField(max_length=100)

    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.instructor

    def get_absolute_url(self):
            return reverse('review-detail', kwargs={'pk': self.pk})




class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    sub = models.CharField(max_length=100, choices=(
        ('Maths', 'Maths'), ('Chemistry', 'Chemistry'), ('Physics', 'Physics'), ('Biology', 'Biology'), ('Hindi', 'Hindi')))
    #address = models.IntegerField(max_length=40)
    time = models.IntegerField(max_length=40 ,choices=(
        (1,1),(2,2),(3,3),(4,4),(5,5)))
    punctual = models.IntegerField(max_length=40,choices=(
        (1,1),(2,2),(3,3),(4,4),(5,5)))
    loud = models.IntegerField(max_length=40,choices=(
        (1,1),(2,2),(3,3),(4,4),(5,5)))
    partiality = models.IntegerField(max_length=40,choices=(
        (1,1),(2,2),(3,3),(4,4),(5,5)))
    clarity = models.IntegerField(max_length=40,choices=(
        (1,1),(2,2),(3,3),(4,4),(5,5)))
    mobile = models.IntegerField(null=True,verbose_name='Ratings',choices=(
        (1,1),(2,2),(3,3),(4,4),(5,5)))
    symptoms = models.IntegerField(max_length=100, null=False,choices=(
        (1,1),(2,2),(3,3),(4,4),(5,5)))
    assignedDoctorId = models.PositiveIntegerField(null=True)
    admitDate = models.DateField(auto_now=True)
    status = models.BooleanField(default=False)







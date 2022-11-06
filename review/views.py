from django.forms import ModelChoiceField
from django.shortcuts import render,  get_object_or_404
from django.http import HttpResponse
from . import forms, models
from django import forms

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
    )
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import PatientForm
from .models import review

# Create your views here.

@login_required
def home(request):
    context = {
        'posts': review.objects.all()
    }
    return render(request, 'review/home.html', context)

class PostListView(ListView):
    model = review
    template_name = 'review/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3

class PostDetailView(DetailView):
    model = review

class PostCreateView( LoginRequiredMixin, CreateView):

    model = review
    fields = ['instructor','ratings', 'comments', 'comments1', 'comments2', 'comments3', 'comments4', 'comments5', 'comments6', 'course']

    def form_valid(self, form):
            form.instance.author = self.request.user
            return super().form_valid(form)

class UserPostListView(ListView):

    model = review
    template_name = 'review/user_reviews.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return review.objects.filter(author=user).order_by('-date_posted')

class PostUpdateView( LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    assigned = User.objects.all().filter(groups__name='TEACHER')
    print(assigned)

    model = review
    fields = ['instructor','ratings', 'comments', 'comments1', 'comments2', 'comments3', 'comments4', 'comments5', 'comments6', 'course']

    def form_valid(self, form):
            form.instance.author = self.request.user
            return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = review
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


@login_required
def about(request):
     return render(request, 'review/about.html', {'title': 'About'})




def apply(request):

    patientForm=PatientForm()
    mydict={'patientForm':patientForm}
    if request.method=='POST':
        print("hi")
        patientForm=PatientForm(request.POST,request.FILES)
        if patientForm.is_valid():
            print("hi")
            patient=patientForm.save(commit=False)
            patient.assignedDoctorId=request.POST.get('assignedDoctorId')
            fg = User.objects.get(id=request.POST.get('assignedDoctorId'))
            patient.user=fg
            patient.save()

        return render(request,'review/student.html',context=mydict)
    return render(request,'patientsignup.html',context=mydict)



def view(request):
    patients=models.Patient.objects.all().filter(status=False,assignedDoctorId=request.user.id)
    hint = models.Patient.objects.all().filter(user__id=request.user.id)
    print(hint)
    ratlist=[]
    for i in hint:
        ratlist.append(i.mobile)
    print(ratlist)
    c=0
    for j in ratlist:
        c=c+j
        d=c/(len(ratlist)*10)
        if d<0.5:
            a="weak ratings"
        else:
            a="strong ratings"
    print(d)


    return render(request,'view-feedback.html',{'patients':patients,'a':a},)


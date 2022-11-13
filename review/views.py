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

    ratlist = []
    ratlist1 = []
    ratlist2 = []
    ratlist3 = []
    ratlist4 = []
    ratlist5 = []
    ratlist6 = []

    for i in hint:
        ratlist.append(i.mobile)
    print(ratlist)

    for i in hint:
        ratlist1.append(i.punctual)
    print(ratlist)
    for i in hint:
        ratlist2.append(i.loud)
    print(ratlist)
    for i in hint:
        ratlist3.append(i.partiality)
    print(ratlist)
    for i in hint:
        ratlist4.append(i.clarity)
    print(ratlist)
    for i in hint:
        ratlist5.append(i.symptoms)
    print(ratlist)
    for i in hint:
        ratlist6.append(i.time)
    print(ratlist)

    a=0
    for j in ratlist:
        a=a+j
        print(a)
    if (a/(len(ratlist)*10))*100 <50:
        d=(a / (len(ratlist) * 10))*100
        a=d
    else:
        d = (a / (len(ratlist) * 10)) * 100
        a=d
    print(a)

    b=0
    for j in ratlist1:
        b=b+j
    if (b / (len(ratlist) * 10)) * 100 < 50:
            d = (b / (len(ratlist) * 10)) * 100
            b = d
    else:
            d = (b / (len(ratlist) * 10)) * 100
            b = d
    l=0
    for j in ratlist2:
        l=l+j
    if (l / (len(ratlist) * 10)) * 100 < 50:
            d = (l / (len(ratlist) * 10)) * 100
            l = d
    else:
            d = (l / (len(ratlist) * 10)) * 100
            l = d
    e=0
    for j in ratlist3:
        e=e+j
    if (e/(len(ratlist)*10))*100 <50:
        d=(e / (len(ratlist) * 10))*100
        e=d
    else:
        d = (e / (len(ratlist) * 10)) * 100
        e=d

    f=0
    for j in ratlist4:
        f=f+j
    if (f/(len(ratlist)*10))*100 <50:
        d=(f / (len(ratlist) * 10))*100
        f=d
    else:
        d = (f / (len(ratlist) * 10)) * 100
        f=d
    g=0
    for j in ratlist5:
        g=g+j
    if (g/(len(ratlist)*10))*100 <50:
        d=(g / (len(ratlist) * 10))*100
        g=d
    else:
        d = (g / (len(ratlist) * 10)) * 100
        g=d
    print(d)
    h = 0
    for j in ratlist6:
        h = h + j
    if (h/(len(ratlist)*10))*100 <50:
        d=(h / (len(ratlist) * 10))*100
        h=d
    else:
        d = (h / (len(ratlist) * 10)) * 100
        h=d



    return render(request,'view-feedback.html',{'patients':patients,'a':a,'b':b,'l':l,'e':e,'f':f,'g':g,'h':h},)


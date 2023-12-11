from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from . forms import StudentForm, RegiserForm
from . models import Student
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

# s@login_required
class GetAndPostData(View):
    def get(self, request):
        if request.user.is_superuser:
            sdata = Student.objects.all()
        else:
            sdata = Student.objects.filter(user=request.user)
        form = StudentForm()
        context = {
            'sdata': sdata,
            'form': form 
        }
        return render(request, 'sform.html', context)

    def post(self, request):
        form = StudentForm(request.POST or None)
        if form.is_valid():
            usr = form.save(commit=False)
            usr.user = request.user
            usr.save()
            return redirect('/')

# @login_required        
class UpdateData(View):
    def get(self, request, id):
        if request.user.is_superuser:
            sdata = get_object_or_404(Student, id=id)
        else:
            sdata = get_object_or_404(Student, id=id, user=request.user)
        form = StudentForm(instance=sdata)
        return render(request, 'uform.html', {'form':form})
    
    def post(self, request, id):
        if request.user.is_superuser:
            sdata = get_object_or_404(Student, id=id)
        else:
            sdata = get_object_or_404(Student, id=id, user=request.user)
        form = StudentForm(request.POST or None, instance=sdata)
        if form.is_valid():
            form.save()
            return redirect('/')
# @login_required        
class DeleteData(View):
    def get(self, request, id):
        if request.user.is_superuser:
            sdata = get_object_or_404(Student, id=id)
        else:
            sdata = get_object_or_404(Student, id=id, user=request.user)
        sdata.delete()
        return redirect('/')
    
def signup(request):
    if request.method == 'POST':
        form = RegiserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = RegiserForm()
    return render(request, 'signform.html', {'form':form})
        
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'lform.html', {'form':form})
    
def logout_user(request):
    logout(request)
    return redirect('/login')
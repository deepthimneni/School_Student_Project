from django.shortcuts import render, redirect
from students.forms import StudentForm
from students.models import Student
# Create your views here.
def stud(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = StudentForm()
    return render(request,'create.html',{'form':form})
def show(request):
    students = Student.objects.all()
    return render(request,"show.html",{'students':students})
def edit(request, id):
    student = Student.objects.get(id=id)
    return render(request,'edit.html', {'student':student})
def update(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(request.POST, instance = student)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'student': student})
def destroy(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect("/show")
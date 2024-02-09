from django.shortcuts import render , HttpResponseRedirect
from .forms import StudentRegistration
from .models import Student

# Create your views here.
# this function will add new item and show all items
def add_show(request):
    if request.method =='POST':
      fm =(StudentRegistration(request.POST))
      if fm.is_valid():
        fm.save()
    else:
       fm =StudentRegistration() 
    stu = Student.objects.all()
    print(stu)
    return render(request,'enroll/addandshow.html',{"form":fm,"st":stu})


# this function for update /edit the data
def update_data(request,id):
    if request.method == 'POST':
       pi = Student.objects.get(pk=id)
       fm = StudentRegistration(request.POST,instance=pi)
       if fm.is_valid():
          fm.save()
    else:
          pi = Student.objects.get(pk=id)
          fm = StudentRegistration(instance=pi)
    return render(request,'enroll/updatestd.html',{"form":fm})



# this function for delete the data
def delete_data(request,id):
   if request.method == 'POST':
      pi = Student.objects.get(pk=id)
      pi.delete()
      return HttpResponseRedirect('/')


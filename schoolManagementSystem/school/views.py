from django.shortcuts import render,redirect
from .forms import Register
from .models import*
from django.contrib.auth import authenticate,login,logout
from .form import TeacherForm

def home(request):
     return render(request, 'hospital/home.html', {})

def about(request):
     return render(request, 'hospital/about.html', {})

def contact(request):
     return render(request, 'hospital/contact.html', {})



def register(request):
	if request.method=="POST":
		form = Register(request.POST)

		if form.is_valid():
			print("HELLO")
			print(form)
			form.save()
			return redirect('login')
	else:
		form = Register()
	return render(request,'hospital/register.html',{'form':form})


def Login(request):
	error = ""
	if request.method=='POST':
		u = request.POST['uname']
		p = request.POST['pwd']
		user = authenticate(username=u,password=p)
		try:
			if user.is_staff:
				login(request,user)
				error = "yes"
			else:
				error = "no"
		except:
			error = "no"
	d = {'error':error}
	return render(request,'hospital/login.html',d)


def Add_Teacher(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')

    if request.method=="POST":
        n = request.POST['name']
        c = request.POST['contact']
        s = request.POST['specialization']
        q = request.POST['specialization']
        t = request.POST['specialization']
        
        try:
            Teacher.objects.create(name=n,contact=c,specialization=s,
            qualification=q,
            teachingLevel=t
            )
            error="no"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'hospital/add_teacher.html',d)


def Update_Teacher(request,pid):


      
    teacher = Teacher.objects.get(id=pid)  
  

    if request.method=="POST":
        teacher.name = request.POST['name']
        teacher.contact = request.POST['contact']
        teacher.specialization = request.POST['specialization']
        teacher.qualification= request.POST['specialization']
        teacher.teachingLevel = request.POST['specialization']


        teacher.save()
        return redirect('view_teacher')

    return render(request,'hospital/update_teacher.html')
        

   



def View_Teacher(request):
    if not request.user.is_staff:
        return redirect('login')
        
    doc = Teacher.objects.all()
    d = {'doc':doc}
    return render(request,'hospital/view_teacher.html',d)


def Delete_Teacher(request,pid):
    if not request.user.is_staff:
        return redirect('login')
        
    teacher = Teacher.objects.get(id=pid)
    teacher.delete()
    return redirect('view_teacher')

def Add_Student(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')

    if request.method=="POST":
        n = request.POST['name']
        c = request.POST['contact']
        a = request.POST['age']
        g = request.POST['gender']
        ad = request.POST['address']
        sc = request.POST['studyClass']

        
        try:
            Student.objects.create(name=n,contact=c,age=a,gender=g,address=ad,studyClass=sc)
            error="no"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'hospital/add_student.html',d)

    
def View_Student(request):
    if not request.user.is_staff:
        return redirect('login')
        
    pat = Student.objects.all()
    d = {'pat':pat}
    return render(request,'hospital/view_student.html',d)


def Update_Student(request,pid):


      
    student = Student.objects.get(id=pid)

      
  

    if request.method=="POST":
        student.name = request.POST['name']
        student.gender = request.POST['gender']
        student.age = request.POST['age']
        student.contact= request.POST['contact']
        student.address = request.POST['address']
        student.studyClass = request.POST['studyClass']


        student.save()
        return redirect('view_student')

    return render(request,'hospital/update_student.html')
        

   



def Delete_Student(request,pid):
    if not request.user.is_staff:
        return redirect('login')
        
    patient = Student.objects.get(id=pid)
    patient.delete()
    return redirect('view_student')

def Feedback(request):
    return render(request,'hospital/feedback.html',{})

def contact(request):
     return render(request, 'hospital/contact.html', {})
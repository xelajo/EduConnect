from django.shortcuts import render,redirect,get_object_or_404
from.forms import TeacherForm,Studentform,parentform,Loginform,Notificationform,Noteuploadform,notificationparentform
from.models import Teacher,Student,Parent,Login,Notification,Noteupload,notificationparent
from django.db.models import Q

# Create your views here.
def UserPage(request):
    return render(request,'index.html')
def teacherhome(request):
    return render(request,'teacherhome.html')
def parenthome(request):
    return render(request,'parenthome.html')
def studenthome(request):
    return render(request,'studenthome.html')
def AdminPage(request):
    return render(request,'adminindex.html')
def LoginPage(request,usertype):
    if usertype=='teacher':
        if request.method=='POST':
            form=Loginform(request.POST)
            if form.is_valid():
                email=form.cleaned_data['email']
                password=form.cleaned_data['password']
                try:
                    user=Teacher.objects.filter(email=email,password=password).first()
                    request.session['teacher_id']=user.id
                    return redirect('teacherhome')
                except Teacher.DoesNotExist:
                    form.add_error(None,"invalid email or password")
        else:
            form=Loginform()        
        return render(request,'loginindex.html',{'form':form})

    if usertype=='parent':
        if request.method=='POST':
            form=Loginform(request.POST)
            if form.is_valid():
                email=form.cleaned_data['email']
                password=form.cleaned_data['password']
                try:
                    user=Parent.objects.filter(email=email,password=password).first()
                    request.session['parent_id']=user.id
                    return redirect('parenthome')
                except Parent.DoesNotExist:
                    form.add_error(None,"invalid email or password")
        else:
            form=Loginform()        
        return render(request,'loginindex.html',{'form':form})

    if usertype=='student':
        if request.method=='POST':
            form=Loginform(request.POST)
            if form.is_valid():
                email=form.cleaned_data['email']
                password=form.cleaned_data['password']
                try:
                    user=Student.objects.filter(email=email,password=password).first()
                    request.session['student_id']=user.id
                    return redirect('studenthome')
                except Student.DoesNotExist:
                    form.add_error(None,"invalid email or password")
        else:
            form=Loginform()        
        return render(request,'loginindex.html',{'form':form})
       
def Teachreg(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Teachreg')
    else:
        form = TeacherForm()
    return render(request,'teachreg.html',{'form':form})
def Studreg (request):
    if request.method=='POST':
        form = Studentform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Studreg')
    else:
        form = Studentform()
    return render(request,'studreg.html',{'form':form})
def Parentreg (request):
    if request.method=='POST':
        form = parentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Parentreg')
    else:
        form = parentform()
    return render(request,'parentreg.html',{'form':form})
def teacheradminview(request):
    book=Teacher.objects.all()
    return render(request,'teacheradminview.html',{'book':book})
def Studentadminview(request):
    book=Student.objects.all()
    return render(request,'studentadminview.html',{'book':book})
def parentadminview(request):
    book=Parent.objects.all()
    return render(request,'parentadminview.html',{'book':book})
def teacherprofile(request):
    id=request.session['user_id']
    instance=get_object_or_404(Teacher,pk=id)
    form=TeacherForm(request.POST or None,instance=instance)
    if form.is_valid():
        form.save()
        return redirect('teacherhome')
    return render(request,'teacherprofile.html',{'form':form})
def parentprofile(request):
    id=request.session['user_id']
    instance=get_object_or_404(Parent,pk=id)
    form=parentform(request.POST or None,instance=instance)
    if form.is_valid():
        form.save()
        return redirect('parenthome')
    return render(request,'parentprofile.html',{'form':form})
def studentprofile(request):
    id=request.session['user_id']
    instance=get_object_or_404(Student,pk=id)
    form=Studentform(request.POST or None,instance=instance)
    if form.is_valid():
        form.save()
        return redirect('studenthome')
    return render(request,'studentprofile.html',{'form':form})
def notification (request):
    i=request.session.get('teacher_id')
    n=get_object_or_404(Teacher,pk=i)
    if request.method=='POST':
        form = Notificationform(request.POST,request.FILES)
        if form.is_valid():
            u=form.save(commit=False)
            u.teacherid=n
            u.save()
            return redirect('teacherhome')
    else:
        form = Notificationform()
    return render(request,'notification.html',{'form':form})
def teachernotificationview(request):
    i=request.session.get('teacher_id')
    n=get_object_or_404(Teacher,pk=i)
    datas=Notification.objects.filter(teacherid=n)
    return render(request,'teachernotificationview.html',{'datas':datas})
def notificationdeletedata(request,pk):
    instance=get_object_or_404(Notification,notification_id=pk)
    instance.delete()
    return redirect('teacherhome')
    
def notificationeditdata(request,pk):
    instance=get_object_or_404(Notification,notification_id=pk)
    form = Notificationform(request.POST or None,instance=instance)
    if form.is_valid():
        form.save()
        return redirect('teacherhome')
    return render(request,'teachernotificationedit.html',{'form':form})
def studentnotificationview(request):
    i=request.session.get('student_id')
    n=get_object_or_404(Student,pk=i)
    datas=Notification.objects.filter(semester = n.semester,department = n.department)
    return render(request,'studentnotificationview.html',{'datas':datas})
def noteupload (request):
    i=request.session.get('teacher_id')
    n=get_object_or_404(Teacher,pk=i)
    if request.method=='POST':
        form = Noteuploadform(request.POST,request.FILES)
        if form.is_valid():
            u=form.save(commit=False)
            u.teacherid=n
            u.save()
            return redirect('teacherhome')
    else:
        form =Noteuploadform ()
    return render(request,'teachernoteupload.html',{'form':form})
def teachernoteview(request):
    i=request.session.get('teacher_id')
    n=get_object_or_404(Teacher,pk=i)
    datas=Noteupload.objects.filter(teacherid=n)
    return render(request,'teachernoteview.html',{'datas':datas})
def notedeletedata(request,pk):
    instance=get_object_or_404(Noteupload,noteupload_id=pk)
    instance.delete()
    return redirect('teachernoteview')
def noteditdata(request,pk):
    instance=get_object_or_404(Noteupload,noteupload_id=pk)
    form = Noteuploadform(request.POST or None,instance=instance)
    if form.is_valid():
        form.save()
        return redirect('teachernoteview')
    return render(request,'teachernoteedit.html',{'form':form})
def studentnoteview(request):
    data=request.GET.get("query")
    i=request.session.get('student_id')
    n=get_object_or_404(Student,pk=i)
    b=None
    if data:
        b=Noteupload.objects.filter(
            Q(subject__icontains=data)|Q(topic__icontains=data))




    
    datas=Noteupload.objects.filter(semester = n.semester,department = n.department)
    return render(request,'studentnoteview.html',{'data':data,'b':b})
def notificationparent(request):
    if request.method == 'POST':
        form = notificationparentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Teachreg')
    else:
        form = notificationparentform()
    return render(request,'notificationparent.html',{'form':form})
def parentstudentview(request):
    data=request.GET.get("query")
    i=request.session.get('teacher_id')
    n=get_object_or_404(Teacher,pk=i)
    b=None
    if data:
        b=Student.objects.filter(
            Q(admno__icontains=data))




    
    # datas=Noteupload.objects.filter(semester = n.semester,department = n.department)
    return render(request,'notificationstudentsearch.html',{'data':data,'b':b})


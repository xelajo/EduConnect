from django import forms
from .models import Teacher,Student,Parent,Login,Notification,Noteupload,notificationparent
class TeacherForm(forms.ModelForm):
    ge=(('male','male')
    ,('female','female'),
    ('others','others'),)
    gender=forms.ChoiceField(choices=ge,widget=forms.RadioSelect())
    
    class Meta:
        model=Teacher
        fields=['photo','name','gender','age','qualification','experience','contactno','email','password']
class Studentform(forms.ModelForm):
    ge=(('male','male')
    ,('female','female'),
    ('others','others'),)
    gender=forms.ChoiceField(choices=ge,widget=forms.RadioSelect())
    dis=(('Thiruvanathapuram ','thiruvanathapuram '),
    ('kollam ','kollam '),
    ('pathanamthitta ','pathanamthitta '),
    ('alappuzha','alappuzha'),
    ('idukki','idukki'),
    ('kottayam','kottayam'),
    ('earnakulam','earnakulam'),
    ('thrissur','thrissur'),
    ('palakkad','palakkad'),
    ('malapuram','malapuram'),
    ('kozhikode','kozhikode'),
    ('wayanad','wayanad'),
    ('kannur','kannur'),
    ('kasargod','kasargod'),)
    district=forms.ChoiceField(choices=dis,widget=forms.Select())
    sem=(('SEM 1 ','SEM 1 ')
    ,('SEM 2 ','SEM 2 '),
    ('SEM 3 ','SEM 3 '),
    ('SEM 4','SEM 4'),)
    semester=forms.ChoiceField(choices=sem,widget=forms.Select())
    dep=(('MBA','MBA')
    ,('MCA','MCA'),
    ('MSC','MSC'),)
    department=forms.ChoiceField(choices=dep,widget=forms.Select())
    class Meta:
        model=Student
        fields=['photo','admno','name','address','district','city','gender','dob','parentname','relationship','contactno','email','password','semester','department']
        widgets={
            'dob':forms.DateInput(attrs={'type':'date'})
            }
class parentform(forms.ModelForm):
    ge=(('male','male')
    ,('female','female'),
    ('others','others'),)
    gender=forms.ChoiceField(choices=ge,widget=forms.RadioSelect())
    class Meta:
        model=Parent
        fields=['parentname','studadmno','contactno','gender','email','password']
class Loginform(forms.ModelForm):
    class Meta:
        model=Login
        fields=['email','password']
class Notificationform(forms.ModelForm):
    sem=(('SEM 1 ','SEM 1 '),
    ('SEM 2 ','SEM 2 '),
    ('SEM 3 ','SEM 3 '),
    ('SEM 4','SEM 4'),)
    semester=forms.ChoiceField(choices=sem,widget=forms.Select())
    dep=(('MBA','MBA')
    ,('MCA','MCA'),
    ('MSC','MSC'),)
    department=forms.ChoiceField(choices=dep,widget=forms.Select())
    class Meta:
        model=Notification
        fields=['department','semester','notification']
class Noteuploadform(forms.ModelForm):
    sem=(('SEM 1 ','SEM 1 '),
    ('SEM 2 ','SEM 2 '),
    ('SEM 3 ','SEM 3 '),
    ('SEM 4','SEM 4'),)
    semester=forms.ChoiceField(choices=sem,widget=forms.Select())
    dep=(('MBA','MBA')
    ,('MCA','MCA'),
    ('MSC','MSC'),)
    department=forms.ChoiceField(choices=dep,widget=forms.Select())
    class Meta:
        model=Noteupload
        fields=['subject','topic','uploadnotes','department','semester']
class notificationparentform(forms.ModelForm):
    class Meta:
        model=notificationparent
        fields=['notification']




from django.urls import path
from .views import UserPage,AdminPage,LoginPage,Teachreg,Studreg,Parentreg,teacheradminview,Studentadminview,parentadminview,teacherhome,parenthome,studenthome,teacherprofile,parentprofile,studentprofile,notification,teachernotificationview,notificationdeletedata,notificationeditdata,studentnotificationview,noteupload,teachernoteview,notedeletedata,noteditdata,studentnoteview,notificationparent,parentstudentview

urlpatterns=[
    path('',UserPage,name='UserPage'),
    path('adminpage/',AdminPage,name='AdminPage'),
    path('loginpage/<str:usertype>/',LoginPage,name='LoginPage'),
    path('Teachreg/',Teachreg,name='Teachreg'),
    path('Studreg/',Studreg,name='Studreg'),
    path('Parentreg/',Parentreg,name='Parentreg'),
    path('teacheradminview/',teacheradminview,name='teacheradminview'),
    path('studentadminview/',Studentadminview,name='studentadminview'),
    path('parentadminview/',parentadminview,name='parentadminview'),
    path('teacherhome/',teacherhome,name='teacherhome'),
    path('parenthome/',parenthome,name='parenthome'),
    path('studenthome/',studenthome,name='studenthome'),
    path('teacherprofile/',teacherprofile,name='teacherprofile'),
    path('parentprofile/',parentprofile,name='parentprofile'),
    path('studentprofile/',studentprofile,name='studentprofile'),
    path('notification/',notification,name='notification'),
    path('teachernotificationview/',teachernotificationview,name='teachernotificationview'),
    path('notificationdeletedata/<int:pk>/',notificationdeletedata,name='notificationdeletedata'),
    path('notificationeditdata/<int:pk>/',notificationeditdata,name='notificationeditdata'),
    path('studentnotificationview/',studentnotificationview,name='studentnotificationview'),
    path('noteupload/',noteupload,name='noteupload'),
    path('teachernoteview/',teachernoteview,name='teachernoteview'),
    path('notedeletedata/<int:pk>/',notedeletedata,name='notedeletedata'),
    path('noteditdata/<int:pk>/',noteditdata,name='noteditdata'),
    path('studentnoteview/',studentnoteview,name='studentnoteview'),
    path('notificationparent/',notificationparent,name='notificationparent'),
    path('parentstudentview/',parentstudentview,name='parentstudentview'),
]


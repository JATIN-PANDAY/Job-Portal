from django.contrib import admin
from django.urls import path,include
from app import views
urlpatterns = [
    path("",views.index,name='index'),
    path('contact',views.contactpage,name='contact'),
    path('contactuser',views.contactuser,name='contactuser'),
    path('testimonial',views.testimonial,name='testimonial'),
    path('category',views.category,name='category'),
    path('errorpage',views.errorpage ,name='errorpage' ),

    path('about',views.about,name='about'),
    path('joblist',views.joblist,name='joblist'),
    path('jobdetail',views.jobdetail,name='jobdetail'),


    path('SignupPage',views.SignupPage,name='SignupPage'),
    path('register',views.RegisterUser,name='register'),
    path('otppage',views.otppage,name='otppage'),
    path('otpverify',views.otpverify,name='otpverify'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('loginuser',views.loginuser,name='loginuser'),
    path('userhomepage',views.userhomepage,name='userhomepage'),
    path('userabout',views.userabout,name='userabout'),
    path('userregister',views.userregister,name='userregister'),
    path('profilepage/<int:pk>',views.profilepage,name='profilepage'),
    path('profileupdate/<int:pk>',views.profileupdate,name='profileupdate'),
    path('userlogout',views.userlogout,name='userlogout'),
    path('applyjobpage/<int:pk>',views.applyjobpage,name='applyjobpage'),
    path('applyjob/<int:pk>',views.applyjob,name='applyjob'),
    path('useraccountdelete/<int:pk>',views.useraccountdelete,name='useraccountdelete'),
    path('userjoblist',views.userjoblist,name='userjoblist'),
    path('applyjobpage/<int:pk>',views.applyjobpage,name='applyjobpage'),
    path('useraccountdelete/<int:pk>',views.useraccountdelete,name='useraccountdelete'),
    path('searchjob/<int:pk>',views.searchjob,name='searchjob'),
    path('jobdetail/<int:pk>',views.jobdetail,name='jobdetail'),




##################### Company side #########################################

    path('companyindex',views.companyindex,name='companyindex'),
    path('companyprofilepage/<int:pk>',views.companyprofilepage,name='companyprofilepage'),
    path('companyprofileupdate/<int:pk>',views.companyprofileupdate,name='companyprofileupdate'),
    path('jobpost',views.jobpostpage,name='jobpost'),
    path('jobdetailsubmit',views.jobdetailsubmit,name='jobdetailsubmit'),
    path('table',views.table,name='table'),
    path('jobapplylist',views.jobapplylist,name='jobapplylist'),



#################### Admin side #############################################
   
   path('adminloginpage',views.adminloginpage,name='adminloginpage'),
   path('adminlogin',views.adminlogin,name='adminlogin'),
   path('adminindex',views.adminindex,name='adminindex'),
   path('usermaster',views.usermaster,name='usermaster'),
   path('adminuserlist',views.adminuserlist,name='userlist'),
   path('admincompanylist',views.admincompanylist,name='admincompanylist'),
   path('userdelete/<int:pk>',views.userdelete,name='userdelete'),
   path('companyverifypage/<int:pk>',views.companyverifypage,name='companyverifypage'),
   path('companyverify/<int:pk>',views.companyverify,name='verify'),
   path('companydelete/<int:pk>',views.companydelete,name='companydelete'),
   path('jobpostlist',views.jobpostlist,name='jobpostlist'),
   path('jobdelete/<int:pk>',views.jobdelete,name='jobdelete'),

  


]

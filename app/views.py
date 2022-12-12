from django.shortcuts import render,redirect
from.models import*
from random import randint
from django.contrib import messages #import messages




def index (request):
    return render (request,'index.html')
def about(request):
    return render(request,'about.html')
def contactpage(request):
    return render(request,'contact.html')
def contactuser(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        sub=request.POST['subject']
        desc=request.POST.get('desc')
        var=contact.objects.create(name=name,email=email,subject=sub,message=desc)
        messages.success(request, 'Message has been sent')
        return render(request,'contact.html')


def joblist(request):
    return render(request,'job-list.html')
def jobdetail(request):
    return render(request,'job-detail.html')
def testimonial(request):
    return render(request,'testimonial.html')
def category(request):
    return render(request,'category.html')
def errorpage (request):
    return render(request,'404.html')


def SignupPage(request):
    return render(request,'signup.html')


    #    Candidate regrestration

def RegisterUser(request):
    if request.POST['role']=='Candidate':
        role=request.POST['role']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        
        user=UserMaster.objects.filter(email=email)
        if user:
            message=' User already exist'
            return render(request,'signup.html',{'msg':message})
        else:
            if password==cpassword:
                otp=randint(100000,999999)
                newuser=UserMaster.objects.create(otp=otp,role=role,email=email,password=password)
                newcand=Candidate.objects.create(user_id=newuser,firstname=fname,lastname=lname)
                return render(request,'otpverify.html',{'email':email})

#    Company regrestration

    else:
        if request.POST['role']=='Company':
            role=request.POST['role']
            fname=request.POST['fname']
            lname=request.POST['lname']
            email=request.POST['email']
            password=request.POST['password']
            cpassword=request.POST['cpassword']
            
            user=UserMaster.objects.filter(email=email)
            if user:
                message=' User already exist'
                return render(request,'signup.html',{'msg':message})
            else:
                if password==cpassword:
                    otp=randint(100000,999999)
                    newuser=UserMaster.objects.create(otp=otp,role=role,email=email,password=password)
                    newcand=Company.objects.create(user_id=newuser,name=fname)
                    return render(request,'login.html')
                else:
                    message='Incorrect Password !'
                    print('The company register successfully',{'msg':message})    
# otp page

def otppage(request):
    return render(request,'otpverify.html')  

# otp verify

def otpverify(request):
    if request.method=='POST':
        email=request.POST['email']      
        otp=int(request.POST['otp'])
        user=UserMaster.objects.get(email=email)

        if user:
            if user.otp==otp:
                message='otp verify successfully'
                return render(request,'login.html',{'msg':message})
            else:
                message='otp is incorrect'
                return render(request,'otpverify.html',{'msg':message})
    else:
        return render(request,'signup.html')    

# loginpage

def loginpage(request):
    return render(request,'login.html')      

# user login

def loginuser(request):
    if request.POST['role']=='Candidate':
        email=request.POST['email']
        password=request.POST['password']
        
        user=UserMaster.objects.get(email=email)
        if user:
            if user.password==password and user.role=='Candidate':
                cand=Candidate.objects.get(user_id=user)
                request.session['id']=user.id
                request.session['email']=user.email
                request.session['password']=user.password
                request.session['firstname']=cand.firstname
                request.session['lastname']=cand.lastname
                return redirect('userhomepage')
            else:
                message='Incorrect Password !'
                return render(request,'login.html',{'msg':message})
        else:
            messsage='User does not exist'
            return render(request,'signup.html')
    
    #  Company login
    
    else:
        if request.POST['role']=='Company':
            email=request.POST['email']
            password=request.POST['password']
            
            user=UserMaster.objects.get(email=email)
        if user:
            if user.password==password and user.role=='Company':
                comp=Company.objects.get(user_id=user)
                request.session['id']=user.id
                request.session['name']=comp.name
                return render(request,'company/index.html')
            else:
                message='Incorrect Password !'
                return render(request,'login.html',{'msg':message})
        else:
            messsage='User does not exist'
            return render(request,'signup.html')



# User server  side


def userhomepage(request):  
    all_data=jobpost.objects.all()
    return render(request,'index1.html',{'all_data':all_data})


def userabout(request):
    return render(request,'about1.html')

def usercontact(request):
    return render(request,'contact1.html')

def userjoblist(request):
    all_data=jobpost.objects.all()
    return render(request,'joblist1.html',{'all_data':all_data})

# user register

def userregister(request):
    message='Register and Find Job '
    return render(request,'signup.html',{'msg':message})






# user profilepage

def profilepage(request,pk):
    user=UserMaster.objects.get(pk=pk)
    cand=Candidate.objects.get(user_id=user)
    return render (request,'profile.html',{'can':cand,'user':user})



# user profile update
 
def profileupdate(request,pk):
    user=UserMaster.objects.get(pk=pk)
    if user.role=="Candidate":
        cand=Candidate.objects.get(user_id=user)
        cand.state=request.POST['state']
        cand.city=request.POST['city']
        cand.email=request.POST['email']
        cand.contact=request.POST['contact']
        cand.lastname=request.POST['lastname']
        cand.firstname=request.POST['firstname']
        cand.save()
        url=f'/profilepage/{pk}'
        return redirect(url)
  
# user logout
def userlogout(request):
    del request.session['email']
    del request.session['password']
    return redirect('index')


# User account delete
def useraccountdelete(request,pk):
    user=UserMaster.objects.get(id=pk)
    user.delete()
    return redirect('index')

# Search bar

def searchjob(request,pk):
    user=UserMaster.objects.get(pk=pk)
    cand=Candidate.objects.get(user_id=user)
    if cand:
        if request.method=='POST':
            name=request.POST.get('jobname')
            location=request.POST.get('location')
            job=jobpost.objects.filter(jobname__icontains=name,location__icontains=location)
        else:
            job=jobpost.objects.all()
        return render(request,'searchjob.html',{'job':job})    
    

# user job apply

def applyjobpage(request,pk):   
    user=request.session['id']
    if user:
        cand=Candidate.objects.get(user_id=user)
        job=jobpost.objects.get(id=pk)
        return render(request,'applyjob.html',{'user':user,'cand':cand,'job':job})

def applyjob(request,pk):
    user=request.session['id']
    if user:
        cand=Candidate.objects.get(user_id=user)
        job=jobpost.objects.get(id=pk)

        edu=request.POST['qualification']
        salary=request.POST['salary']
        exp=request.POST['experience']
        resume=request.FILES['resume']
        name=request.POST['name']
        email=request.POST['email']
        contact=request.POST['contact']
        state=request.POST['state']
        city=request.POST['city']
        address=request.POST['address']
        jname=request.POST['jobname']

        desc=request.POST['desc']

        newapply=Applylist.objects.create(candidate=cand,name=name,email=email,contact=contact,state=state,city=city,address=address,
                                            jobname=jname,qualification=edu,experience=exp,salaryexpected=salary,desc=desc,resume=resume)
        message='Apply done successfully'

        return render(request,'applyjob.html',{'msg':message})  



    





##################### Company side ##############################################

def companyindex(request):
    return render(request,'company/index.html')



def companyprofilepage(request,pk):
    user=UserMaster.objects.get(pk=pk)
    comp=Company.objects.get(user_id=user)
    return render (request,'company/profile.html',{'comp':comp,'user':user})

def companyprofileupdate(request,pk):
    user=UserMaster.objects.get(pk=pk)
    if user.role=="Company":
        comp=Company.objects.get(user_id=user)
        comp.city=request.POST['city']
        comp.email=request.POST['email']
        comp.name=request.POST['name']
        comp.save()
        url=f'/companyprofilepage/{pk}'
        return redirect(url)


def jobpostpage(request):
    return render(request,'company/jobpost.html')

def jobdetailsubmit(request):

    user=UserMaster.objects.get(id=request.session['id'])

    if user:
        if user.role=='Company':

            comp=Company.objects.get(user_id=user)
            cname=request.POST.get('companyname',False)
            ccontact=request.POST.get('companycontact',False)
            caddress=request.POST.get('companyaddress',False)
            cwebsite=request.POST.get('companywebsite',False)
            respon=request.POST.get('responbilites',False)
            salary=request.POST.get('salary',False)
            jname=request.POST.get('jobname',False)
            cemail=request.POST.get('companyemail',False)
            jdesc=request.POST.get('jobdescription',False)
            qual=request.POST.get('qualification',False)
            locat=request.POST.get('location',False)
            exp=request.POST.get('experience',False)
            logo=request.FILES  ['logo']
                
            newjob=jobpost.objects.create(company_id=comp,companyname=cname,companyaddress=caddress,companycontact=ccontact,companyemail=cemail,companywebsite=cwebsite,
                                              resposibilites=respon,salarypackage=salary,experience=exp,jobname=jname,jobdescreption=jdesc,qualification=qual,location=locat,logo_pic=logo )

            message='Job post successfullly'
 
            return render(request,'company/jobpost.html',{'msg':message})

# job list table

def table(request):
    all_data=jobpost.objects.all()
    return render(request,'company/tables.html',{'all_data':all_data})

#  Candidate apply list

def jobapplylist(request):
    all_jobapply=Applylist.objects.all()
    return render(request,'company/jobapplylist.html',{'all_jobapply':all_jobapply})

################################ Admin session ###############################

def adminloginpage(request):
    return render(request,'admin/login.html')

def adminlogin(request):
    name=request.POST['username']
    password=request.POST['password']

    if name=='admin' and password=='1234':
        return redirect('adminindex')
    else:
        message="Username and Password does'nt match"
        return render(request,'admin/login.html',{'msg':message})

def adminindex(request):
        # if 'username'in request.session and 'password' in request.session :
        return render(request,'admin/index.html')
    # else:
    #     return redirect('adminlogin')


def adminuserlist(request):
    all_user=UserMaster.objects.filter(role='Candidate')
    return render(request,'admin/userlist.html',{'all_user':all_user})


def admincompanylist(request):
    all_comp=UserMaster.objects.filter(role='Company')
    return render(request,'admin/companylist.html',{'all_comp':all_comp})


def userdelete(request,pk):
    cand=UserMaster.objects.get(pk=pk)
    cand.delete()
    return redirect('adminindex')

def companyverifypage(request,pk):
    company=UserMaster.objects.get(pk=pk)
    if company:
        return render(request,'admin/verify.html')

def companyverify(request,pk):
    company=UserMaster.objects.get(pk=pk)
    if company:
        company.is_verified=request.POST.get('verify')
        company.save()
        return redirect('admincompanylist')

def companydelete(request,pk):
    company=UserMaster.objects.get(pk=pk)
    company.delete()
    return redirect('admincompanylist')

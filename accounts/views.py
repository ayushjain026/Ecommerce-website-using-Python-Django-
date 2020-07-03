from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Wrong email or password!!")
            return redirect("login")
    else:
        return render(request, "login.html")


def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['confirm_password']

        if password1 == password2:
            if User.objects.filter(username=username).exists:
                messages.info(request, f"{username} User name already taken ")
            if User.objects.filter(email=email).exists():
                messages.info(request,"E-mail exist want to login!!")
            else:
                try:
                    user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)

                    import smtplib
                    from email.message import EmailMessage
                    s = smtplib.SMTP('smtp.gmail.com', 587)
                    s.starttls()
                    msg = EmailMessage()
                    s.login(" ------ ", " ---- ")#Enter your gmail and password here
                    SUBJECT = "Welcome to AllStore"
                    TEXT = f"Hello {username},\nThank you for registering with AllStore.\nWe are so excited you joined us.\nWe have a variety of products to buy for you\n\nThank You,\nAll Stores by Ayush Jain "
                    message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
                    s.sendmail(" ------ ", f"{email}", message)#Enter your gmail and password here
                    s.quit()

                    user.save()
                except:
                    messages.info(request, "Some thing went wrong please try again!")
                    return render(request, 'register.html')
                return render(request, 'login.html')
            return render(request, 'register.html')
        else:
            messages.info(request,"Password does not match")
            return render(request, 'register.html')
    else:
        return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def contacts(request):
    return render(request, "contacts.html")


def lost(request):
    return render(request, 'lost.html')


def reset(request):
    global a
    try:
        if request.method == "POST":
            a = request.POST['username']
            if a != '':
                user = User.objects.get(username=a)
                print(f'\n\n\n\n\n\t\t\t\t\tyour password{user.password}')
                return render(request, 'reset.html')
            else:
                messages.info(request, 'Please fill all the details')
                return render(request, 'lost.html')
    except:
        messages.info(request, 'Something went wrong!!')
        return redirect(request, 'login.html')


def s(request):
    return redirect(request, 'login.html')
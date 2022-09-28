from django.shortcuts import render , redirect
from .models import Proflie , Address , Numbers 
# Create your views here.
from .forms import Sginup , ActiveFrom
from django.core.mail import send_mail
def sginup(request):
    if request.method == 'POST':
        form = Sginup(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            myfrom = form.save()
            proflie = Proflie.objects.get(user__username=username)
            proflie.active = False
            proflie.save()
            send_mail(
                subject='activeate your accounts',
                message= f"you can use this code to activate you accout {proflie.code} ",
                from_email= 'tchactive@gmail.com',
                recipient_list= [email],
                fail_silently= False,
            )
            return redirect(f'/{username}/acitve')
    else:
        form = Sginup()
    return render(request , 'registration/register.html' , {'form':form})

def useractive(request,username):
    if request.method == 'POST':
        form = ActiveFrom(request.POST)
        porflie = Proflie.objects.get(user__username=username)
        if form.is_valid():
            code = form.cleaned_data['code']
            if porflie.code == code:
                porflie.code = ''
                porflie.active = True
                porflie.code_used = True
                return redirect('/accounts/login')
            else:
                pass
    else:
        form = ActiveFrom()
    return render(request , 'registration/code.html' , {'form':form})


def user_proflie(request):
    proflie = Proflie.objects.get(user = request.user)
    addres = Address.objects.filter(user = request.user)
    number = Numbers.objects.filter(user = request.user)
    return render(request , 'registration/proflie.html' , {'proflie':proflie , 'number':number , 'adderrs':addres })
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import password_reset, password_reset_confirm
from django.contrib import auth
from django.views.decorators.csrf import csrf_protect
from forms import SignUpForm
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)     # create form object
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            subject, from_email, to = 'Welcome to BavBooks', 'sbavania12@gmail.com', email
            plaintext = get_template('Welcome.txt')
            htmly     = get_template('Welcome.html')
            text_content = plaintext.render()
            html_content = htmly.render()
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            num=msg.send()
            if num==1:
                User.objects.create_user(username=username, password=password, email=email)
                user = authenticate(username=username, password=password)
                auth.login(request, user)
                messages.add_message(request, messages.SUCCESS, 'Your account were successfully created.')
                return HttpResponseRedirect('/')
            else :
               messages.add_message(request, messages.ERROR, 'There was some problems while creating your account. Please review some fields before submiting again.')
               return render(request, 'Registration.html', { 'form': form }) 
    
        else:
            messages.add_message(request, messages.ERROR, 'There was some problems while creating your account. Please review some fields before submiting again.')
            return render(request, 'Registration.html', { 'form': form })
    
    else:
        return render(request, 'Registration.html', { 'form': SignUpForm() })

def login(request):
     if 'next' in request.GET:
         re=request.GET['next']
     else:
         re='/'
         
         
     if request.user.is_authenticated():
        return HttpResponseRedirect('/')
     else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            reg=request.POST['re1']
            
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    if 'next' in request.GET:
                        return HttpResponseRedirect(request.GET['next'])
                    else:
                        return HttpResponseRedirect(reg)
                else:
                    messages.add_message(request, messages.ERROR, 'Your account is desactivated.')
                    return render(request, 'Login.html')
            else:
                messages.add_message(request, messages.ERROR, 'Username or password invalid.')
                return render(request, 'Login.html')
        else:
            return render(request, 'Login.html',{'re': re})






def loggedout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')
    
    
    
def reset(request):
    return password_reset(request, template_name='reset.html',
        email_template_name='reset_email.html',
        subject_template_name='reset_subject.txt',
        post_reset_redirect=reverse('success'))

def reset_confirm(request, uidb64=None, token=None):
    return password_reset_confirm(request, template_name='reset_confirm.html',
        uidb64=uidb64, token=token, post_reset_redirect=reverse('reset_success'))

def success(request):
  return render(request, 'success.html')
   
def reset_success(request):
  return render(request, 'reset_success.html')        

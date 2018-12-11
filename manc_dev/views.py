from django.contrib.auth import login,authenticate
from django.shortcuts import render,get_object_or_404,redirect
from .models import Post,Profile
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes,force_text
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from .forms import SignUpForm, ContactForm
from django.http import HttpResponse
from django.core.mail import BadHeaderError, EmailMessage
from .tokens import account_activation_token


#Create your views here.
def home_page(request):
    return render(request,'manc_dev/home_page.html')

def about(request):
    detail = get_object_or_404(Post)
    frontend = {'detail':detail}
    return render(request, 'manc_dev/about.html',frontend)

def careers(request):
    detail = get_object_or_404(Post)
    frontend = {'detail':detail}
    return render(request,'manc_dev/careers.html',frontend)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('registration/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def account_activation_sent(request):
    return render(request, 'registration/account_activation_sent.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('home_page')
    else:
        return render(request, 'registration/account_activation_invalid.html')



def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            content = form.cleaned_data['content']
            try:
                email = EmailMessage(contact_name,
                                    content,
                                    contact_email,
                                    ['youremail@gmail.com'], #change to your email
                                     reply_to=[contact_email],
                                   )
                email.send()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('./thanks/')
    return render(request, 'contact_form/contact.html', {'form': form})


def thanks(request):
    return render(request, 'contact_form/thanks.html')
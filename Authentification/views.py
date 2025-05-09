from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .utils import is_ajax, classify_face
import base64
from logs.models import Log
from django.core.files.base import ContentFile
from django.contrib.auth.models import User
from profiles.models import Profile
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    # instantiate the standard Django login form
    form = AuthenticationForm(request, data=request.POST or None)

    # add Bootstrap classes so it looks nice without extra filters
    form.fields['username'].widget.attrs.update({
        'class': 'form-control',
        'placeholder': 'Username',
    })
    form.fields['password'].widget.attrs.update({
        'class': 'form-control',
        'placeholder': 'Password',
    })

    # if they submitted the username/password form (not the AJAX face-login)
    if request.method == 'POST' and 'username' in request.POST:
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')

    # render the login page with both the form and face-login JS
    return render(request, 'login.html', {
        'form': form,
    })

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home_view(request):
    return render(request, 'main.html', {})

def find_user_view(request):
    if is_ajax(request):
        photo = request.POST.get('photo')
        _, str_img = photo.split(';base64')

        # print(photo)
        decoded_file = base64.b64decode(str_img)
        print(decoded_file)

        x = Log()
        x.photo.save('upload.png', ContentFile(decoded_file))
        x.save()

        res = classify_face(x.photo.path)
        if res:
            user_exists = User.objects.filter(username=res).exists()
            if user_exists:
                user = User.objects.get(username=res)
                profile = Profile.objects.get(user=user)
                x.profile = profile
                x.save()

                login(request, user)
                return JsonResponse({'success': True})
        return JsonResponse({'success': False})
    
from django.shortcuts import render, HttpResponse

from django.contrib.auth.decorators import login_required

from .models import Profile

from .forms import  UserRegistrationForm, UserEditForm, ProfileEditForm

@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})

def Signup(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            # 当用户注册的时候，会自动建立一个空白的用户信息关联到用户。在之前创建的用户，则必须在管理后台中手工为其添加对应的Profile对象
            Profile.objects.create(user=new_user)
            return render(request, 'registration/signup_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/signup.html', {'form': user_form})

from django.http import HttpResponse,JsonResponse
import json
@login_required
def edit(request):
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return JsonResponse({"title":"Success!!!","message":"Successfully published","icon":"success"})
        else:
            el1 = json.loads(user_form.errors.as_json())
            el2 = json.loads(profile_form.errors.as_json())
            el1.update(el2)
            return JsonResponse({"title":"ERROR!!!","message": el1,"icon":"error"})
    else:
        try:
            Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            Profile.objects.create(user=request.user)
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request, 'account/edit.html', {'user_form': user_form, 'profile_form': profile_form})



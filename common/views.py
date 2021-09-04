from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm


def signup(request):
    """
    회원가입
    """

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})




def page_not_found(request, exception, template_name="templates/common/404.html"):
    """
    404 Page Not Found
    """
    return render(request, template_name, {})

def server_error(request, *args, **argv):
    return render(request, 'templates/common/500.html', status=500)


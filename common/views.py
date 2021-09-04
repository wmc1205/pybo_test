from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response,render, redirect
from django.template import RequestContext
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


def page_not_found(request, exception):
    """
    404 Page Not Found
    """
    response=render_to_response('common/404.html',{},
                                context_instance=RequestContext(request))
    response.status_code = 404
    return response

def server_error(request):
    response = render_to_response('common/505.html',{},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response
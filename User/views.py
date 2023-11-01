from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.conf import settings


def login_view(request):
    try:
        url_id = request.GET.get('session_id', None)
        if url_id:
            print('login1')
            request.session["session_id"] = url_id
            return redirect("/")
        else:
            print('login2')
            return redirect(f"https://100014.pythonanywhere.com/?redirect_url={settings.MY_BASE_URL}/user/login/")
    except Exception as e:
        print(str(e))
        return redirect(f"https://100014.pythonanywhere.com/?redirect_url={settings.MY_BASE_URL}/user/login/")

def signout_view(request):
    d = request.session.get("session_id")
    if d:
        try:
            print('out1')
            del request.session["session_id"]
            return redirect("https://100014.pythonanywhere.com/sign-out")
        except Exception as e:
            print(str(e))
            return redirect("https://100014.pythonanywhere.com/sign-out")
    else:
        print('out2')
        return redirect("https://100014.pythonanywhere.com/sign-out")
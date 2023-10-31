from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from imgtotext.noun_verb import extract_dialogue_info_from_image
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os

def Home(request):
    try:
        if request.session.get("session_id"):
            return render(request, 'base.html')
        else:
            return redirect(f"https://100014.pythonanywhere.com/?redirect_url={settings.MY_BASE_URL}/user/login/")
    except Exception as e:
        return redirect(f"https://100014.pythonanywhere.com/?redirect_url={settings.MY_BASE_URL}/user/login/")

def Collect_noun_and_verb(request):

    try:
        if request.session.get("session_id"):

            if request.method == 'GET':
                return render(request, 'image_upload_page.html')

            if request.method == 'POST':
                if 'image' in request.FILES:
                    uploaded_image = request.FILES['image']

                    fs = FileSystemStorage(location=os.path.join(settings.STATICFILES_DIRS[0], 'UPLOAD'))
                    saved_path = fs.save(uploaded_image.name, uploaded_image)

                    result_dict = extract_dialogue_info_from_image(os.path.join(settings.STATICFILES_DIRS[0], 'UPLOAD', saved_path))

                return render(request, 'separate_results.html', {'dialogue_info': result_dict})
        else:
            return redirect(f"https://100014.pythonanywhere.com/?redirect_url={settings.MY_BASE_URL}/user/login/")
    except Exception as e:
        return redirect(f"https://100014.pythonanywhere.com/?redirect_url={settings.MY_BASE_URL}/user/login/")
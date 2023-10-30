from django.shortcuts import render
from imgtotext.noun_verb import extract_dialogue_info_from_image
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os


def Home(request):
    return render(request, 'base.html')

def Collect_noun_and_verb(request):
    if request.method == 'GET':
        return render(request, 'image_upload_page.html')

    if request.method == 'POST':
        if 'image' in request.FILES:
            uploaded_image = request.FILES['image']

            fs = FileSystemStorage(location=os.path.join(settings.STATICFILES_DIRS[0], 'UPLOAD'))
            saved_path = fs.save(uploaded_image.name, uploaded_image)

            result_dict = extract_dialogue_info_from_image(os.path.join(settings.STATICFILES_DIRS[0], 'UPLOAD', saved_path))

        return render(request, 'separate_results.html', {'dialogue_info': result_dict})
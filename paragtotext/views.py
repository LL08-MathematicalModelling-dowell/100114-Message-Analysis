from django.shortcuts import render, redirect
from paragtotext.analyzing_data import For_noun_verb_adj_from_article
from .test import *
from summery import settings
from paragtotext.time_with_sentence import organize_text_by_time


# Create your views here.
# def Collect_noun_and_verb_from_article(request):
#
#     try:
#         if request.session.get("session_id"):
#
#             if request.method == 'GET':
#                 return render(request, 'article_upload_page.html')
#
#             if request.method == 'POST':
#                 article = request.POST['article']
#                 print(article)
#                 result_dict = For_noun_verb_adj_from_article(article)
#
#                 return render(request, 'separate_results.html', {'dialogue_info': result_dict})
#         else:
#             return redirect(f"https://100014.pythonanywhere.com/?redirect_url={settings.MY_BASE_URL}/user/login/")
#     except Exception as e:
#         return redirect(f"https://100014.pythonanywhere.com/?redirect_url={settings.MY_BASE_URL}/user/login/")



def Collect_noun_and_verb_from_article_with_time(request):

    try:
        if request.session.get("session_id"):
            # print(1)
            if request.method == 'GET':
                return render(request, 'article_upload_page.html')

            if request.method == 'POST':
                article = request.POST['article']
                # print(article)
                result_dict = organize_text_by_time(article)
                # print(result_dict)

                if len(result_dict)<=0:
                    return render(request, 'check.html', {'dialogue_info': result_dict,'msg':'Write or Paste appropriate article.'})
                else:
                    return render(request, 'check.html', {'dialogue_info': result_dict})

        else:
            return redirect(f"https://100014.pythonanywhere.com/?redirect_url={settings.MY_BASE_URL}/user/login/")
    except Exception as e:
        return redirect(f"https://100014.pythonanywhere.com/?redirect_url={settings.MY_BASE_URL}/user/login/")
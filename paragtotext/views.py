from django.shortcuts import render, redirect
from paragtotext.analyzing_data import For_noun_verb_adj_from_article
from summery import settings


# Create your views here.
def Collect_noun_and_verb_from_article(request):

    try:
        if request.session.get("session_id"):

            if request.method == 'GET':
                return render(request, 'article_upload_page.html')

            if request.method == 'POST':
                article = request.POST['article']
                print(article)
                result_dict = For_noun_verb_adj_from_article(article)

                return render(request, 'separate_results.html', {'dialogue_info': result_dict})
        else:
            return redirect(f"https://100014.pythonanywhere.com/?redirect_url={settings.MY_BASE_URL}/user/login/")
    except Exception as e:
        return redirect(f"https://100014.pythonanywhere.com/?redirect_url={settings.MY_BASE_URL}/user/login/")
#-*- coding: utf-8 -*-

from django.http import HttpResponse, Http404
from django.shortcuts import redirect

def home(request):
    text = """<h1>Bienvenue sur mon blog !</h1>
    <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>"""

    return HttpResponse(text)

def view_article(request, id_article):
    """Renvoie l'article correspondant à l'identifiant."""

    if int(id_article) > 100:
        raise Http404

    return redirect(view_redirection)

def list_articles(request, month, year):
    """Liste des articles d'un mois précis."""

    text = "Vous avez demandé les articles de {0} {1}".format(month, year)
    return HttpResponse(text)

def view_redirection(request):
    return HttpResponse(u"Vous avez été redirigé.")

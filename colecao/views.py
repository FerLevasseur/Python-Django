from django.shortcuts import render


def index(request):
    return render(request, 'colecao/index.html')

def imagem(request):
    return render(request, 'colecao/imagem.html')

# Create your views here.

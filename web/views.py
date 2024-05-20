from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore
from .sardinas import predict_code

def form(request):
    return render(request, 'lang_formulaire.html')

def submit_view(request):
    if request.method == 'POST':
        langage = set()
        for key in request.POST:
            if key.startswith('mot'):
                langage.add(request.POST[key].strip())
        is_code = predict_code(langage)
        if is_code:
            return render(request, 'positif.html', {'langage': langage})
        else:
            return render(request, 'negatif.html', {'langage': langage})
    return render(request, 'lang_formulaire.html')

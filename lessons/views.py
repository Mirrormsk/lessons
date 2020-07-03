from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def reverse(request):
    text: str = request.GET['usertext']
    cnt = len(text.split())
    reversed_text = text[::-1]
    return render(request, 'reverse.html', {'reversed_text': reversed_text,
                                            'usertext': text,
                                            'cnt': cnt})

from django.http import HttpResponse


def test_sos(request):
    return HttpResponse('<h1> this is sos project 13</h1>')
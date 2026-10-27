from django.http import HttpResponse


def test_sos(request):
    return HttpResponse('<h1> this sos app of project 15 </h1>')
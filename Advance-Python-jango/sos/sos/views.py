from django.http import HttpResponse

def test_sos(request):
    return HttpResponse("Hello,world.you're at the sos test page.")
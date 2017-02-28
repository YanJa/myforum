from django.http import HttpResponse


def index(request):
    for i in dir(request):
        # print(i, end="\n")
        pass
    print(request.get_host())
    print(request.get_port())
    print(request.get_raw_uri())
    return HttpResponse("Hello world")

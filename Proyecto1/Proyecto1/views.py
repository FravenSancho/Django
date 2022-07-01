from django.http import HttpResponse

def saludo(request):

    return HttpResponse("hola perras")

def despedida(request):
    return HttpResponse("adiós perras")

name='Lizz'
print(name[0:2])
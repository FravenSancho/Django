from django.http import HttpResponse
import datetime

def saludo(request): #First View

    documento = """<html>
    <body>
    <h1>
    Hola Mundo
    </h1>
    </body>
    </html>"""

    return HttpResponse(documento)

def despedida(request):

    return HttpResponse("Adiós Mundo")

def fecha(request):

    fecha_actual = datetime.datetime.now()

    documento = """<html>
    <body>
    <h1>
    Fecha y hora actuales %s
    </h1>
    </body>
    </html>""" % fecha_actual

    return HttpResponse(documento)

def calcularEdad(request, agno,edad):
    
    
    periodo = agno - 2022
    edadFutura = edad + periodo
    documento = "<html><body><h1>En el año %s tendrás %s años" %(agno, edadFutura)

    return HttpResponse(documento)
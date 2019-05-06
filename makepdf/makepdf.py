from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import datetime 
_days = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
_months = [
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
_today = datetime.datetime.now()


def hazcarta(*args):
    tipos = args[0]
    tipos = args[0]
    equipo = args[2]
    print (len(args))
    
    w, h = A4
    c = canvas.Canvas("hola-mundo.pdf", pagesize=A4)
    c.drawString(50, h - 50, "Mexico {}  {} de {} del {}".format(
        _days[datetime.date.weekday(datetime.date.today())],
        _today.day,
        _months[datetime.date.today().month - 1],
        2019))
    
    c.showPage()
    c.save()
    
hazcarta(1,2,3)

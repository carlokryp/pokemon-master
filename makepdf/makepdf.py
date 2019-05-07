from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import datetime
_days = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes",
         "Sabado", "Domingo"]
_months = [
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
_today = datetime.datetime.now()


def hazcarta(*args):
    tipos = args[0]
    resp = args[1]
    equipo = args[2]
    w, h = A4
    c = canvas.Canvas("hola-mundo.pdf", pagesize=A4)
    url_img = "http://cort.as/-HmvP"
    c.drawImage(url_img, 40, h - 280, width=270, height=270)
    c.drawString(380, h - 50, "Mexico {}  {} de {} del {}".format(
        _days[datetime.date.weekday(datetime.date.today())],
        _today.day,
        _months[datetime.date.today().month - 1],
        2019))
    text = c.beginText(70, h - 280)
    text.setFont("Times-Roman", 16)
    text.textLines(
        "Bienvenido maestro pokemon. \
        \n Elegiste ser Maestro tipo {} ".format(tipos[resp]))
    text.textLines("\n\n")
    text.textLines(
        "Tu equipo está conformado por 6 pokemones con 4 ataques:")
    text.textLines("\n\n")
    for i in range(6):
        aux = equipo[i][1]
        aux = [i.capitalize() for i in aux]
        text.textLines(
            "{} : {}: 1:{} 2:{} 3: {} 4:{} \n "
            .format(
             i+1, equipo[i][0].capitalize(), aux[0], aux[1], aux[2], aux[3]))
    text.textLines("\n\n")
    text.textLines(" \n Te deseo la mejor de las suertes")
    firma = c.beginText(200, 180)
    firma.setFont("Times-Roman", 14)
    firma.textLines("Atentamente: CarloKryp")
    c.drawText(text)
    c.drawText(firma)
    c.showPage()
    c.save()
    # Verificar try
    print("Se ha generado un archivo pdf donde ejecutaste main.py")

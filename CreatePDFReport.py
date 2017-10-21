#pip install reportlab
from reportlab.pdfgen import canvas
import database_value_change
import database_design

c = canvas.Canvas("report.pdf")
database_design.cursor.execute("SELECT * FROM BUSINESS WHERE Id = 1 ")
data = database_design.cursor.fetchall()
print (type(data))
print list(data[0])
a = [str(i) for i in data]
b = ','.join(a)
print (type(b))
print b[:]
c.drawString(50,800,b[:])
c.save()

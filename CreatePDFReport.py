#pip install reportlab
from reportlab.pdfgen import canvas
from ast import literal_eval
import database_value_change
import database_design

c = canvas.Canvas("report.pdf")
database_design.cursor.execute("SELECT * FROM BUSINESS")
data = database_design.cursor.fetchall()

for row in data:
   print "BusinessName  " + row[1]
   print "BusinessOrigin" + row[2]
   print "BusinessDestination" + row[3]
   print "BusinessGoods" + row[4]
   print "BusinessWeight" + str(row[5])
   print "BusinessInvoices" + str(row[6])
   print "BusinessStartingDate" + row[7]
   print "BusinessEndDate" + row[8]

BusinessName= "BusinessName: " + row[1]
BusinessOrigin = "BusinessOrigin: " + row[2]
BusinessDestination = "BusinessDestination: " + row[3]
BusinessGoods = "BusinessGoods: " + row[4]
BusinessWeight = "BusinessWeight: " + str(row[5]) + " kg"
BusinessInvoices = "BusinessInvoices: " + str(row[6]) + " $ "
BusinessStartingDate = "BusinessStartingDate: " + row[7]
BusinessEndDate = "BusinessEndDate: " + row[8]

c.drawString(50,800,BusinessName)
c.drawString(50,780,BusinessOrigin)
c.drawString(50,760,BusinessDestination)
c.drawString(50,740,BusinessGoods)
c.drawString(50,720,BusinessWeight)
c.drawString(50,700,BusinessInvoices)
c.drawString(50,680,BusinessStartingDate)
c.drawString(50,660,BusinessEndDate)

c.save()

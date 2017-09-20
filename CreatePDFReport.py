from reportlab.pdfgen import canvas

c = canvas.Canvas("report.pdf")
c.drawString(100, 750, "Hello World!")
c.circle(132, 750, 50, 1)
c.save()

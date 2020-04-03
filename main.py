# --Imported Modules--
import random
from datetime import date

# --Key Variables--
now = date.today()
jobID = random.randint(1000, 9999)

# --Guide Lines--
def drawMyRuler(pdf):
    pdf.drawString(100,810, 'x100')
    pdf.drawString(200,810, 'x200')
    pdf.drawString(300,810, 'x300')
    pdf.drawString(400,810, 'x400')
    pdf.drawString(500,810, 'x500')

    pdf.drawString(10,100, 'y100')
    pdf.drawString(10,200, 'y200')
    pdf.drawString(10,300, 'y300')
    pdf.drawString(10,400, 'y400')
    pdf.drawString(10,500, 'y500')
    pdf.drawString(10,600, 'y600')
    pdf.drawString(10,700, 'y700')
    pdf.drawString(10,800, 'y800')    

# --Questions--
starting = input("Starting Location: ")
starting = starting.title()
#
destination = input("Finishing Location: ")
destination = destination.title()
#
distance = int(input("Distance: "))
distanceUnits = input("KM or Miles? ")
distanceUnits = distanceUnits.upper()
totalDistance = str(distance) + ' ' + distanceUnits
#
cargo = input("Cargo Description: ")
cargo = cargo.title()
cargoWeight = int(input("Cargo Weight: "))
cargoUnits = input("KG or Tonnes? ")
cargoUnits = cargoUnits.upper()
cargoTotal = str(cargoWeight) + ' ' + cargoUnits + ' ' + cargo
#
finance = int(input("Profit: "))

# --Content--
fileName = 'job.pdf' #' + str(jobID) + '# Add this piece after 'job' for custom ID files
documentTitle = 'Job Number: ' + str(jobID)
textLines = [
    'Starting: ' + starting,
    'Destination: ' + destination,
    'Distance: ' + totalDistance,
    'Cargo: ' + cargoTotal,
    'Finance: ' + str(finance)
]

image = 'https://codysinfo.uk/vtcpy/exampleVTC.png'

# --Document Setup-- 
from reportlab.pdfgen import canvas

pdf = canvas.Canvas(fileName)
pdf.setTitle(documentTitle)

# --Document Addons--

# Guild Lines (Only Active When Editing File)
#drawMyRuler(pdf)

# Register A New Font
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

# Colours - colors.[colour]
# from reportlab.lib import colors

pdfmetrics.registerFont(
    TTFont('abc', 'https://codysinfo.uk/vtcpy/Poppins-Regular.ttf')
)
pdf.setFont('abc', 36)

# --Title--  

# VTC Image
pdf.drawInlineImage(image, 75, 600)

# Title
pdf.drawCentredString(300, 565, "Title Here")

# --Sub Title-- 
pdf.setFillColorCMYK(22, 11, 0, 0)
pdf.setFont('abc', 24)
pdf.drawCentredString(300, 525, "Job Number ID: ")
pdf.drawCentredString(300, 500, str(jobID)) 
pdf.drawCentredString(300, 390, "Job Details:")

# Box
pdf.line(30, 380, 570, 380)
pdf.line(30, 380, 30, 50)
pdf.line(30, 50, 570, 50)
pdf.line(570, 380, 570, 50)

# Job Information
text = pdf.beginText(200, 300)
text.setFillColorCMYK(22, 11, 0, 0)
text.setFont("Courier", 18)
for line in textLines:
    text.textLine(line)

pdf.drawText(text)


# --Footer-- !!DO NOT EDIT!!
pdf.setFillColorCMYK(22, 11, 0, 0)
pdf.setFont('abc', 16)
pdf.drawCentredString(290, 25, "2020 © Property of Cody Allen")

# Save PDF
pdf.save()
from reportlab.lib.colors import blue
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

import json

canvas = Canvas("BadApple.pdf", pagesize=A4)
 
WIDTH, HEIGHT = A4
FONT_SIZE = 10

X_OFFSET, Y_OFFSET = 9, HEIGHT-204 

# Set font
pdfmetrics.registerFont(TTFont("FreeMono","data\\FreeMono.ttf"))
canvas.setFont("FreeMono", FONT_SIZE)

canvas.setFillColor(blue)
with open("data/data.json", "r") as read_file:
    arr = json.load(read_file)



for i in range(0,6572): #6572
    frame = arr[i]
    for y in range(72):
        line = ""
        for x in range(96):
            if frame[y][x] == 1:
                line += "■"
            else:
                line += " "
        canvas.drawString(X_OFFSET, Y_OFFSET-y*(FONT_SIZE*0.6), line)
    canvas.showPage()
    canvas.setFont("FreeMono", FONT_SIZE)
    canvas.setFillColor(blue)



# Save the PDF file
canvas.save()
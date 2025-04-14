from fpdf import FPDF, XPos, YPos
from PIL import Image

name=input("Name: ")

class PDF(FPDF):
    def header(self):
        self.set_font("Helvetica",size=25)
        text_x = (self.w - self.get_string_width(f"CS50 Shirtificate")) / 2
        text_y = (self.h  - 250)
        self.text(text_x, text_y, f"CS50 Shirtificate")

pdf = PDF()
pdf.add_page()
pdf.set_auto_page_break(False)
pdf.image("shirtificate.png", x=30, y=90, w=150)
pdf.set_text_color(255, 255, 255)  # Set the text color to white
pdf.set_font("Helvetica", size=25)
text_x = (pdf.w - pdf.get_string_width(f"{name} took CS50")) / 2
text_y = (pdf.h  - 90/2)/2
pdf.text(text_x, text_y, f"{name} took CS50")

pdf.output("shirtificate.pdf")

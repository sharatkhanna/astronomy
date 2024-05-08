from pathlib import Path
import glob
from fpdf import FPDF

filepaths = glob.glob("files/*.txt")
pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
    filename = Path(filepath).stem
    pdf.add_page()
    pdf.set_font(family="Times", size=20, style="B")
    pdf.cell(w=50, h=8, txt=filename.capitalize(), ln=1)

    file = open(filepath, "r")
    content = file.read()

    pdf.set_font(family="Times", size=12)
    pdf.multi_cell(w=0, h=6, txt=content)

pdf.output("output.pdf")


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

pdf.output("output.pdf")


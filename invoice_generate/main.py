import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    pdf = FPDF(orientation="L", unit="mm", format="A4")
    pdf.add_page()

    filename = Path(filepath).stem
    invoice_nr, inv_dt = filename.split("-")

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice Nr. {invoice_nr}", ln=1)
    pdf.cell(w=50, h=8, txt=f"Date. {inv_dt}", ln=1)
    pdf.ln()

    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    titles = list(df.columns)
    titles =[item.replace("_"," ").title() for item in titles]
    total = df["total_price"].sum()

    pdf.set_font(family="Times", size=12, style="B")
    pdf.cell(w=30, h=8, txt=titles[0], border=1, align="C")
    pdf.cell(w=75, h=8, txt=titles[1], border=1, align="C")
    pdf.cell(w=40, h=8, txt=titles[2], border=1, align="C")
    pdf.cell(w=30, h=8, txt=titles[3], border=1, align="C")
    pdf.cell(w=30, h=8, txt=titles[4], border=1, align="C", ln=1)

    for index, row in df.iterrows():
        pdf.set_font(family="Times", size=12)
        pdf.set_text_color(80,80,80)
        pdf.cell(w=30, h=8, txt=str(row['product_id']), border=1, align="C")
        pdf.cell(w=75, h=8, txt=str(row['product_name']), border=1, align="C")
        pdf.cell(w=40, h=8, txt=str(row['amount_purchased']), border=1, align="C")
        pdf.cell(w=30, h=8, txt=str(row['price_per_unit']), border=1, align="C")
        pdf.cell(w=30, h=8, txt=str(row['total_price']), border=1, align="C", ln=1)

    pdf.set_font(family="Times", size=12, style="B")
    pdf.cell(w=175, h=8, txt="Grand Total", border=1, align="L")
    pdf.cell(w=30, h=8, txt=str(total), border=1, align="C", ln=1)

    pdf.set_font(family="Times", size=12, style="B")
    pdf.cell(w=30, h=8, txt=f"The total amount due is {total}.", ln=1)
    pdf.ln()

    pdf.set_font(family="Times", size=14, style="B")
    pdf.cell(w=30, h=8, txt=f"PythonHow")
    pdf.image("pythonhow.png", w=10)

    pdf.output(f"PDFs/{filename}.pdf")




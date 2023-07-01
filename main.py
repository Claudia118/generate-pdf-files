from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

# reading CSV file
df = pd.read_csv("topics.csv")

# Displays master page
for index, row in df.iterrows():
    # Adding page Header content
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=30)
    pdf.set_text_color(25, 25, 112)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)

    # Adding a line
    pdf.line(10, 21, 200, 21)

    # Set footer for master page
    # Number of lines to go down to place footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=10)
    pdf.set_text_color(25, 25, 112)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="R")

    # Displays other pages
    for i in range(row["Pages"] - 1):
        pdf.add_page()

        # Set footer for other pages
        # Number of lines to go down to place footer
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=10)
        pdf.set_text_color(25, 25, 112)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="R")

pdf.output("output.pdf")
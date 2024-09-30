import pdfplumber

def extract_text_from_pdf_with_plumber(pdf_file_path):
    with pdfplumber.open(pdf_file_path) as pdf:
        extracted_text = ""
        for page in pdf.pages:
            extracted_text += page.extract_text() + "\n"
    
    return extracted_text

pdf_path = 'document.pdf'
text = extract_text_from_pdf_with_plumber(pdf_path)

print(text)

with open('extracted_text.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(text)

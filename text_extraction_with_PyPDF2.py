import PyPDF2

def extract_text_from_pdf(pdf_file_path):
    with open(pdf_file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        
        extracted_text = ""
        
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            extracted_text += page.extract_text()
        
        return extracted_text

pdf_path = 'document.pdf'
text = extract_text_from_pdf(pdf_path)

print(text)

with open('extracted_text.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(text)


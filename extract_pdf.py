from pypdf import PdfReader
import sys

pdf_path = r"c:\Users\hp\Downloads\DATAANALYST.pdf"

try:
    reader = PdfReader(pdf_path)
    texts = []
    for page in reader.pages:
        t = page.extract_text()
        if t:
            texts.append(t)
    out = "\n\n".join(texts)
    with open('extracted_dataanalyst.txt', 'w', encoding='utf-8') as f:
        f.write(out)
    # wrote output to extracted_dataanalyst.txt (UTF-8)
except Exception as e:
    print('ERROR:', e, file=sys.stderr)
    sys.exit(1)

import fitz
from PIL import Image
import io

# Open a PDF file
pdf_file = fitz.open("HCI.pdf")

# Extract text from PDF and save to individual text files
for pageNumber, page in enumerate(pdf_file.pages(), start=1):
    text = page.get_text("text")
    txt = open(f"report_Page.txt", "a", encoding="utf-8")
    txt.writelines(text.strip())
    txt.close()

# Extract images from PDF
for page_index in range(len(pdf_file)):
    page = pdf_file[page_index]

    image_list = page.get_images(full=True)


    for image_index, img in enumerate(image_list, start=1):
        xref = img[0]
        base_image = pdf_file.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]

        image = Image.open(io.BytesIO(image_bytes))
        image = image.convert("RGB")  # Convert to RGB color mode
        image.save(f"./img/image_page_{page_index}_index_{image_index}.{image_ext}")
        

# Close the PDF file
pdf_file.close()

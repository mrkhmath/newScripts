import PyPDF2
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io
from PIL import Image
import tempfile

def resize_and_add_image_to_pdf(pdf_path, image_path, output_pdf_path):
    # Load the original PDF
    input_pdf = PyPDF2.PdfReader(open(pdf_path, 'rb'))
    
    # Ensure the PDF has at least 2 pages
    if len(input_pdf.pages) < 2:
        raise ValueError("The PDF does not have enough pages.")
    
    # Load the image and resize it to 20% of its original size
    image = Image.open(image_path)
    image_width, image_height = image.size
    new_size = (int(image_width * 0.1), int(image_height * 0.1))
    image_resized = image.resize(new_size, Image.ANTIALIAS)
    
    # Save the resized image to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as temp_image_file:
        image_format = 'PNG'  # Use PNG as a safe default format
        image_resized.save(temp_image_file, format=image_format)
        temp_image_path = temp_image_file.name
    
    # Create a new PDF page with the resized image
    packet = io.BytesIO()
    c = canvas.Canvas(packet, pagesize=letter)
    # Adjust x, y coordinates to position the image at the desired location on the page
    c.drawImage(temp_image_path, 50, 630, width=new_size[0], height=new_size[1])  # Position as needed
    c.showPage()
    c.save()
    
    # Clean up the temporary image file
    # os.unlink(temp_image_path)  # Uncomment this if you want to delete the temp file immediately after use
    
    packet.seek(0)
    new_pdf = PyPDF2.PdfReader(packet)
    
    # Create an output PDF
    output = PyPDF2.PdfWriter()
    
    # Add the first page as is
    output.add_page(input_pdf.pages[0])
    
    # Merge the second page with the new PDF that contains the image
    page = input_pdf.pages[1]
    watermark = new_pdf.pages[0]
    page.merge_page(watermark)
    output.add_page(page)
    
    # If there are more than 2 pages, add the rest of the pages
    if len(input_pdf.pages) > 2:
        for i in range(2, len(input_pdf.pages)):
            output.add_page(input_pdf.pages[i])
    
    # Save the output PDF
    with open(output_pdf_path, 'wb') as outputStream:
        output.write(outputStream)

# Example usage
pdf_path = 'C:/Users/kh_ma/Downloads/original.pdf'
image_path = 'C:/Users/kh_ma/Downloads/Capture.PNG'
output_pdf_path = 'C:/Users/kh_ma/Downloads/output.pdf'
resize_and_add_image_to_pdf(pdf_path, image_path, output_pdf_path)

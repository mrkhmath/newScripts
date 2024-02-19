from PyPDF2 import PdfReader, PdfWriter
import re

# File path for the PDF
file_path = 'C:\\Users\\kh_ma\\Downloads\\eSIS_Report_grade_10.pdf'

# Function to split PDF into separate pages and name each file by the number opposite to "Student #"
def split_pdf(file_path):
    # Open the PDF file
    pdf = PdfReader(open(file_path, "rb"))

    # Iterate through each page of the PDF
    for page_num in range(len(pdf.pages)):
        # Get a single page
        page = pdf.pages[page_num]

        # Extract text from the page
        text = page.extract_text()
 
        # Find the student number using a regular expression
        # Assuming the student number is in the format "Student #: [Number]"
        match = re.match(r'Student #:\s*(\d+)', text)
        student_number=text.split('\n')[7].split()[0]
        # if text.split('\n')[9].split()[0]=="Please":
        #  print(student_number)
        # if match:
            # student_number = match.group(1)
        #    
        # else:
            # If no student number is found, name the file with page number
            # student_number = f'page_{page_num + 1}'

        # Create a new PDF writer object and add the single page
        pdf_writer = PdfWriter()
        pdf_writer.add_page(page)

#         # Output file path
        output_filename = f'C:\\Users\\kh_ma\\Downloads\\10Reports\\{student_number}.pdf'

#         # Write the page to a new file
        with open(output_filename, "wb") as output_file:
            pdf_writer.write(output_file)
        
        print(f"Created: {output_filename}")

# Call the function to split the PDF
split_pdf(file_path)


# 683433
# 683820
# 684202
# 685558
# 686093
# 697534
# 711401
# 714939
# 732594
# 737662
# 739636
# 793752
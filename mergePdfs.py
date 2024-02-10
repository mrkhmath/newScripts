import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfReader, PdfWriter

def merge_pdfs(paths, output):
    pdf_writer = PdfWriter()
    for path in paths:
        pdf_reader = PdfReader(path)
        for page in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page])
    with open(output, 'wb') as out:
        pdf_writer.write(out)

def select_files():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_paths = filedialog.askopenfilenames(title='Select PDF Files', filetypes=[('PDF Files', '*.pdf')])
    if not file_paths:
        messagebox.showwarning("Warning", "No PDF files were selected!")
        root.destroy()
        return None, None
    return root, file_paths

def save_file_dialog(root):
    output_file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")], title="Save the merged PDF as...")
    if not output_file:
        messagebox.showwarning("Warning", "You did not specify an output file!")
        root.destroy()
        return None
    return output_file

def main():
    root, file_paths = select_files()
    if file_paths:  # Proceed if the user selected at least one file
        output_file = save_file_dialog(root)
        if output_file:  # Proceed if the user specified an output file name
            merge_pdfs(file_paths, output_file)
            messagebox.showinfo(title="Success", message="PDFs merged successfully!")
    root.destroy()

if __name__ == "__main__":
    main()

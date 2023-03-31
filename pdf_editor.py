import PyPDF2
import os
import time

# get the project directory
current_dir = os.getcwd()

# get directory of PDF files to be edited
files_to_edit_path = os.path.join(current_dir, 'PDFs')

# get all PDF files inside directory and store in a list
pdfs_path = []

# loop through all the files in the directory
for file_name in os.listdir(files_to_edit_path):
    if file_name.endswith('.pdf'):
        pdfs_path.append(os.path.join(files_to_edit_path, file_name))

# rotate PDFs
print(f'Rotating {len(pdfs_path)} PDFs')
for pdf_path in pdfs_path:
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        pdf_writer = PyPDF2.PdfWriter()

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            page.rotate(-90)
            pdf_writer.add_page(page)

        # get file_name again for saving
        file_name_for_saving = os.path.basename(pdf_path)

        with open(f'{current_dir}/Edited PDFs/{file_name_for_saving}', 'wb') as output_file:
            pdf_writer.write(output_file)
            
time.sleep(3)
print('Done!')
print('Please check in the Edited PDFs folder.')
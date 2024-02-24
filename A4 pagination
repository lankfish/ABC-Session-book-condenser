#%% Preamble

import os
from pypdf import PdfReader, PdfWriter

#Assumes script is in same directory as desired PDF file
pythonpath = os.path.dirname(__file__)

#USER INPUTS
#Filename of file to condense (including .abc)
infile = "condensed_book.pdf"
#Filename of file to output to (including .abc)
outfile = "A4_ordered_book.pdf"

#%%

A6_book = PdfReader(pythonpath + "\\" + infile)
A4_ordered = PdfWriter()

start_page = 0
while start_page + 7 <= A6_book._get_num_pages():
    print(f"starting at p.{start_page}, ending at p.{start_page+7}")
    for num in [0, 2, 4, 6, 3, 1, 7, 5]:
        A4_ordered.add_page(A6_book.pages[start_page + num])
    start_page += 8
    
for num in [0, 2, 4, 6, 3, 1, 7, 5]:
    try:
        A4_ordered.add_page(A6_book.pages[start_page + num])
    except:
        A4_ordered.add_blank_page()

A4_ordered.write(pythonpath + "\\" + outfile)

# -*- coding: utf-8 -*-
#%%Preamble

import re
import os

#Assumes script is in same directory as desired ABC file
pythonpath = os.path.dirname(__file__)

#USER INPUTS
#Filename of file to condense (including .abc)
infile = "folksoc_book.abc"
#Filename of file to output to (including .abc)
outfile = "condensed_book_in_order.abc"
#Organise for A4 double-sided printing?
A4_printing = False

#Formatting header
formathead = ["%%pageheight 10.5cm",
              "%%pagewidth 14.8cm",
              "%%pagescale 0.6",
              "%%topmargin 0.5cm",
              "%%botmargin 0.5cm",
              "%%leftmargin 1.5cm",
              "%%rightmargin 1.5cm",
              "%%gutter 1cm",
              "%%titlefont Times-roman 20",
              "%%vskip 4cm",
              "%%textfont Times-roman 40",
              "%%center Condensed Tunebook \n",
              "<div class=\"abc-file-header\">",
              "%%titlefont Times-roman 20",
              "</div>\n",
              "%%newpage\n"]

#Section titles
titlelist = ["\n%%newpage",
              "X:{xnum}",
              "%%titlefont Times-roman 40",
              "T:{ttitle}",
              "K:\n\n"]

#%%
comped = []
comped.append("\n".join(formathead))
valid_starts = ["A:", "B:", "C:", "D:", "F:", "G:", "H:", "K:", "L:", "M:", "m:",
                "N:", "O:", "P:", "Q:", "R:", "r:", "S:", "s:", "T:", "U:", "W:",
                "w:", "Z:"]

f = open(pythonpath + "\\" + infile)
file = f.readlines()
header = False
title = False
xnum = 1
ii = 1
for line in file:
    if line[0:2] == "X:":
        comped.append(line[0:2] + str(xnum) + "\n")
        header = True
        xnum += 1
    elif line[0:2] in valid_starts and header == True:
        comped[ii] += line
    elif header == True:
        comped[ii] += line + "\n"
        header = False
        ii += 1
    elif line[0:3] == "%%%":
        title ^= True      #Flips it to the opposite of the current state
    elif line[0:2] == "% ":
        if xnum == 1:
            comped.append("\n".join(titlelist).format(xnum=xnum, ttitle=line[2:-2]))
        else:
            comped.append("\n".join(titlelist).format(xnum=xnum, ttitle=line[2:-2]))
        xnum += 1
        ii += 1
    else:
        pass
    
    
if A4_printing == True:
    A6_page = 0
    num = 0
    A6_groupings = [[]]
    for tune in comped:             #Grouping A6 pages together in the knowlegde that four tunes fit per A6 page
        if "%%newpage" in tune or num >= 3:
            A6_groupings.append([])
            A6_groupings[A6_page+1].append(tune)
            A6_page += 1
            num = 0
        elif num < 3:
            A6_groupings[A6_page].append(tune)
            num += 1
    if len(A6_groupings)%8 != 0:
        for i in range(8-(len(A6_groupings)%8)):
            A6_groupings.append([])
    A6_groupings = A6_groupings[1:]
    A4_order = []
    A4_page = 0
    while A4_page*8 + 8 <= len(A6_groupings):
        for i in [0, 2, 4, 6, 3, 1, 7, 5]:
            A4_order.append(A6_groupings[A4_page*8 + i])
        A4_page += 1
    for i, page in enumerate(A4_order):
        A4_order[i] = "".join(page)
    out = "".join(A4_order)
else:
    out = "".join(comped)
    
f = open(pythonpath + "\\" + outfile, "x")
f.write(out)
f.close()
print("Finished")

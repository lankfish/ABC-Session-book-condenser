# -*- coding: utf-8 -*-

#%%Preamble

import re
import os

pythonpath = os.path.dirname(__file__)

#USER INPUTS
#Filename of file to condense (including .abc)
infile = "tune_book.abc"
#Filename of file to output to (including .abc)
outfile = "condensed_book.abc"

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
              "</div>\n"]

#Section titles
titlelist = ["\n%%newpage",
              "X:{tnum}",
              "%%titlefont Times-roman 40",
              "T:{ttitle}",
              "K:\n\n"]

#%%
out = "\n".join(formathead)
valid_starts = ["A:", "B:", "C:", "D:", "F:", "G:", "H:", "K:", "L:", "M:", "m:",
                "N:", "O:", "P:", "Q:", "R:", "r:", "S:", "s:", "T:", "U:", "W:",
                "w:", "X:", "Z:"]

f = open(pythonpath + "\\" + infile)
file = f.readlines()                 #Open and read file
header = False     #Is true when dealing with the header of a tune
title = False      #Is true when dealing with a section title
num = 1            #tune number, so they remain consistant even with adding section titles
for line in file:
    if line[0:2] == "X:":
        out += line[0:2] + str(num) + "\n"
        num += 1
        header = True
    elif line[0:2] in valid_starts and header == True:
        out += line
    elif header == True:
        out += line + "\n"
        header = False
    elif line[0:3] == "%%%":
        title ^= True      #Flips it to the opposite of the current state
    elif line[0:2] == "% " and title == True:
        out += "\n".join(titlelist).format(tnum=num, ttitle=line[2:-2])
        num += 1
    else:
        pass
    
f = open(pythonpath + "\\" + outfile, "x")
f.write(out)
f.close()
print("Finished")

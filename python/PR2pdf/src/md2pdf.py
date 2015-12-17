# encoding:utf-8

import markdown
import codecs
import os

# # # # # # # # # #
# This formula was found in a tap:
# Caskroom/cask/wkhtmltopdf
# To install it, run:
#  brew install Caskroom/cask/wkhtmltopdf
# # # # # # # # # #

encoding = 'UTF-8'

# filenames
in_filename = '../config/tmp.md'
out_filename = '../config/tmp.html'
pdf_filename = '../config/tmp.pdf'

# read .md
f_input = codecs.open(in_filename, 'r', encoding)
allLines = f_input.read()

# markdown -> html
md = markdown.Markdown()
html = md.convert(allLines)

# output .html
f_out = codecs.open(out_filename, 'w', encoding)
f_out.write(html)
f_out.close()

# html -> pdf
command = ('wkhtmltopdf', '--encoding utf-8', out_filename, pdf_filename)
os.system(" ".join(command))

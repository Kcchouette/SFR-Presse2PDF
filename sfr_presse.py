#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json, urllib, sys, re
from fpdf import FPDF
from PIL import Image
from pprint import pprint

def main():

    if len(sys.argv) >= 2:
        name = sys.argv[1]
    else:
        sys.exit(0)

    url = sys.argv[1]

    baseurl = re.sub('material\.json$', '', url)

    response = urllib.urlopen(url)
    data = json.loads(response.read())

    pdf = FPDF(unit = "pt", format = [data["pages"][0]["hd"]["width"], data["pages"][0]["hd"]["height"]])

    title = data["metadata"]["title"].encode('utf-8')
    number = str(data["metadata"]["issue_number"])
    lg = str(data["metadata"]["language_code"])
    dte = str(data["metadata"]["publication_date"])

    pdf.set_auto_page_break(False)
    pdf.set_margins(0, 0, 0)

    for page in data["pages"]:

		nb = 0
		col = 0
		row = 0

		pdf.add_page()
		
		for nb in range(page["hd"]["tile_col_count"] * page["hd"]["tile_row_count"]):
			
			image_init = (100 * col) + (1 * row)

			image_number = remplirZero(image_init)

			name_file = str(page["number"]) + "_" + image_number + ".jpeg"

			with open(name_file, 'wb') as f:

				f.write(urllib.urlopen(baseurl + page["hd"]["path"] + "/tile" + image_number + ".jpeg").read())
				f.close()
				pdf.image(name_file, x=col*page["hd"]["tile_width"] , y=row*page["hd"]["tile_height"] , type = 'JPEG')

				if (nb+1) % page["hd"]["tile_col_count"] == 0:
					col = 0
					row += 1
				else:
					col += 1

    pdf.output(title + " N " + number + "_" + lg + "_" + dte + ".pdf", "F")

def remplirZero(number):
	if len(str(number)) == 1:
		return "00x0" + str(number)
	if len(str(number)) == 2:
		return "00x" + str(number)
	if len(str(number)) == 3:
		return "0" + str(number)[0] + "x" + str(number)[1] + str(number)[2]
	if len(str(number)) == 4:
		return str(number)[0] + str(number)[1] + "x" + str(number)[2] + str(number)[3]

if __name__ == '__main__':
    main()

from PyPDF2 import PdfFileWriter, PdfFileReader
import io, os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# replace string below with file path to folder containing the original brew sheet pdf
file_path = "C:\\FILE\PATH\TO\BREW\SHEET\FOLDER"
# replace defaults below according to preferences and order of fields listed starting on line 21
defaults = ["Sean Keenan", "", "", "", 
		"25 L", "60 mins", "", "70%", "", "", 
		"", "", "", "", "", "", ""]

# coordinates for ingredients, mash, and hops pdf fields
ingredients_space = [40, 225]
mash_space = [300, 465, 515]
hops_space = [40, 120, 170, 220]

# fields - change "hasDefault" to True if you want the command line to provide a default option,
# False if you don't want a default option to be displayed in the command line
brewer = {"hasDefault": True, "hasMultiple": False, "pos": (120, 677)}
recipe_name = {"hasDefault": False, "hasMultiple": False, "pos": (390, 677)}
brew_date = {"hasDefault": False, "hasMultiple": False, "pos": (120, 661)}
beer_type = {"hasDefault": False, "hasMultiple": False, "pos": (390, 661)}
batch_size = {"hasDefault": True, "hasMultiple": False, "pos": (120, 645)}
boil_time = {"hasDefault": True, "hasMultiple": False, "pos": (235, 645)}
batch_num = {"hasDefault": False, "hasMultiple": False, "pos": (395, 645)}
exp_efficiency = {"hasDefault": True, "hasMultiple": False, "pos": (525, 645)}
ingredients = {"hasDefault": False, "hasMultiple": True, "pos": (40, 583)}
hops = {"hasDefault": False, "hasMultiple": True, "pos": (40, 405)}
mash_info = {"hasDefault": False, "hasMultiple": True, "pos": (300, 583)}
yeast_type = {"hasDefault": False, "hasMultiple": False, "pos": (470, 421)}
exp_og = {"hasDefault": False, "hasMultiple": False, "pos": (230, 294)}
exp_fg = {"hasDefault": False, "hasMultiple": False, "pos": (230, 277)}
exp_abv = {"hasDefault": False, "hasMultiple": False, "pos": (230, 260)}
ibus = {"hasDefault": False, "hasMultiple": False, "pos": (230, 243)}
srm = {"hasDefault": False, "hasMultiple": False, "pos": (230, 226)}
inputs = {"brewer": brewer,
	  "recipe name": recipe_name,
	  "brew date": brew_date,
	  "beer type": beer_type,
	  "batch size": batch_size,
	  "boil time": boil_time,
	  "batch #": batch_num,
	  "exp. efficiency": exp_efficiency,
	  "ingredients": ingredients,
	  "hops": hops,
	  "mash info": mash_info,
	  "yeast type": yeast_type,
	  "exp. OG": exp_og,
	  "exp. FG": exp_fg,
	  "exp. ABV": exp_abv,
	  "IBUs": ibus,
	  "SRM": srm
}

packet = io.BytesIO()
canv = canvas.Canvas(packet, pagesize = letter)

# command line logic
for i, (key, value) in enumerate(inputs.items()):
	data_arr = []		
	if (value["hasDefault"] and not value["hasMultiple"]):
		user_input = input("{} (0 for default '{}'): ".format(key, defaults[i]))
	elif (value["hasMultiple"]):
		if key is "ingredients":
			while (user_input != "n"):
				data_arr.append(input("ingredient type: "))
				data_arr.append(input("amount: "))
				user_input = input("keep going? (y/n): ")
			user_input = ""
		elif key is "hops":
			while (user_input != "n"):
				data_arr.append(input("hop type: "))
				data_arr.append(input("amount: "))
				data_arr.append(input("AA %: "))
				data_arr.append(input("boil time: "))
				user_input = input("keep going? (y/n): ")
			user_input = ""
		else:
			while (user_input != "n"):
				data_arr.append(input("mash type: "))
				data_arr.append(input("temp: "))
				data_arr.append(input("time: "))
				user_input = input("keep going? (y/n): ")
			user_input = ""
	else:
		user_input = input("{}: ".format(key))
	
	if user_input is "0":
		user_input = defaults[i]
	elif (user_input == "end"):
		break

	if not data_arr:
		canv.drawString(value["pos"][0], value["pos"][1], user_input)
	else:
		if (key == "ingredients"):
			height = value["pos"][1]
			for counter, item in enumerate(data_arr):
				canv.drawString(ingredients_space[counter%2], height, item)
				if counter%2:
					height -= 17
		elif (key == "hops"):
			height = value["pos"][1]
			for counter, item in enumerate(data_arr):
				canv.drawString(hops_space[counter%4], height, item)
				if ((counter+1)%4 == 0 and counter != 0):
					height -= 17
		else:
			height = value["pos"][1]
			for counter, item in enumerate(data_arr):
				canv.drawString(mash_space[counter%3], height, item)
				if ((counter+1)%3 == 0 and counter != 0):
					height -= 17

canv.save()

packet.seek(0)
new_pdf = PdfFileReader(packet)
os.chdir(file_path)
# change "original_brew_sheet.pdf" to the name of your brew sheet pdf
existing_pdf = PdfFileReader(open("original_brew_sheet.pdf", "rb"))
output = PdfFileWriter()
page = existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)
# change "destination.pdf" to the name of your desired new pdf
outputStream = open("destination.pdf", "wb")
output.write(outputStream)
outputStream.close()

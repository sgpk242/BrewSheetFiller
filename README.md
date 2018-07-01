# BrewSheetFiller
Command-line python program to digitally fill out [Brewer's Friend recipe sheet](https://www.brewersfriend.com/brewday-allgrain/), instead of using an online PDF editor. 

***To install:***

Save file on your computer wherever your want. Several things in the code will need to be editted to suit your needs:
1. Change default field options
2. Change name of original Brewer's Friend PDF
3. Change name of new PDF (needs to be edited each time or the new PDF will be overwritten)

See the code for commented tips. 

Finally, install the PyPDF2 and reportlab packages using your command line package manager. 

e.g. on Windows, type ```pip install PyPDF2 reportlab```

***To run:***

Navigate to the folder containing brewSheetFiller.py. Type ```python brewSheetFiller.py``` and fill out the fields, pressing "return" to enter a blank space or to move to the next field, or typing ```0``` to fill in the default option.  

***Note:***

This tool does not fill out the Water, Yeast, Cost, Hydrometer Readings, or Notes sections, because I typically fill these out by hand on brew day. This feature could be easily coded by the user if desired. 

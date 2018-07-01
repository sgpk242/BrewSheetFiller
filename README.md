# BrewSheetFiller
Command-line python program to fill out [Brewer's Friend recipe sheet](https://www.brewersfriend.com/brewday-allgrain/)

***To install:***

Save file on your computer wherever your want. Several things in the code will need to be editted to suit your needs:
1. Change default field options
2. Change name of original Brewer's Friend pdf
3. Change name of new pdf (needs to be edited each time or the new pdf will be overwritten)

See the code for commented tips. 

Finally, install the PyPDF2 and reportlab packages using your command line package manager. 

e.g. on Windows, type ```pip install PyPDF2 reportlab```

***To run:***

Navigate to the folder containing brewSheetFiller.py. Type ```python brewSheetFiller.py``` and fill out the fields, pressing "return" to enter a blank space or to move to the next field, or typing ```0``` to fill in the default option.  

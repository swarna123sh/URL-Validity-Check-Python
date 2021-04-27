import validators
import urllib.request
from prettytable import PrettyTable
import details
# Create instance of PrettyTable
x = PrettyTable()

''' CHECK THE URL'''
# Create table with columns to record pf URLs
x.field_names = ["URL", "STATUS"]
for i in details.urlc:
  urlchk=validators.url(i)
  if not urlchk:    
    x.add_row([i, "Invalid URL"])
  else:
    # Try opening the URL
    try:
      z = urllib.request.urlopen(i)    
    # Catching the exception generated     
    except Exception as e :      
      x.add_row([i, str(e)])
    else:
      x.add_row([i, "Valid URL"])  
print(x)
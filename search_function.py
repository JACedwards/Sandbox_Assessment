
import pandas as pd

def search(first_name=None, last_name=None, address=None, tax_id=None):    
   
   #Convert csv file to pandas dataframe
   df = pd.read_csv('people.csv')

   # create filter variables:
     # (preface first two filters variables with conditionals
        # to avoid throwing "NoneType has no attribute .title()" error if parameter = None)

   if first_name != None:
      is_first = df['First Name'] == first_name.title()
   if last_name != None:
      is_last = df['Last Name'] == last_name.title()
   is_address = df['Address'] == address
   is_tax_id = df['Tax ID'] == tax_id

   #if any of the parameters = None,
   #  reset filter variable so that any parameter = None does NOT filter out
   #  any rows
   if first_name == None:
      is_first = df['First Name'] != first_name
   if last_name == None:
      is_last = df['Last Name'] != last_name
   if address== None:
      is_address = df['Address'] != address
   if tax_id == None:
      is_tax_id = df['Tax ID'] != tax_id

   #create filtered dataframe
   df_filtered = df[is_first & is_last & is_address & is_tax_id]
   
   #convert dataframe to list of dictionaries
   output = df_filtered.to_dict(orient='records')
   
   return output

#(I didn't copy down all of the test cases, but I think the calls below recreate most of them)

print(search())
# print(search(last_name='macho'))
# print(search(last_name='macho', address='123 Harvard Ave, Somerville, MA, 02114'))
# print(search(first_name='MaNny', last_name='macho', address='123 Harvard Ave, Somerville, MA, 02114'))
# print(search(first_name='DIANE', last_name='MaCho', address='45551 Gregor St, Lexington, KY, 14567', tax_id=435234511.0))

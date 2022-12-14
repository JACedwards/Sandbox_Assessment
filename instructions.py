# # Implement a Python 3 search function that accepts keyword arguments of type str that represent search criteria and returns a list of dict objects that represent person records that match the input criteria. This search function should operate on the person CSV data set contained in /home/coderpad/data/people.csv. Omitted keyword arguments (i.e. arguments with None values) for a given invocation should not exclude records in the returned person list. This means that search should return the entire list of person records when no parameters are passed.

# # The algorithm in search should use CASE INSENSITIVE string matching to determine if person records should be included in the result list.

# # The people CSV file contains a header row that should be excluded from search results. However, you should still review the header row to understand the ordering of the comma-separated data in the record.

# # For convenience, here is the content of /home/coderpad/data/people.csv:

# # First Name,Last Name,Address,Tax ID
# # Boris,Lincoln,"111 Haskell Hall, Medford, MA 02155",321659876
# # Donna,Lincoln,"111 Haskell Hall, Medford, MA 02155",334561468
# # Manny,Macho,"123 Harvard Ave, Somerville, MA, 02114",387123897
# # Sara,Macho,"123 Harvard Ave, Somerville, MA, 02114",881234987
# # Chris,Macho,"123 Harvard Ave, Somerville, MA, 02114",236748281
# # Diane,Macho,"45551 Gregor St, Lexington, KY, 14567",435234511
# # Jim,Smith,"513 Dang Lane, Champaign, IL, 61844",742245736
# # Richard,Smith,"198 Rail St, Moline, IL, 61833",234580298
# # Richard,Fox,"500 Large Court, Moline, IL 61833",924620110
# # Sample return values can be discerned by examining the assert statements at the end of this problem’s code buffer. If search is correctly implemented, the assert statements should all pass (i.e. not raise an AssertionError).

# # HINT 1: Use Python 3’s built-in csv module or pandas to parse the people CSV file.

# # HINT 2: Start solving this problem by examining the content of people CSV file (its content is shown above) and the assert statements in the code buffer — this will further clarify the requirements.
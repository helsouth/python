import re
import pandas as pd

# Load the data file where pydump.txt is the output of pysecrets users.pwdump renamed to pydump.txt
with open("pydump.txt", "r") as file:
    data = file.read()
# Patterns to search in each block
patterns = {
    "DistinguishedName": r"DistinguishedName: (.+)",
    "SamAccountName": r"SamAccountName: (\S+)",
    "SID": r"Sid: (\S+)",
    "SamAccountType": r"SamAccountType: (\S+)",
    "Flags": r"Flags: (\d+)",
    "WDigest_Hash_01": r"Hash 01: (\S+)",
    "Salt": r"Salt: (\S+)",
    "DefaultIterationCount": r"DefaultIterationCount: (\d+)"
}

# Split on blank lines - remove leading/trailing whitespace. splits using double newline. 
# re.search finds specific information and retrieves for each group. regular expression checks for a match on each and assigns value or none
# user = {}  creates empty dictionary for each user to store parsed information
# users.append(user) appends the completed block to the user list

# Parse the data
users = [
    {key: (match.group(1) if (match := re.search(pattern, block)) else None)
     for key, pattern in patterns.items()}
    for block in data.strip().split("\n\n")
]

# Uses Pandas library to Convert list of user libraries to a DataFrame for tabulation
df = pd.DataFrame(users)

# Print the table (datea frame) to console
print(df) 

# Save the dataframe as CSV. index=false removes the data frames row labels (line numbers) 
df.to_csv("user_table_detailed.csv", index=False)


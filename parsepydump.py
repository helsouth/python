import re
import pandas as pd

# Load the data file
with open("pydump.txt", "r") as file:
    data = file.read()

# Parse the data
users = []
for block in data.strip().split("\n\n"):  # Split on blank lines
    user = {}
    user["DistinguishedName"] = re.search(r"DistinguishedName: (.+)", block).group(1) if re.search(r"DistinguishedName: (.+)", block) else None
    user["SamAccountName"] = re.search(r"SamAccountName: (\S+)", block).group(1) if re.search(r"SamAccountName: (\S+)", block) else None
    user["SID"] = re.search(r"Sid: (\S+)", block).group(1) if re.search(r"Sid: (\S+)", block) else None
    user["SamAccountType"] = re.search(r"SamAccountType: (\S+)", block).group(1) if re.search(r"SamAccountType: (\S+)", block) else None
    user["Flags"] = re.search(r"Flags: (\d+)", block).group(1) if re.search(r"Flags: (\d+)", block) else None
    user["WDigest_Hash_01"] = re.search(r"Hash 01: (\S+)", block).group(1) if re.search(r"Hash 01: (\S+)", block) else None
    user["Salt"] = re.search(r"Salt: (\S+)", block).group(1) if re.search(r"Salt: (\S+)", block) else None
    user["DefaultIterationCount"] = re.search(r"DefaultIterationCount: (\d+)", block).group(1) if re.search(r"DefaultIterationCount: (\d+)", block) else None
    users.append(user)

# Convert to a DataFrame for tabulation
df = pd.DataFrame(users)

# Print the table
print(df)

# Save as CSV
df.to_csv("user_table_detailed.csv", index=False)


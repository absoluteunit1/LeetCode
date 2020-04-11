
# Using replace()
def defangIPAddr(address):
    return address.replace(".", "[.]")

# Recursively
def defangIPAddr2(address):
    if len(address) == 1:
        return address[0]
    elif address[0] == ".":
        return "[" + address[0] + "]" + defangIPAddr2(address[1:])
    return address[0] + defangIPAddr2(address[1:])

# Iteratively
def defangIPAddr3(address):
    return "".join(["[.]" if i == "." else i for i in address])


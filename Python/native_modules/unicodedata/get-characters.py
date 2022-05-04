from unicodedata import name
"""
Get different signs from unicodedata.name
"""
print({(chr(j)) for j in range(256) if 'SIGN' in name(chr(j), '')})

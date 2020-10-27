from unicodedata import normalize
"""
Normalize words with accents
using unicodedata.normalize
"""
s1 = 'caféteria'
s2 = 'cafe\u0301teria'  # é

print(f"""Before transforming/normalizing
{s1=} {s2=}
Lengths: {len(s1)} {len(s2)}""")

# Types of normalization ['NFC', 'NFD']
print(f"""After transforming/normalizing
{normalize('NFC',s1)} {normalize('NFC',s2)}
Lengths: {len(s1)} {len(s2)}""")

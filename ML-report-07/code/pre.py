pairs = [[normalizeString(s) for s in l.split('\t')[:2]] for l in lines]
# split the input words in pairs
def normalizeString(s):
   s = s.lower().strip()
   if ' ' not in s:
       s = list(s)
       s = ' '.join(s)
   s = unicodeToAscii(s)
   s = re.sub(r"([.!?])", r" \1", s)
   return s
#import re
# def palindroma(ch):
#   return True if ch == ch[::-1] else False
# def only_text(ch):
#   return ''.join(filter(str.isalpha, ch)) if not ch.isalpha() else ch #re.sub(r'[^a-zA-Z]', '', ch)
# ch = only_text(input("Inserisci una stringa ---> ").replace(" ", "").lower())
# print(f"La parola {ch} e palindroma ? {palindroma(ch)}")

#seconda versione
import re
def palindroma(ch):
  reverse = ch[::-1]
  if ch == reverse:
    return True
  return False

def only_text(ch):
  if not ch.isalpha():
    ch = re.sub(r'[^a-zA-Z]', '', ch)
    #ch = ''.join(filter(str.isalpha, ch))
  return ch

ch = input("Inserisci una stringa ---> ").replace(" ", "").lower()
ch = only_text(ch)
print(f"La parola {ch} e palindroma? {palindroma(ch)}")


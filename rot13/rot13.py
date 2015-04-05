
def rot13_char(ch):
  if not ch.isalpha():
    return ch

  ch_low = ch.lower()
  if ch_low <= 'm':
    dist = 13
  else:
    dist = -13
  return chr(ord(ch) + dist)

def rot13(s):
  return ''.join( rot13_char(ch) for ch in s )

if __name__ == '__main__':
  try:
    while True:
      print rot13(raw_input())
  except KeyboardInterrupt:
      print 'Bye!'
    

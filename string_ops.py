def find_nth_occurrence(substring, string, occ=1):
  try:
    string ="This is an example. Return the nth occurrence of example in this example string."

    x = string.split(substring,occ)
    
    if len (x)<= occ:
        return -1
    else:
        return len (string) - len(x[-1]) - len (substring)
  except:
    print('try again')
find_nth_occurrence("example", string, 2)


#################
 def solve(a, b):
  try:
    if a == b:
        return True
    elif a== '*':
        return True
    elif '*' not  in a:
        return False
    
    elif len(a)-1 <= len (b):
        x = a.split('*')
        x[0] in b and x[1] == b[:-1]
        return True
    else:
        return False
  except:
    print('try again')
solve("code*warr", "codeswarr") 


##################3
def is_palindrome (s):
  try:
    x =s.lower()
    print(x)
    if x == x[::-1]:
        return True
    else:
        return False
  except:
    print('try again')
is_palindrome("sdsdsd")
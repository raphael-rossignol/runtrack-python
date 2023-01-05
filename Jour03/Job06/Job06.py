string = "abcdefghijklmnopqrstuvwxyz" * 10
n = len(string)
level = 0
while n > 0:
  count = 2 ** level
  if n >= count:
    print(string[:count])
  else:
    if level % 2 == 0:
      print(string)
    else:
      print(string[::-1])
  string = string[count:]
  n = len(string)
  level += 1

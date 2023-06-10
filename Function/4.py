def function_name(string):
  upper = 0
  lower = 0
  for i in string:
    if i.islower():
      lower += 1
    elif i.isupper():
      upper += 1
  print(f'No. of Uppercase Characters : {upper}')
  print(f'No. of Lowercase Characters : {lower}')
function_name('The quick Sand Man')
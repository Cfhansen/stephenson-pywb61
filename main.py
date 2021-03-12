def get_more_values():
  print('Enter a value:')
  return int(input())

results = []

print('Enter a value:')
val_ = int(input())
results.append(val_)

if val_ == 0:
  print('I can\'t average that.')

while val_ != 0:
  val_ = get_more_values()
  results.append(val_)

if len(results) > 1:
  print(sum(results) / (len(results) - 1))

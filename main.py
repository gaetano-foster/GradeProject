categories = {
  'Participation': 0.1,
  'Homework': 0.2,
  'Test': 0.4,
  'Quiz': 0.3
}

grades = {
  'Participation': 1.0,
  'Homework': 1.0,
  'Test': 1.0,
  'Quiz': 1.0
}

def utils_isfloat(str):
  try:
    float(str)
    return True
  except ValueError:
    return False

def check_categories():
  sum = 0
  for key, value in categories.items():
    sum += value
    
  if sum != 1.0:
    return False
  else:
    return True

def category_add(args):
  if not utils_isfloat(args[1]):
    print('Error: Invalid Syntax\n' + args[0] + ' --->' + args[1] + '<--- ' + args[2] + '\nArgument 2 must be a decimal number! (I.E. 0.1)')
    return False
  weight = float(args[1])
  title = args[2]
  
  if weight > 1 or weight <= 0:
    print('Error: Weight must be between 0 and 1.')
    return False
  categories[title] = weight
  grades[title] = 1.0
  
  i = 0
  for key, value in categories.items():
    i += value
    
  if i != 1:
    print('Warning: Weights do not add up to 1.\n' + 'Current sum: ' + str(i) + '\nCategories: ')
    for key, value in categories.items():
      print(key + ' Weight: '  + str(value))
    print('It is recommended that you modify some values to make sure the sum of all weights is equal to 1 using the MODIFY command.')

def category_modify(args):
  if args[2] == 'weight':
    if not utils_isfloat(args[3]):
      print('Error: Invalid Syntax\n' + args[0] + ' ' + args[1] + ' ' + args[2] + ' --->' + args[3] + '<---' + '\nArgument 3 must be a decimal number! (I.E. 0.1)')
      return False
    weight = float(args[3])

    if args[1] not in categories:
      print('Error: There is no category with title "' + str(args[1]) + '".')
      return False
    categories[args[1]] = weight
    return True

  if args[2] == 'name':
    if args[1] not in categories or args[1] not in grades:
      print('Error: There is no category with title "' + str(args[1]) + '".')
      return False
    categories[args[1]] = args[3]
    grades[args[1]] = args[3]
    return True

def put_grades(args):
  g = []
  for n in args:
    if not utils_isfloat(n):
      continue
    else:
      g.append(float(n))

  if args[1] not in grades:
    print('Error: There is no category with title "' + str(args[1]) + '".')
    return False
  grades[args[1]] = sum(g) / len(g)
  print(grades[args[1]])
  return True

def process_command(args):
  cmd = args[0]
  if cmd == 'add':
    category_add(args)
  if cmd == 'modify':
    category_modify(args)
  if cmd == 'put_grade':
    put_grades(args)

process_command(['grade', 'Participation', 1.0, 0.5, 0.8, 0.2, 1.0, 1.0, 1.0, 1.0])
#process_command(['add', '1.0', 'Exam'])
#print('\n\n\n')
#process_command(['modify', 'Exam', 'weight', '0.2'])
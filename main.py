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

q = 1

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
    categories[args[3]] = categories.pop(args[1])
    grades[args[3]] = grades.pop(args[1])
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
  print('Put grade ' + str(grades[args[1]]) + ' in ' + args[1] + '.')
  return True

def quarter(args):
  if not args[1].isdigit():
    print('Error: Please input a number.')
    return False
  q = int(args[1])
  return True
  
def total_grade(args):
  for key, value in categories.items():
    print(key + ' Weight: ' + str(value))
  
  print('\n')
  
  for key, value in grades.items():
    print(key + ' Grade: ' + str(value))
  
  weighted_grades = []
  for key, value in grades.items():
    weighted_grades.append(value * categories[key])
  
  final_grade = sum(weighted_grades)
  print('Final Quarter ' + str(q) + ' Grade: ' + str(final_grade))

def cmd_help():
  print('Commands:\n')
  print('add [weight] [category name]: add a new category\n')
  print('modify [category name] [mode (weight or name)] [value]: modify the name or weight of a category\n')
  print('put [category] [...grades...]: puts in the grades for a given category. Any amount of grades can be inputted.\n')
  print('quarter [number]: changes what quarter the grades are for.\n')
  print('grades: print the final grades and weights.\n')
  print('help: display all commands\n')
  print('stop: exit program\n')
  
def stop():
  print('Goodbye!')
  quit()
  

def process_command(args):
  cmd = args[0]
  print(cmd)
  if cmd == 'add':
    category_add(args)
    return
  if cmd == 'modify':
    category_modify(args)
    return
  if cmd == 'put':
    put_grades(args)
    return
  if cmd == 'quarter':
    quarter(args)
    return
  if cmd == 'grades':
    total_grade(args)
    return
  if cmd == 'help':
    cmd_help()
    return
  if cmd == 'stop':
    stop()
    return
  else:
    print('Unknown command: "' + cmd + '" is undefined.')

def main():
  print('====Command Line Grader====')
  print('Type "help" if you need it!')
  print('===========================')
  while True: # This is ok because there is a stop command to manually exit
    raw_in = input('>>')
    process_command(raw_in.split())

if __name__ == '__main__':
    main()

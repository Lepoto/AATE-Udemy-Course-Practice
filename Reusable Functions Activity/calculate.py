def perform_calculation(number_one, number_two, operator):
  if operator == "+":
    return number_one + number_two
  elif operator == '-':
    return number_one - number_two
  elif operator == '*':
    return number_one * number_two
  elif operator == '/':
    return number_one / number_two
  else:
    return "Invalid operator"

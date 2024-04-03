import time

ingredients = ['eggs', 'flour', 'sugar', 'butter', 'chocolate', 'milk']
score = 0

print("Hello, you have to guess 3 ingredients from the cookies recipe, ready?")
time.sleep(2)

for i in range(3):
  ingredient = input("Ingredient " + str(i + 1) + "? ")
  if ingredient in ingredients:
    print("You have correctly guessed " + ingredient)
    score += 1
  else:
    print("Uh oh, wrong guess!")

print("Game over, you have " + str(score) + " points out of 3")

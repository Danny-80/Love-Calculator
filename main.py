
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")



both_names = (name1 + name2).lower()

letters_true = ['t','r','u','e']
letters_love = ['l','o','v','e']

count_true = 0
count_love = 0

for letter in letters_true:
  x = both_names.count(letter)
  count_true += x
  

for letter in letters_love:
  x = both_names.count(letter)
  count_love += x


love_score = str(count_true) + str(count_love)
love_score_int = int(love_score)


if love_score_int < 10 or love_score_int > 90:
  print(f'Your love score is {love_score_int}, you go together like coke and mentos.')
elif love_score_int > 40 or love_score_int < 50:
  print(f'Your love score is {love_score_int}, you are allright together.')
else:
  print(f'Your love score is {love_score_int}.')

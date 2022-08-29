import re

def passwordValidator(user_input):
  while True:
    is_valid = False

    if (len(user_input)<6 or len(user_input)>12):
      print("Not valid ! Total characters should be between 6 and 12")
      break
    elif not re.search("[A-Z]",user_input):
      print("Not valid ! It should contain atleast one Capital letter.")
      break
    elif not re.search("[a-z]",user_input):
      print("Not valid ! It should contain atleast one Samll letter")
      break
    elif not re.search("[1-9]",user_input):
      print("Not valid ! It should contain atleast one number between 1 to 9")
      break
    elif not re.search("[@#$]",user_input):
      print("Not valid ! It should contain at least one letter in [@#$]")
      break
    elif re.search("[\s]",user_input):
      print("Not valid ! It should not contain any space")
      break
    else:
      is_valid = True
      break

  if(is_valid):
    print("Password is valid")

if __name__ == '__main__':
  while True:
    passwordValidator(input("\nEnter Your Password: "))
    if(input("Again [y/n] ").lower() == 'n'):
      break
  print("\nBye")
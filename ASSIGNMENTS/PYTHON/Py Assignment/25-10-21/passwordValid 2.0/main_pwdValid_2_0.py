import re

def passwordValidator(user_input):
  while True:
    is_valid = False

    if (len(user_input)<6 or len(user_input)>12):
      break
    elif not re.search("[A-Z]",user_input):
      break
    elif not re.search("[a-z]",user_input):
      break
    elif not re.search("[1-9]",user_input):
      break
    elif not re.search("[@#$]",user_input):
      break
    elif re.search("[\s]",user_input):
      break
    else:
      is_valid = True
      break

  if(is_valid):
    return True
  else:
      return False

if __name__ == "__main__":
    passwords_ls = input("Enter Your All Passwords with separated Comma: ").split(",")
    with open('password_output.txt',"w") as op_file:
        for pwd in passwords_ls:
            if passwordValidator(pwd):
                op_file.write(pwd)
                op_file.write('\n')
    print('Succesfully Completed')






def command_menu():
    print("\nCOMMAND MENU")
    print("\nlist - List All Movies\nadd - dd a Movie"
          "\ndel - Delete a Movie\nexit - Exit Program")



movie_list = ["Nayagan", "Mahanadhi", "Apoorva Sagodharargal",
              "Thevar Magan", "Guna", "Virumaandi"
              "Aalavandan"]

def list_movie():
    i = 1
    for movie in movie_list:
        print(f"{i}.{movie}.")
        # print(" ",i,".",movie)
        i += 1

def add_movie():
    add_list = input("Name: ")
    movie_list.append(add_list)
    print(f"{add_list} was added.")

def del_movies():
    num_del = int(input("Number: "))
    del_list_name = movie_list[num_del - 1]
    movie_list.pop(num_del - 1)
    print(f"{del_list_name} was deleted.")


def main():
    command_menu()
    while True:
        command = input("\nCommand: ").lower()
        if command == 'list':
            # i = 1
            # for movie in movie_list:
            #     print(f"{i}.{movie}.")
            #     i+=1
            list_movie()
        elif command == "add":
            # add_list = input("Name: ")
            # movie_list.append(add_list)
            # print(f"{add_list} was added.")
            add_movie()
        elif command == "del":
            # num_del = int(input("Number: "))
            # del_list_name = movie_list[num_del-1]
            # movie_list.pop(num_del-1)
            # print(f"{del_list_name} was deleted.")
            del_movies()
        elif command == 'exit':
            print("Bye!")
            break
        else:
            print("INVALID INPUT")

if __name__ == '__main__':
    main()





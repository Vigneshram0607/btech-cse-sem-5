try:
    letters = digits = symbols = 0

    with open("input.txt","r") as ip_file:
        sentence = ip_file.read()
        # print(sentence)
        for i in range(len(sentence)):
            if(sentence[i].isalpha()):
                letters+=1
            elif(sentence[i].isdigit()):
                digits+=1
            else:
                symbols+=1

    with open("output.txt","w") as op_file:
        op_data = 'LETTERS: '+str(letters)+"\nDIGITS: "+str(digits)+"\nSYMBOLS: "+str(symbols)
        # print(op_data)
        op_file.write(op_data)
    print("SUCCESSFULLY COMPLETED")

except FileNotFoundError:
    print("FILE NOT FOUND")

except Exception:
    print("UNKNOWN EXCEPTION")
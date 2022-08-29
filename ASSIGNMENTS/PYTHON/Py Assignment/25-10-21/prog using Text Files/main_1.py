try:
    ip_file = open("input.txt","r")
    ip_data = ip_file.read()
    # print(ip_file.read())
    print(ip_data)
    # ip_data = ip_data.split(',')
    # ip_data_sorted = sorted(ip_data)
    # op_file = open("output.txt","w")
    # op_file.write((',').join(ip_data_sorted))
    # op_file.close()
    print("Successfully Completed")
except FileNotFoundError:
    print("FILE NOT FOUND")
except Exception:
    print("UNKNOWN EXCEPTION")

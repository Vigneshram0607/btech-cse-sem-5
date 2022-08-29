with open('freq_input.txt','r') as ip_file:
    ip_data = ip_file.read().split(' ')
ip_data_dup = []
with open("freq_output.txt","w") as op_file:
    for data in sorted(ip_data):
        op_data = data +' : '+ str(ip_data.count(data)) + '\n'
        if data not in ip_data_dup:
            ip_data_dup.append(data)
            op_file.write(op_data)

print("SUCCESSFULLY COMPLETED")

import csv

FILENAME = 'trip_data.csv'

def readTripFile():
    with open(FILENAME, 'r') as trip_file:
        file_reader = csv.reader(trip_file)
        for data in file_reader:
            print("{:15} {:10} {:10}".format(data[0], data[1], data[2]))
    print('\n')

def writeTripFile(distance, gallons):
    data_row = [dist_input, gallons_input, round(dist_input / gallons_input, 2)]
    with open(FILENAME, 'a') as trip_update_data:
        csv_write = csv.writer(trip_update_data)
        csv_write.writerow(data_row)
    print('\n')


if __name__ == "__main__":
    print("The Miles Per Gallon program")
    readTripFile()
    again = True
    while again:
        dist_input = int(input("{:25}".format("Enter Miles driven:")))
        gallons_input = int(input("{:25}".format("Enter Gallons Of Gas:")))
        mpg_calc = print("{:25} {:1}".format("Miles Per Gallon:", (round(dist_input/gallons_input, 2))))
        writeTripFile(distance= dist_input, gallons= gallons_input)
        readTripFile()
        if(input('More Entries [y/n]: ').lower() == 'n'):
            again = False
    print('Bye')




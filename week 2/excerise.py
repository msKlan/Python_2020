import csv
import argparse

# 1.a


def print_file_content(file):
	with open(file, 'r') as file:
		reader = csv.reader(file)
		for row in reader:
			print(row)
   
#print_file_content('random_csv_file.csv')


#1.b
listOfTuple = ("i", "do", "not", "care")


def write_list_to_file(output_file, lst):
    with open("output_file", "w") as f:
    	for i in listOfTuple:
       		f.write(i+"\n")
         
#write_list_to_file("output.csv", listOfTuple)
         
def write_items_to_file(output_file, *items):
    with open("outputfile.csv", "w") as f:
    	for x in items:
       		f.write(x+"\n")
        

#write_items_to_file("output.csv", "hej", "halløj", "hey")

#1.c

def read_csv(file):
    with open(file, "r") as f:
        reader = csv.reader(f)
        return list(reader)
        #data = list(reader)
        #print(data)
    
#read_csv("random_csv_file.csv")

#2.a
def write_list_to_csvfile(output_file, lst):
    with open(output_file, "w") as f:
       wr=csv.writer(f)
       wr.writerows(lst)


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="read and print file to console or to another file")
	parser.add_argument("csv", help="input csv file")
	parser.add_argument("--file", help = "print csv file to console")
	args = parser.parse_args()
	print(args)
	

	data = read_csv(args.csv)
 
	if args.file == None:
		print(data)
	else:
		write_list_to_csvfile(args.file, data)
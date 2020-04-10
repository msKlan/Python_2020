import argparse
from sys import argv
import os.path
from os import path


def write_list_to_file(output_file, lst):
    with open(output_file, "w") as f:
    	for i in lst:
       		f.write(i+"\n")

def list_files_in_folder(path, output):
    filer = os.listdir(path)
    write_list_to_file(output, filer)

def list_files_in_folder_recursive(root):
	for dirName, subdirList, fileList in os.walk(root):
		print("Found directory. %s" % dirName)
		for fname in fileList:
			print("\t%s" % fname)

def print_first_line_of_files(files):
	for file in files:
		with open(file, "r") as f:
			l = f.readline()
			print("File: %s - First line: %s" % (file, l))

def print_emails(files):
	for file in files:
		with open(file, "r") as f:
			for line in f:
				if "@" in line:
					print("File: %s - Email: %s" % (file, line))


def write_headlines(files):
	for file in files:
		with open(file, "r") as f:
			for line in f:
				if line[0]=="#":
					print("File: %s - Headline: %s" % (file, line))

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="read and print file to console or to another file")
	parser.add_argument("--list_files_in_folder", nargs=2, help="Folder bare folder")
	parser.add_argument("--list_files_in_folder_recursive", help="Folder bare folder")
	parser.add_argument("--print_first_line_of_files", nargs="*", help="Folder bare folder")
	parser.add_argument("--print_emails", nargs="*", help="Folder bare folder")
	parser.add_argument("--write_headlines", nargs="*", help="Folder bare folder")
   
	args = parser.parse_args()
	print(args)
 
	if args.list_files_in_folder:
  		list_files_in_folder(args.list_files_in_folder[0], args.list_files_in_folder[1])
	elif args.list_files_in_folder_recursive:
	  	list_files_in_folder_recursive(args.list_files_in_folder_recursive)
	elif args.print_first_line_of_files:
	  	print_first_line_of_files(args.print_first_line_of_files)
	elif args.print_emails:
	  	print_emails(args.print_emails)
	elif args.write_headlines:
	  	write_headlines(args.write_headlines)
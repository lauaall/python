# Remove specified extension from files in a directory
import os

def main():
    directory = input("Enter a directory: ")
    extension = input("Enter a file extension(without .): ")
    os.chdir(directory)
    files = os.listdir(directory)
    for file in files:
        if file.endswith("." + extension):
            new_file = file[:-4]
            os.rename(file, new_file)
            print("Renamed {} to {}".format(file, new_file))
    print("")
    print("Done!")
main()
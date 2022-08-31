# Remove specified extension from files in a directory
import os

def main():
    print("------------------------------")
    print("Custom Extension Remover")
    print("Created by lauaall")
    print("------------------------------")
    directory = input("Enter a directory: ")
    if directory == "" :
        print("")
        print("Error!, No directory specified.")
        exit()
    extension = input("Enter a file extension(without .): ")
    if extension == "" :
        print("")
        print("Error!, No extension specified.")
        exit()
    print("")
    os.chdir(directory)
    files = os.listdir(directory)
    for file in files:
        if file.endswith("." + extension):
            new_file = file[:-4]
            os.rename(file, new_file)
            print("Renamed {} to {}".format(file, new_file))
    print("")
    print("Done!")
if __name__ == "__main__":
    start_time = os.times()
    main()
    end_time = os.times()
    print("Operation took {} seconds".format(end_time[0] - start_time[0]))
    input("Press Enter to exit...")
    exit()
main()

filename = input("Enter a file name: ")

#Split the file name into its base name and extension
basename, extension = filename.rsplit('.', 1)

print("The extension of the file is:", extension)




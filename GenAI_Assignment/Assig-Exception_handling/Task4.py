filename= input("Enter Filename")

try:
    file= open(filename, "r")

    for i in range(3):
        line = file.readline()

        if line =="":
            break

        print(line, end="")

    file.close()

except FileNotFoundError:
    print("Error: Filr NOt Found") 

except PermissionError:
    print("Error: Permission Denied")

finally:
    print("File Operation Attempted")    

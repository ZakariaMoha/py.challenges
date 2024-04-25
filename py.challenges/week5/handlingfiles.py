try:
    # File Creation
    with open("my_file.txt", "w") as file:
        file.write("This is line 1\n")
        file.write("12345\n")
        file.write("Another line here\n")

    # File Reading and Display
    print("Contents of my_file.txt:")
    with open("my_file.txt", "r") as file:
        for line in file:
            print(line.strip())

    # File Appending
    with open("my_file.txt", "a") as file:
        file.write("Additional line 1\n")
        file.write("67890\n")
        file.write("One more line\n")

except FileNotFoundError:
    print("File not found. Please check the file path.")
except PermissionError:
    print("Permission denied. Please check file permissions.")
except Exception as e:
    print("An error occurred:", e)
finally:
    print("File handling process completed.")

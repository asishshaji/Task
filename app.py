import createFile
import deleteEverything
import time
import os

while True:
    try:
        print("---------------------------------------------")
        choice = int(
            input("1: Create files\n2: Delete everything\n3: Delete path\n:>"))
        print("---------------------------------------------")

        if choice == 1:
            size = int(input("Enter size :> "))
            createFile.createFiles(size)
        elif choice == 2:
            start = time.time()
            deleteEverything.delete(os.path.join(os.getcwd(), "tmp"))
            end = time.time()
            print("")
            print("[i] Completed in", round(end-start, 3), "seconds")
            print("")
        elif choice == 3:
            folderName = input("Enter folder name :> ")
            print(os.path.join(os.getcwd(), "tmp", folderName))

            deleteEverything.delete(os.path.join(
                os.getcwd(), "tmp", folderName))
        else:
            break
    except ValueError:
        print()
        print("[i] Enter integer values")
        print()

print("")
print("[!] Closing app")
print("")

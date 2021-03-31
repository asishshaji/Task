import os


def createFiles(size=2):
    orgPath = os.getcwd()
    if(not os.path.exists(os.path.join(orgPath, "tmp"))):
        os.mkdir(os.path.join(orgPath, "tmp"))
    os.chdir(os.path.join(orgPath, "tmp"))
    for i in range(size):
        if not os.path.exists("TEST"+str(i)):
            os.mkdir("TEST"+str(i))
            print("[i] Created folder :", "TEST"+str(i))
        with open(os.path.join("TEST"+str(i), str(i)+".txt"), "w+") as file:
            print("[i] Created file :", os.path.join(
                "TEST"+str(i), str(i)+".txt"))
            file.write("In Jupyter Notebook you can execute Terminal commands in the notebook cells by prepending an exclamation point/bang( ! ) to the beginning of the command. This can be useful for many things such as getting information without having to open a Terminal/Command Prompt, or installing a conda package you are trying to use")

    for i in range(size):
        with open("{}.txt".format(str(i)), "w+") as file:
            file.write(str(i) * 23)
            print("[i] Created file :", "{}.txt".format(str(i)))

    print("")
    print("[i] Created files and folders")
    print("")

    os.chdir(orgPath)

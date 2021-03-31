import os


def delete(path):
    currentContents = os.listdir(path)

    if os.path.isdir(path) and len(os.listdir(path)) == 0:
        os.rmdir(path)

    if len(currentContents) - 3 != 0:
        for content in currentContents:
            folderPath = os.path.join(path, content)

            if os.path.isfile(folderPath):
                if(content.split(".")[1] != "py"):
                    os.remove(folderPath)
                    print("[x] Removed file : {}".format(folderPath))
                    if os.path.isdir(path) and len(os.listdir(path)) == 0:
                        os.rmdir(path)

            elif os.path.isdir(folderPath) or len(os.listdir(folderPath)) != 0:
                delete(folderPath)

                if os.path.isdir(folderPath) and len(os.listdir(folderPath)) == 0:
                    os.rmdir(folderPath)
                    print("[x] Removed folder : {}".format(folderPath))

    else:
        print("")
        print("[i] Folder is empty")
        print("")
        return

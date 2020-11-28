import os

def countDirectory(path):
    count = 0
    for fileobj in os.listdir(path):
        fileobj = fileobj.split(".")
        if len(fileobj) == 2:
            filename = fileobj[0]
            file_extension = "." + fileobj[1]
        else:
            if fileobj[0] == "__pycache__":
                file_extension = fileobj[0]
                filename = ""
            else:
                file_extension = ""
                filename = fileobj[0]

        if file_extension == ".py":
            with open(path+r"\\"+filename+file_extension, 'r') as f:
                for line in f:
                    count+=1

        elif file_extension == "":
            count+=countDirectory(path + r"\\" + filename)
    return count

# r"C:\Users\finnk\Documents\Blender\visualScripting\blender_visual_scripting_addon"
print("The total line count is: ", countDirectory(r"C:\Users\finnk\Documents\Blender\visualScripting\blender_visual_scripting_addon"))
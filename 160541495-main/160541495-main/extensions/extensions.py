x=input("name file ")
if "." in x:
    b=x.split(".")
    b=b[-1]
    b=b.lower().strip()
    if b =="gif":
        print("image/gif",end="")
    elif b== "jpg" or b == "jpeg":
        print("image/jpeg",end="")
    elif b=="png":
        print("image/png",end="")
    elif b=="pdf":
        print("application/pdf",end="")
    elif b=="txt":
        print("text/plain",end="")
    elif b=="zip":
        print("application/zip",end="")
    else:
        print("application/octet-stream",end="")

else:
     print("application/octet-stream",end="")








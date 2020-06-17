filename=str(input("input thr filename: "))
z=filename.split(".")
if(z[1]=="py"):
    print("The Extension of the file is:'python'")
elif(z[1]=="java"):
    print("The extension of the file is: 'java'")
elif(z[1]=="c++"):
    print("The extension of the file is:'c++'")
elif(z[1]=="c"):
    print("The extension of the file is:'c'")
else:
    print("please add extension to the file")
try:
    file=open("file_1.txt",'w')
    #data =file.write()
    data = "hi everyone"
    file.write(data)
    print(data)

except BaseException as be:
    print(be)   
finally:
    file.close()
    print("*****file closed****")
    

def print_list(list,index=0):
    if(index==len(list)):
        return
    
    print(list[index])
    return print_list(list,index+1)


fruits=["mango","banana","orange","watermilon","graps"]

print_list(fruits)
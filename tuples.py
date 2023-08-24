def partition(numX):
    tup = ()
    if numX % 2 == 0:
        tup = (numX,None)
    else:
        tup = (None, numX)
    return tup


def partition_list(List):
    newlist=[]
    for i in List:
        res = partition(i)
        newlist.append(res)
    return newlist

part_list = [1,2,3,4,5,6,7,8,9,10,11]


# X = int(input("Please Enter Your Number"))
# first = partition(X)

response = partition_list(part_list)
print(response)

N=int(input())
output=[]
for i in range(N):
    command=list(map(str,input().split()))
    if command[0] == "insert":
        output.insert(int(command[1]),int(command[2]))
    elif command[0] == "print":
        print(output)
    elif command[0] == "remove":
        output.remove(int(command[1]))
    elif command[0] == "sort":
        output.sort()
    elif command[0] == "pop":
        output.pop()
    elif command[0] == "append":
        output.append(int(command[1]))
    elif command[0] == "reverse":
        output.reverse()
        
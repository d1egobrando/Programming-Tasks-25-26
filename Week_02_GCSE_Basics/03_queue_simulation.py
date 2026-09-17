queue = []
name1 = input("Enter a name: ")
name2 = input("Enter a name: ")
name3 = input("Enter a name: ")
name4 = input("Enter a name: ")

queue.append(name1)
queue.append(name2)
queue.append(name3)
queue.append(name4) #add to queue (Enqueue)

print(queue[0]) #peek size

print(queue)

print(("The length of the queue is: " ,len(queue))) #size of queue

while len(queue) != 0:
    print(queue.pop(0)) #dequeue

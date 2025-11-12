#copilot*
class Node:
    def __init__(self, data):
        self.data = data #stores Data*
        self.next = None   #Pointer to the next node

class LinkedList:
    def __init__(self):
        self.head = None  #Initialize the head of the list

    def append(self, data):
        new_node = Node(data) 
        if not self.head:
            self.head  = new_node
            return
        current =self.head
        while current.next:
            current = current.next  

        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" --> ")
            current = current.next
        print("None")

ll = LinkedList()
ll.append(5)
ll.append(20)
ll.append(30)
ll.display() 
            




   


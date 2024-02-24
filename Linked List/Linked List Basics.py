  
# Node class
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
#Linked list class

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    # append at the end of the list
    def append(self,new_node):
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            return
        self.tail.next=new_node
        self.tail = self.tail.next

    def printList(self, head):
        while head:
            print(head.data,end=' ')
            head=head.next
        print()

    def displayList(self, head):
        #code here
        llist =str(head.data)
        while head.next != None:
            head = head.next
            llist=llist+'-->'+str(head.data)
        return llist
    
    #Function to count nodes of a linked list.
    def getCount(self, head_node):
        #code here
        count =1
        while head_node.next != None:
            count +=1
            head_node = head_node.next
        return count
    
    def sumOfElements(self, head):
        S=head.data
        while head.next != None:
            head = head.next
            S+=head.data
        return S

    def searchLinkedList(self, head, x):
        while head != None:
            if head.data == x:
                return 1
            head = head.next
        return 0
    def insertAtBegining(self,head,x):
        # code here
        node=Node(x) # create a new node
        node.next=head
        return node
    
    #Function to insert a node at the end of the linked list.
    def insertAtEnd(self, head, x):
        if head is None:
            return Node(x)
        current = head
        while current.next is not None:
            current = current.next
        current.next = Node(x)
        return head
    
    def insertAtPosition(self,head,pos,data):
        current = head
        count = 0
        while current != None:
            count +=1
            if pos == 0:
                node = Node(data)
                node.next = head
                return node
            elif count == pos:
                node = Node(data)
                if current.next != None:
                    node.next = current.next
                current.next = node
                return head
            else:
                current = current.next
        return head
    

a=LinkedList()
#nodes=list(map(int,input().strip().split())) #list containing nodes
nodes = [320, 16, 913, 695, 392, 935, 203, 158, 771, 249, 515, 593, 966, 995, 413, 423, 6, 652, 55, 102, 895, 742, 997, 275]
#print(len(nodes))

for x in nodes:
    node=Node(x) # create a new node
    a.append(node)

pos =0
data = 611
a.head=LinkedList().insertAtPosition(a.head,pos,data)
print(LinkedList().displayList(a.head))

pos =1
data = 611
a.head=LinkedList().insertAtPosition(a.head,pos,data)
print(LinkedList().displayList(a.head))

pos =len(nodes)+1
data = 611
a.head=LinkedList().insertAtPosition(a.head,pos,data)

print(LinkedList().displayList(a.head))
print('Count :',LinkedList().getCount(a.head))
print('Sum :',LinkedList().sumOfElements(a.head))
print('Search :',LinkedList().searchLinkedList(a.head,x=5))
print('Search :',LinkedList().searchLinkedList(a.head,x=0))

b=LinkedList()
nodes_info= [5,1,6,1,9,1]
for i in range(0,len(nodes_info)-1,2):
    if(nodes_info[i+1]==0):
        b.head = LinkedList().insertAtBegining(b.head,nodes_info[i])
    else:
        b.head = LinkedList().insertAtEnd(b.head,nodes_info[i])

LinkedList().printList(b.head)

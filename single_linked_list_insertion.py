class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def append(self,data):
        new_node=Node(data)
        if(self.head==None):
            self.head=new_node
            return
        else:
            last_node=self.head
            while last_node.next:
                last_node=last_node.next
            last_node.next=new_node
    def print_list(self):
        head_node=self.head
        while head_node:
            print(head_node.data)
            head_node=head_node.next
llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")


llist.print_list() 
llist.append(87)
llist.append(80)
llist.print_list()

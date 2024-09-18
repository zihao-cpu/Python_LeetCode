class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
class MyLinkedList:
    def __init__(self,val) -> None:
        self.head=ListNode(val)
        self.size=1
    def get(self,index:int)->int:
        if index<0 or index>=self.size:
            return -1
        current =self.head
        for i in range(0,index):
            current=current.next
        return current.val
    def addAtHead(self,val:int)->None:
        self.head.next = ListNode(val, self.dummy_head.next)
        self.size += 1
    def addAtTail(self,val:int)->None:
        current=self.head
        while current.next:
            current=current.next
        current.next=ListNode(val)
        self.size+=1
    def addAtIndex(self,index,val)->None:
        if index<0 or index>self.size:
            return 
        current=self.head
        for i in range(0,index):
            current=current.next
        current.next=ListNode(val,current.next)
        self.size+=1
    def deleteAtIndex(self,index):
        if index<0 or index>self.size:
            return
        current=self.head
        for i in range(0,index):
            current=current.next
        current.next=current.next.next
        self.size-=1
    def printLinkedList(self)->list:
        dataVals=[]
        current=self.head
        for i in range(0,self.size):
            dataVals.append(current.val)
            current=current.next
        # while current.next:
        #     dataVals.append(current.val)
        #     current=current.next
        return dataVals

obj = MyLinkedList(1)

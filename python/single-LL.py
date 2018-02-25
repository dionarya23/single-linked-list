class Node :
    
    def __init__(self,data,nextNode=None):
        self.data = data
        self.nextNode = nextNode

    def getData(self) :
        return self.data

    def setData(self, val):
        self.data = val
    
    def getNextNode(self):
        return self.nextNode

    def setNextNode(self, val):
        self.nextNode = val

class LinkedList:

    def __init__(self, head = None):
        self.head = head
        self.size = 0

    def getSize(self):
        return self.size

    def addNode(self, data):
        newNode = Node(data,self.head)
        self.head = newNode
        self.size+=1
        return True

    def printNode(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.getNextNode()


myList = LinkedList()
angka = 1
acuan = 4
print("======== Inserting Data =========")
while angka < acuan :
      integer = int(input("Insert a Integer : "))
      myList.addNode(integer)
      a = raw_input("Try again? : ")
      if a=="yes":
        angka = 1
      elif a=="no":
        angka = 5

myList.printNode()

class Node
    attr_accessor :next
    attr_reader   :value
   
    def initialize(value)
      @value = value
      @next  = nil
    end
   
    def to_s
      "Node with value: #{@value}"
    end
  end

class LinkedList
    def initialize
        @head = nil
    end

    def add(value)
        if @head
            find_tail.next = Node.new(value)
        else
            @head = Node.new(value)
        end
    end

    def find_tail
        node=@head
        return node if !node.next
        return node if !node.next while(node=node.next)
    end

    def print
        node = @head
        puts node
        
        while (node = node.next)
            puts node
        end
    end
end

ex = LinkedList.new
ex.add(10)
ex.add(20)
ex.add(30)

ex.print
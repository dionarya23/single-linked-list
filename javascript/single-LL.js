function Node(data) {
    this.data = data;
    this.next = null;
}


class SingleLL {
    constructor() {
     this._length = 0
     this.head = null
    }

    add(value) {
        var node = new Node(value),
        currentNode = this.head;

        if(!currentNode) {
            this.head = node;
            this._length++;

            return node;
        }

        while(currentNode.next) {
            currentNode = currentNode.next;
        }

        currentNode.next = node;
        this._length++;

        return node;
    }
}

var insert = new SingleLL();
insert.add(3);
insert.add(5);
insert.add(5);

console.log(insert.head);
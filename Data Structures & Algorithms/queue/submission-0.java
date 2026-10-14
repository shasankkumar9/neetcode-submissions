class Deque {

    public class Node {
        int val;
        Node prev;
        Node next;
        public Node(int val) {
            this.val = val;
        }
    }

    private Node head;
    private Node tail;

    public Deque() {
        
    }

    public boolean isEmpty() {
        return head == null;
    }

    public void append(int value) {
       Node newNode = new Node(value);
       if(isEmpty()) {
        head = newNode;
        tail = newNode;
        return;
       }
       tail.next = newNode;
       newNode.prev = tail;
       tail = newNode;
    }

    public void appendleft(int value) {
        Node newNode = new Node(value);
        if(isEmpty()) {
            head = newNode;
            tail = newNode;
        }
        newNode.next = head;
        head.prev = newNode;
        head = newNode;
    }

    public int pop() {
        if(tail == null) return -1;
        int val = tail.val;
        tail = tail.prev;
        if(tail != null) tail.next = null;
        return val;
    }

    public int popleft() {
        if(head == null) return -1;
        int val = head.val;
        head = head.next;
        if(head != null) head.prev = null;
        return val;
    }
}

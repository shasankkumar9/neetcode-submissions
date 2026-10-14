class Deque {
    public class Node {
        int val;
        Node prev = null;
        Node next = null;
        public Node(int val) {
            this.val = val;
        }
    }

    private Node head = null;
    private Node tail = null;

    public Deque() {}

    public boolean isEmpty() {
        return head == null && tail == null;
    }

    public void append(int value) {
        Node newNode = new Node(value);
        if (isEmpty()) {
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

        if (isEmpty()) {
            head = newNode;
            tail = newNode;
            return;
        }

        newNode.next = head;
        head.prev = newNode;
        head = newNode;
    }

    public int pop() {
        if (isEmpty()) {
            return -1;
        }

        int val = tail.val;

        if (head == tail) {
            head = null;
            tail = null;
        } else {
            tail = tail.prev;
            tail.next = null;
        }

        return val;
    }

    public int popleft() {
        if (isEmpty()) {
            return -1;
        }

        int val = head.val;

        if (head == tail) {
            head = null;
            tail = null;
        } else {
            head = head.next;
            head.prev = null;
        }

        return val;
    }
}

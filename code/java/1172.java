// https://leetcode.com/problems/design-browser-history/
class BrowserHistory {
    private Node cur;

    public BrowserHistory(String homepage) {
        cur = new Node(homepage);
    }

    public void visit(String url) {
        Node n = new Node(url);
        cur.next = n;
        n.prev = cur;
        cur = n;
    }

    public String back(int steps) {
        while (steps > 0 && cur.prev != null) {
            steps--;
            cur = cur.prev;
        }
        return cur.url;
    }

    public String forward(int steps) {
        while (steps > 0 && cur.next != null) {
            steps--;
            cur = cur.next;
        }
        return cur.url;
    }

    static class Node {
        String url;
        Node next;
        Node prev;

        public Node(String url) {
            this.url = url;
            this.next = null;
            this.prev = null;
        }
    }
}

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * BrowserHistory obj = new BrowserHistory(homepage);
 * obj.visit(url);
 * String param_2 = obj.back(steps);
 * String param_3 = obj.forward(steps);
 */

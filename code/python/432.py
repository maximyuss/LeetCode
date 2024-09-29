# https://leetcode.com/problems/all-oone-data-structure/
class Node:
    def __init__(self, val=0, prev=None, next=None):
        self.freq = val
        self.keys = set()
        self.prev = prev
        self.next = next


class AllOne:
    def __init__(self):
        self.store = {}
        self.begin = Node()
        self.end = Node()
        self.begin.next = self.end
        self.end.prev = self.begin

    def inc(self, key: str) -> None:
        if key in self.store:
            node = self.store[key]
            freq = node.freq
            node.keys.remove(key)
            next_node = node.next
            if next_node == self.end or next_node.freq != freq + 1:
                # Create a new node
                new_node = Node(freq + 1, node, next_node)
                node.next = new_node
                next_node.prev = new_node
                new_node.keys.add(key)
                self.store[key] = new_node
            else:
                # Increment the existing next node
                next_node.keys.add(key)
                self.store[key] = next_node
            # Remove the current node if it has no keys left
            if not node.keys:
                self.removeNode(node)
        else:  # Key does not exist
            first_node = self.begin.next
            if first_node == self.end or first_node.freq > 1:
                # Create a new node
                new_node = Node(1, self.begin, first_node)
                self.begin.next = new_node
                first_node.prev = new_node
                new_node.keys.add(key)
                self.store[key] = new_node
            else:
                first_node.keys.add(key)
                self.store[key] = first_node

    def dec(self, key: str) -> None:
        if key not in self.store: return
        node = self.store[key]
        node.keys.remove(key)
        freq = node.freq
        if freq == 1:
            # Remove the key from the map if freq is 1
            del self.store[key]
        else:
            prev_node = node.prev
            if prev_node == self.begin or prev_node.freq != freq - 1:
                # Create a new node
                new_node = Node(freq - 1, prev_node, node)
                prev_node.next = new_node
                node.prev = new_node
                new_node.keys.add(key)
                self.store[key] = new_node
            else:
                # Decrement the existing previous node
                prev_node.keys.add(key)
                self.store[key] = prev_node
        # Remove the node if it has no keys left
        if not node.keys:
            self.removeNode(node)

    def getMaxKey(self) -> str:
        if self.end.prev == self.begin:
            return ""
        return next(iter(self.end.prev.keys))

    def getMinKey(self) -> str:
        if self.begin.next == self.end:
            return ""
        return next(iter(self.begin.next.keys))

    def removeNode(self, node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode

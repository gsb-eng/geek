'''
Program to find the loop and delete in a linked list.
'''


class Node(object):
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList(object):
    """
    Singly Linked List.
    """
    def __init__(self, node=None):
        self.head = None

    def insert(self, node):
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def print_list(self, node=None):
        if not node:
            node = self.head
        data = str(node.data)
        if node.next:
            data += " -- > " + str(self.print_list(node.next))
        return data

    def is_loop_exists(self):
        slow_runner = self.head
        speed_runner = self.head.next
        while True:
            if slow_runner is speed_runner:
                print "Loop Exists"
                return slow_runner
            slow_runner = slow_runner.next
            speed_runner = speed_runner.next.next
            if not speed_runner:
                print "Not loop"
                return

    def is_node_reachable(self, node, loop_node):
        cur_node = loop_node.next
        if cur_node is loop_node:
            return cur_node
        while cur_node is not loop_node:
            if cur_node is node:
                print "Node found" + str(node.data)
                return node
            cur_node = cur_node.next

    def break_loop(self):
        reachable_node = None
        cur_node = self.head
        loop_node = self.is_loop_exists()
        print "loop node is " + str(loop_node.data)
        if loop_node:
            while cur_node.next:
                reachable_node = self.is_node_reachable(cur_node, loop_node)
                if reachable_node:
                    print "Reachable node " + str(reachable_node.data)
                    break
                print " Current " + str(cur_node.data)
                cur_node = cur_node.next

        while True:
            if loop_node.next is reachable_node:
                loop_node.next = None
                break
            loop_node = loop_node.next

ll = LinkedList()
loop = Node(4)
ll.insert(loop)
ll.insert(Node(1))
ll.insert(Node(2))
ll.insert(Node(12))
ll.insert(Node(3))
ll.insert(loop)
ll.insert(Node(5))
ll.insert(Node(6))
ll.insert(Node(8))

ll.is_loop_exists()
ll.break_loop()
print ll.print_list()

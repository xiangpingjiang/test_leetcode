from typing import Optional

from collections import OrderedDict

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def create_linked_list(data):
    """
    从给定的数据创建带随机指针的链表
    data格式: [[val, random_index], ...]
    其中random_index表示随机指针指向的节点索引，null用None表示
    """
    if not data:
        return None
    
    # 第一步：创建所有节点（不设置next和random指针）
    nodes = []
    for item in data:
        val = item[0]
        node = Node(val)
        nodes.append(node)
    
    # 第二步：设置next指针
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    
    # 第三步：设置random指针
    for i, item in enumerate(data):
        random_idx = item[1]
        if random_idx is not None and 0 <= random_idx < len(nodes):
            nodes[i].random = nodes[random_idx]
    
    return nodes[0]  # 返回头节点


def print_linked_list(head):
    """
    打印链表，包括随机指针指向的节点索引
    """
    if not head:
        print("Empty linked list")
        return
    
    # 创建节点到索引的映射
    node_to_index = {}
    current = head
    index = 0
    
    # 第一次遍历：建立节点到索引的映射
    while current:
        node_to_index[current] = index
        current = current.next
        index += 1
    
    # 第二次遍历：打印链表
    current = head
    index = 0
    result = []
    
    while current:
        # 获取random指针指向的节点索引
        if current.random and current.random in node_to_index:
            random_index = node_to_index[current.random]
        else:
            random_index = None
        
        result.append([current.val, random_index])
        current = current.next
        index += 1
    
    print(result)


def print_linked_list_detailed(head):
    """
    打印更详细的信息，包括每个节点的内存地址
    """
    if not head:
        print("Empty linked list")
        return
    
    # 创建节点到索引的映射
    node_to_index = {}
    current = head
    index = 0
    
    print("Linked List Details:")
    print("-" * 50)
    
    # 建立节点到索引的映射
    while current:
        node_to_index[current] = index
        current = current.next
        index += 1
    
    # 打印每个节点的详细信息
    current = head
    index = 0
    
    while current:
        # 获取random指针信息
        if current.random:
            if current.random in node_to_index:
                random_info = f"node {node_to_index[current.random]} (val: {current.random.val})"
            else:
                random_info = f"node outside list (val: {current.random.val})"
        else:
            random_info = "null"
        
        # 获取next指针信息
        if current.next:
            if current.next in node_to_index:
                next_info = f"node {node_to_index[current.next]}"
            else:
                next_info = "node outside list"
        else:
            next_info = "null"
        
        print(f"Node {index}: val={current.val}, "
              f"address={hex(id(current))}, "
              f"next->{next_info}, "
              f"random->{random_info}")
        
        current = current.next
        index += 1
    print("-" * 50)

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        
        d = {}

        i = 0 
        p = head
        while p:
            d[p] = i
            i+= 1
            p = p.next
        
        l = []
        p = head
        while p:
            t = [p.val]
            ran = None

            if p.random:
                ran = d[p.random]
            t.append(ran)
            l.append(t)
            p = p.next
        
        l_c = []
        for i in l:
            n = Node(x=i[0])
            l_c.append(n)
        
        m = len(l_c)

        for i in range(m-1):
            l_c[i].next = l_c[i+1]
            if l[i][1] != None:
                l_c[i].random = l_c[l[i][1]]
        
        l_c[-1].next = None

        if l[-1][1] != None:
            l_c[-1].random = l_c[l[-1][1]]
        return l_c[0]

# 测试代码
if __name__ == "__main__":
    # 测试数据
    data = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
    
    print("原始数据:", data)
    print()
    
    # 创建链表
    head = create_linked_list(data)
    
    # 打印链表（简洁格式）
    print("简洁格式输出:")
    print_linked_list(head)
    print()


    s = Solution()

    h =  s.copyRandomList(head)
    print_linked_list(h)
    
    # # 打印链表（详细格式）
    # print_linked_list_detailed(head)
    
    # # 测试空链表
    # print("\n测试空链表:")
    # empty_head = create_linked_list([])
    # print_linked_list(empty_head)
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(lst):
    """从列表创建链表，返回头节点"""
    if not lst:
        return None
    
    head = ListNode(lst[0])
    current = head
    
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head

def print_linked_list(head):
    """打印链表，格式为：1 -> 2 -> 3 -> None"""
    result = []
    current = head
    
    while current:
        result.append(str(current.val))
        current = current.next
    
    if not result:
        print("None")
    else:
        print(" -> ".join(result) + " -> None")

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        li1 = []
        li2 = []
        p = l1
        while p:
            li1.append(p.val)
            p = p.next

        p = l2
        while p:
            li2.append(p.val)
            p = p.next

        s = 0
        for i in range(len(li1)):
            s += li1[i] * 10**i
        for i in range(len(li2)):
            s += li2[i] * 10**i

        str_s = str(s)[::-1]
        i = 0
        while str_s[i] == '0':
            i += 1
        str_s = str_s[i:]
        n = len(str_s)
        n_l = []
        for i in range(n):
            node = ListNode(val=int(str_s[i]))
            n_l.append(node)
        for i in range(n-1):
            n_l[i].next = n_l[i+1]
        n_l[-1].next = None

        return n_l[0]

# 测试代码
if __name__ == "__main__":
    # 测试用例1：普通链表
    lst1 = [2,4,3]


    lst2 = [5,6,4]
    head1 = create_linked_list(lst1)
    head2 = create_linked_list(lst2)

    s = Solution()
    h =  s.addTwoNumbers(head1,head2)
    print_linked_list(h)
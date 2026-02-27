class ListNode:
    def __init__(self, val=0, next=None,key = 0):
        self.val = val
        self.next = next
        self.key = key


class LRUCache:

    def __init__(self, capacity: int):
        self.d = {}
        self.start = ListNode(val = 'init')
        self.end = self.start
        self.end_pre = None
        self.capacity = capacity
        self.length = 0
        

    def get(self, key: int) -> int:
        if self.capacity != 1:
            if key in self.d:
                ans = self.d[key].next.val
                node = ListNode(val=ans,key=key)
                if self.length > 1:
                    self.d[key].next = self.d[key].next.next
                else:
                    self.end = self.start                
                if self.end_pre:
                    self.d[key] = self.end_pre
                else:
                    self.d[key] = self.start
                self.end_pre = self.end
                self.end.next , self.end = node, node
                return ans
            else:
                return -1
        else:
            if key in self.d:
                return self.d[key]
            else:
                return -1
        

    def put(self, key: int, value: int) -> None:
        node = ListNode(val = value,key=key)
        if self.capacity != 1:
            if key not in self.d:
                if self.length + 1 <= self.capacity:
                    self.length += 1
                else:
                    self.d.pop(self.start.next.key)
                    self.start.next = self.start.next.next
                    

            else:
                if self.length > 1:
                    self.d[key].next = self.d[key].next.next
                else:
                    self.end = self.start


            self.end_pre = self.end
            self.end.next , self.end = node, node

            if self.end_pre:
                self.d[key] = self.end_pre
            else:
                self.d[key] = self.start
        else:
            if key not in self.d:
                if self.length == 0:
                    self.d[key] = value
                    self.length = 1
                else:
                    self.d = {}
                    self.d[key] = value
            else:
                self.d[key] = value



f_l = ["LRUCache","put","put","get","get","put","get","get","get"]

p_l = [[2],[2,1],[3,2],[3],[2],[4,3],[2],[3],[4]]
ans = [None]

obj = LRUCache(p_l[0][0])

for i in range(1,len(f_l)):
    if f_l[i] == "put":
        obj.put(p_l[i][0],p_l[i][1])
        ans.append(None)
    if f_l[i] == "get":
        a = obj.get(p_l[i][0])
        ans.append(a)
print(ans)
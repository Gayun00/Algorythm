class ListNode:
    def __init__(self, val=0,prev=None, next=None):
        self.val = val
        self.prev= prev
        self.next= next
    


class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = self.current = ListNode(val=homepage)
        

    def visit(self, url: str) -> None:
        self.current.next = ListNode(val=url, prev=self.current)
        self.current = self.current.next
        return None

    def back(self, steps: int) -> str:
        while steps and self.current.prev is not None:
            steps-=1
            self.current = self.current.prev
        return self.current.val

    def forward(self, steps: int) -> str:
        while steps and self.current.next is not None:
            steps -=1
            self.current = self.current.next
        return self.current.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
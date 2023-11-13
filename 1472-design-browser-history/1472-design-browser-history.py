
class BrowserHistory:

    def __init__(self, homepage: str):
        self.realLen = 1
        self.curpos = 0
        self.history = [homepage]
       
    def visit(self, url: str) -> None:
        if len(self.history) < self.curpos + 2:
            self.history.append(url)
        else:
            self.history[self.curpos + 1] = url
        self.curpos +=1
        self.realLen = self.curpos + 1
        
       
        
    def back(self, steps: int) -> str:
        self.curpos = max(self.curpos - steps ,0)
        return self.history[self.curpos]
        
     

    def forward(self, steps: int) -> str:
        self.curpos = min(self.curpos + steps, self.realLen - 1)
        return self.history[self.curpos]
     


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
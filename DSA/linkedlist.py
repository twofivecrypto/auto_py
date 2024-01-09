stock = []

stock.append('mango')

print(stock)
print(len(stock))


class MangoNode:
    def __init__(self, label):
        self.label = label
        self.next_mango = None
        
class MangoBasket:
    def __init__(self):
        self.top_mango = None
        
    def is_empty(self):
        return self.top_mango is None
    
    def add_mango(self, label):
        new_mango = MangoNode(label)
        if self.is_empty():
            self.top_mango = new_mango
            return 
        last_mango = self.top_mango
        while last_mango.next_mango:
            last_mango = last_mango.next_mango
            last_mango.next_mango = new_mango
            
    def eat_mango(self, label):
        if self.is_empty():
            return
        if self.top_mango.label == label:
            self.top_mango = self.top_mango.next_mango
            return
        self.top_mango = self.top_mango.next_mango
        return
    
        
import math

class pagination():
    def __init__(self,items=[],page_size=10):
        self.items=items
        self.page_size=page_size
        self.current_idx=0
        self.total_pages=math.ceil(len(self.items)/self.page_size)
    

    def get_visible_item(self):
        start=self.current_idx * self.page_size
        end=start+self.page_size
        return self.items[start:end]
    
    def go_to_page(self,page_num):
        if 1<=page_num<=self.total_pages:
            self.current_idx=page_num-1
            return self.current_idx
        else:
            print("error. out of range")

    def first_page(self):
        self.current_idx=0
        return self.current_idx
    
    def last_page(self):
        self.current_idx=self.total_pages-1
        return self.current_idx
    
    def next_page(self):
        self.current_idx=self.current_idx+1
        return self.current_idx
    
    def previous_page(self):
        self.current_idx=self.current_idx-1
        return self.current_idx
    

words = list("abcdefghijklmnopqrstuvwxyz")
p = pagination(words, 5)

print(p.get_visible_item())  
p.next_page()
print(p.get_visible_item())  
p.last_page()
print(p.get_visible_item())  
p.previous_page()
print(p.get_visible_item())  

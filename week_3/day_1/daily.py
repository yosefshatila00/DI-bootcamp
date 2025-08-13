class Pagination:
    def __init__(self, items=None, page_size=10):
        self.items = items if items is not None else []
        self.page_size = page_size
        self.current_idx = 0 
        self.total_pages = (len(self.items) + self.page_size - 1) // self.page_size if self.items else 1
    
    def get_visible_items(self):
        """Return items on current page"""
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.items[start:end]
    
    def go_to_page(self, page_num):
        """Go to specific page (1-based)"""
        if page_num < 1 or page_num > self.total_pages:
            raise ValueError(f"Invalid page number. Must be between 1 and {self.total_pages}")
        self.current_idx = page_num - 1
        return self
    
    def first_page(self):
        """Go to first page"""
        self.current_idx = 0
        return self
    
    def last_page(self):
        """Go to last page"""
        self.current_idx = self.total_pages - 1
        return self
    
    def next_page(self):
        """Go to next page if exists"""
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1
        return self
    
    def previous_page(self):
        """Go to previous page if exists"""
        if self.current_idx > 0:
            self.current_idx -= 1
        return self
    
    def __str__(self):
        """String representation of current page items"""
        return "\n".join(str(item) for item in self.get_visible_items())


if __name__ == "__main__":
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    p = Pagination(alphabet, 4)
    
    print("Initial page:")
    print(p.get_visible_items())  
    
    print("\nNext page:")
    p.next_page()
    print(p.get_visible_items()) 
    
    print("\nLast page:")
    p.last_page()
    print(p.get_visible_items())  
    
    print("\nGo to page 3:")
    p.go_to_page(3)
    print(p.get_visible_items()) 
    print("\nTry invalid page:")
    try:
        p.go_to_page(0)
    except ValueError as e:
        print(f"Error: {e}")
    
    print("\nString output:")
    print(p.first_page()) 
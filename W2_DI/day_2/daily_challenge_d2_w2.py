class Pagination:
    def __init__(self, items=None, pageSize=10):
        self.items = items if items is not None else []
        self.pageSize = int(pageSize)
        self.currentPage = 1
        self.totalPages = self.calculate_total_pages()

    def calculate_total_pages(self):
        return -(-len(self.items) // self.pageSize)

    def getVisibleItems(self):
        start_index = (self.currentPage - 1) * self.pageSize
        end_index = start_index + self.pageSize
        return self.items[start_index:end_index]

    def prevPage(self):
        self.currentPage = max(1, self.currentPage - 1)
        return self

    def nextPage(self):
        self.currentPage = min(self.totalPages, self.currentPage + 1)
        return self

    def firstPage(self):
        self.currentPage = 1
        return self

    def lastPage(self):
        self.currentPage = self.totalPages
        return self

    def goToPage(self, pageNum):
        target_page = int(pageNum)
        self.currentPage = max(1, min(self.totalPages, target_page))
        return self

alphabetList = list("abcdefghijklmnopqrstuvwxyz")

p = Pagination(alphabetList, 4)

print(p.getVisibleItems())  
p.nextPage()
print(p.getVisibleItems())  
p.lastPage()
print(p.getVisibleItems())  
print(p.currentPage)  
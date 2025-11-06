class Metropolia_pub:
    def __init__(self,name):
        self.name = name
    def print_information(self):
        print(f'Name: {self.name}')
        
class Book(Metropolia_pub):
    def __init__(self,name,author,page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count
    def print_information(self):
        super().print_information()
        print(f'Author: {self.author}')
        print(f'Page: {self.page_count}\n')

class Magazine(Metropolia_pub):
    def __init__(self,name,chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor
    def print_information(self):
        super().print_information()
        print(f'Chief Editor: {self.chief_editor}\n')


b1 = Book('Compartment No. 6', 'Rosa Liksom',192)
m1 = Magazine('Donald Duck ','Aki Hyyppä')
b1.print_information()
m1.print_information()

class Author:
    def __init__(self, name):
        self.name = name
        self.books_published = [] # Books published by author, empty list on init

    def publish(self, title): 
        if title in self.books_published: # Do not allow duplicate books to be published by one author
            print('Error - cannot publish two books of the same title.') 
        else:
            self.books_published.append(title) 
            print(f'Successfully published {title}') # Let user know that book was successfully published

    def __str__(self):
        titles = ', '.join(self.books_published) or 'No published books' # If author has books published, join them together. Else, titles = 'No published books'
        return f'Name: {self.name}, Books Published: {titles}'
    
def main():
    # Example authors/books for testing
    jrr_tolkien = Author('J.R.R. Tolkien') 
    jrr_tolkien.publish('The Hobbit')
    jrr_tolkien.publish('The Return of the King')

    victor_hugo = Author('Victor Hugo')
    victor_hugo.publish('Les Misérables')
    
    print(jrr_tolkien)
    print(victor_hugo)

# Call main function 
if __name__ == '__main__':
    main()

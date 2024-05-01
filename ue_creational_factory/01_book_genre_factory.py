# Develop a factory to create books of different genres (e.g., Fiction, Nonfiction),
# each genre having a unique method to describe its content.



# Test the functionality of the Book Factory
if __name__ == '__main__':
    fiction_book = BookFactory.create_book("fiction")
    print("Fiction book description: ", end="")
    fiction_book.describe()

    nonfiction_book = BookFactory.create_book("nonfiction")
    print("Nonfiction book description: ", end="")
    nonfiction_book.describe()

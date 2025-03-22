class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = "Incomplete"  # Default holat

    def mark_as_complete(self):
        self.status = "Complete"

    def __str__(self):
        return f"Title: {self.title}\nDescription: {self.description}\nDue Date: {self.due_date}\nStatus: {self.status}\n"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_complete(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_as_complete()
                print(f"Task '{title}' marked as complete.")
                return
        print(f"Task '{title}' not found.")

    def list_all_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for task in self.tasks:
                print(task)

    def list_incomplete_tasks(self):
        incomplete_tasks = [task for task in self.tasks if task.status == "Incomplete"]
        if not incomplete_tasks:
            print("No incomplete tasks.")
        else:
            for task in incomplete_tasks:
                print(task)


def main():
    todo_list = ToDoList()

    while True:
        print("\n--- ToDo List Application ---")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. List All Tasks")
        print("4. List Incomplete Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            task = Task(title, description, due_date)
            todo_list.add_task(task)
            print("Task added successfully.")

        elif choice == "2":
            title = input("Enter the title of the task to mark as complete: ")
            todo_list.mark_task_complete(title)

        elif choice == "3":
            print("\n--- All Tasks ---")
            todo_list.list_all_tasks()

        elif choice == "4":
            print("\n--- Incomplete Tasks ---")
            todo_list.list_incomplete_tasks()

        elif choice == "5":
            print("Exiting the application. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()







class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
    def __str__(self):
        return f"Title: {self.title}\nContent: {self.content}\nAuthor: {self.author}\n"
class Blog:
    def __init__(self):
        self.posts = []
    def add_post(self, post):
        self.posts.append(post)
        print("Post added successfully.")
    def list_all_posts(self):
        if not self.posts:
            print("No posts available.")
        else:
            for post in self.posts:
                print(post)
    def list_posts_by_author(self, author):
        author_posts = [post for post in self.posts if post.author == author]
        if not author_posts:
            print(f"No posts found by author '{author}'.")
        else:
            for post in author_posts:
                print(post)
    def delete_post(self, title):
        for post in self.posts:
            if post.title == title:
                self.posts.remove(post)
                print(f"Post '{title}' deleted successfully.")
                return
        print(f"Post '{title}' not found.")
    def edit_post(self, title, new_content):
        for post in self.posts:
            if post.title == title:
                post.content = new_content
                print(f"Post '{title}' edited successfully.")
                return
        print(f"Post '{title}' not found.")
    def list_latest_posts(self, count=5):
        if not self.posts:
            print("No posts available.")
        else:
            latest_posts = self.posts[-count:]  # Eng so'nggi `count` ta maqola
            for post in latest_posts:
                print(post)
def main():
    blog = Blog()
    while True:
        print("\n--- Simple Blog System ---")
        print("1. Add Post")
        print("2. List All Posts")
        print("3. List Posts by Author")
        print("4. Delete Post")
        print("5. Edit Post")
        print("6. List Latest Posts")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            title = input("Enter post title: ")
            content = input("Enter post content: ")
            author = input("Enter author name: ")
            post = Post(title, content, author)
            blog.add_post(post)
        elif choice == "2":
            print("\n--- All Posts ---")
            blog.list_all_posts()
        elif choice == "3":
            author = input("Enter author name: ")
            print(f"\n--- Posts by {author} ---")
            blog.list_posts_by_author(author)
        elif choice == "4":
            title = input("Enter the title of the post to delete: ")
            blog.delete_post(title)
        elif choice == "5":
            title = input("Enter the title of the post to edit: ")
            new_content = input("Enter new content: ")
            blog.edit_post(title, new_content)
        elif choice == "6":
            count = int(input("Enter the number of latest posts to display: "))
            print(f"\n--- Latest {count} Posts ---")
            blog.list_latest_posts(count)
        elif choice == "7":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()





class Account:
    def __init__(self, account_number, account_holder_name, balance=0):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Invalid deposit amount.")
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")
    def transfer(self, target_account, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            target_account.balance += amount
            print(f"Transferred {amount} to {target_account.account_holder_name}.")
        else:
            print("Invalid transfer amount or insufficient balance.")
    def __str__(self):
        return f"Account Number: {self.account_number}\nAccount Holder: {self.account_holder_name}\nBalance: {self.balance}\n"
class Bank:
    def __init__(self):
        self.accounts = []
    def add_account(self, account):
        self.accounts.append(account)
        print("Account added successfully.")
    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None
    def check_balance(self, account_number):
        account = self.find_account(account_number)
        if account:
            print(f"Balance for account {account_number}: {account.balance}")
        else:
            print("Account not found.")
    def deposit_money(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            account.deposit(amount)
        else:
            print("Account not found.")
    def withdraw_money(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            account.withdraw(amount)
        else:
            print("Account not found.")
    def transfer_money(self, from_account_number, to_account_number, amount):
        from_account = self.find_account(from_account_number)
        to_account = self.find_account(to_account_number)
        if from_account and to_account:
            from_account.transfer(to_account, amount)
        else:
            print("One or both accounts not found.")
    def display_account_details(self, account_number):
        account = self.find_account(account_number)
        if account:
            print(account)
        else:
            print("Account not found.")
def main():
    bank = Bank()
    while True:
        print("\n--- Simple Banking System ---")
        print("1. Add Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Transfer Money")
        print("6. Display Account Details")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            account_number = input("Enter account number: ")
            account_holder_name = input("Enter account holder name: ")
            initial_balance = float(input("Enter initial balance: "))
            account = Account(account_number, account_holder_name, initial_balance)
            bank.add_account(account)
        elif choice == "2":
            account_number = input("Enter account number: ")
            bank.check_balance(account_number)
        elif choice == "3":
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))
            bank.deposit_money(account_number, amount)
        elif choice == "4":
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            bank.withdraw_money(account_number, amount)
        elif choice == "5":
            from_account_number = input("Enter your account number: ")
            to_account_number = input("Enter recipient account number: ")
            amount = float(input("Enter amount to transfer: "))
            bank.transfer_money(from_account_number, to_account_number, amount)
        elif choice == "6":
            account_number = input("Enter account number: ")
            bank.display_account_details(account_number)
        elif choice == "7":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()

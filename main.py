import sqlite3


def create_database():
    connection = sqlite3.connect("contacts.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            number INTEGER
        )
    """)

    connection.commit()
    connection.close()


def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    number = int(input("Enter number: "))

    connection = sqlite3.connect("contacts.db")
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO contacts (name, phone, number)
        VALUES (?, ?, ?)
        """,
        (name, phone, number)
    )

    connection.commit()
    connection.close()

    print("Contact added successfully.")


def show_contacts():
    connection = sqlite3.connect("contacts.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM contacts")
    contacts = cursor.fetchall()

    connection.close()

    for contact in contacts:
        print(contact)

def search_contact():
    name = input("Enter name to search: ")

    connection = sqlite3.connect("contacts.db")
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM contacts WHERE name LIKE ?",
        (f"%{name}%",)
    )

    contacts = cursor.fetchall()

    connection.close()

    if contacts:
        for contact in contacts:
            print(contact)
    else:
        print("No contacts found.")


def main():
    create_database()

    while True:
       print("1. Add contact")
       print("2. Show contacts")
       print("3. Search contact")
       print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()

        elif choice == "2":
            show_contacts()

        elif choice == "3":
            search_contact()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()

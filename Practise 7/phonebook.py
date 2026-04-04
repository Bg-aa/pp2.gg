import csv
from connect import get_connection

# 📌 Создание таблицы (если нет)
def create_table():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS contacts (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        phone VARCHAR(20)
    )
    """)

    conn.commit()
    cur.close()
    conn.close()


# 📌 1. Вставка из CSV
def insert_from_csv(filename):
    conn = get_connection()
    cur = conn.cursor()

    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cur.execute(
                "INSERT INTO contacts (name, phone) VALUES (%s, %s)",
                (row['name'], row['phone'])
            )

    conn.commit()
    cur.close()
    conn.close()
    print("Data inserted from CSV")


# 📌 2. Вставка вручную
def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO contacts (name, phone) VALUES (%s, %s)",
        (name, phone)
    )

    conn.commit()
    cur.close()
    conn.close()
    print("Contact added")


# 📌 3. Обновление
def update_contact():
    name = input("Enter name to update: ")
    new_name = input("New name (leave empty if not needed): ")
    new_phone = input("New phone (leave empty if not needed): ")

    conn = get_connection()
    cur = conn.cursor()

    if new_name:
        cur.execute(
            "UPDATE contacts SET name = %s WHERE name = %s",
            (new_name, name)
        )

    if new_phone:
        cur.execute(
            "UPDATE contacts SET phone = %s WHERE name = %s",
            (new_phone, name)
        )

    conn.commit()
    cur.close()
    conn.close()
    print("Contact updated")


def query_contacts():
    conn = get_connection()
    cur = conn.cursor()

    print("All contacts:")
    cur.execute("SELECT * FROM contacts")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    print("\n--- Search options ---")
    print("1. Search by name")
    print("2. Search by phone prefix")
    print("0. Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Enter name: ")
        cur.execute(
            "SELECT * FROM contacts WHERE name ILIKE %s",
            ('%' + name + '%',)
        )
        rows = cur.fetchall()

        print("\n Results:")
        for row in rows:
            print(row)

    elif choice == "2":
        prefix = input("Enter phone prefix: ")
        cur.execute(
            "SELECT * FROM contacts WHERE phone LIKE %s",
            (prefix + '%',)
        )
        rows = cur.fetchall()

        print("\n Results:")
        for row in rows:
            print(row)

    cur.close()
    conn.close()

# 📌 5. Удаление
def delete_contact():
    print("1. Delete by name")
    print("2. Delete by phone")

    choice = input("Choose: ")

    conn = get_connection()
    cur = conn.cursor()

    if choice == "1":
        name = input("Enter name: ")
        cur.execute("DELETE FROM contacts WHERE name = %s", (name,))

    elif choice == "2":
        phone = input("Enter phone: ")
        cur.execute("DELETE FROM contacts WHERE phone = %s", (phone,))

    conn.commit()
    cur.close()
    conn.close()
    print("Contact deleted")


# 📌 Меню
def menu():
    create_table()

    while True:
        print("\n--- PhoneBook ---")
        print("1. Insert from CSV")
        print("2. Add manually")
        print("3. Update contact")
        print("4. Query contacts")
        print("5. Delete contact")
        print("0. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            insert_from_csv(r"C:\Users\bagda\OneDrive\Desktop\Python\pp2.gg\Practise 7\contacts.csv")
        elif choice == "2":
            insert_from_console()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            query_contacts()
        elif choice == "5":
            delete_contact()
        elif choice == "0":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    menu()
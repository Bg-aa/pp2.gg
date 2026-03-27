# phonebook.py
import os
import csv
from connect import get_connection

# -----------------------------
# Инициализация таблицы
# -----------------------------
def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(100) NOT NULL,
            phone VARCHAR(20) NOT NULL UNIQUE
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

# -----------------------------
# Вставка контактов из CSV
# -----------------------------
def insert_from_csv(file_path):
    # путь относительно текущего скрипта
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(base_dir, file_path)

    conn = get_connection()
    cur = conn.cursor()
    try:
        with open(csv_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) < 2:
                    continue
                first_name, phone = row[0].strip(), row[1].strip()
                try:
                    cur.execute(
                        "INSERT INTO contacts (first_name, phone) VALUES (%s, %s) ON CONFLICT (phone) DO NOTHING;",
                        (first_name, phone)
                    )
                except Exception as e:
                    print(f"Ошибка при добавлении {first_name}, {phone}: {e}")
        conn.commit()
        print("Импорт CSV завершён!")
    finally:
        cur.close()
        conn.close()

# -----------------------------
# Вставка контакта с консоли
# -----------------------------
def insert_from_console():
    first_name = input("Введите имя: ").strip()
    phone = input("Введите телефон: ").strip()
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO contacts (first_name, phone) VALUES (%s, %s) ON CONFLICT (phone) DO NOTHING;",
            (first_name, phone)
        )
        conn.commit()
        print("Контакт добавлен!")
    except Exception as e:
        print("Ошибка:", e)
    finally:
        cur.close()
        conn.close()

# -----------------------------
# Обновление контакта
# -----------------------------
def update_contact():
    phone = input("Введите телефон контакта для обновления: ").strip()
    field = input("Что обновляем? (first_name/phone): ").strip()
    new_value = input(f"Введите новое значение для {field}: ").strip()
    if field not in ('first_name', 'phone'):
        print("Неверное поле")
        return
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(f"UPDATE contacts SET {field} = %s WHERE phone = %s", (new_value, phone))
        if cur.rowcount == 0:
            print("Контакт не найден")
        else:
            print("Контакт обновлён!")
        conn.commit()
    except Exception as e:
        print("Ошибка:", e)
    finally:
        cur.close()
        conn.close()

# -----------------------------
# Поиск контактов
# -----------------------------
def query_contacts():
    print("1. По имени")
    print("2. По префиксу телефона")
    choice = input("Выберите фильтр: ").strip()
    conn = get_connection()
    cur = conn.cursor()
    try:
        if choice == '1':
            name = input("Введите имя: ").strip()
            cur.execute("SELECT first_name, phone FROM contacts WHERE first_name ILIKE %s", (f"%{name}%",))
        elif choice == '2':
            prefix = input("Введите префикс телефона: ").strip()
            cur.execute("SELECT first_name, phone FROM contacts WHERE phone LIKE %s", (f"{prefix}%",))
        else:
            print("Неверный выбор")
            return
        rows = cur.fetchall()
        if not rows:
            print("Ничего не найдено")
        for row in rows:
            print(f"{row[0]} - {row[1]}")
    finally:
        cur.close()
        conn.close()

# -----------------------------
# Удаление контакта
# -----------------------------
def delete_contact():
    choice = input("Удалять по (1) имени или (2) телефону? ").strip()
    conn = get_connection()
    cur = conn.cursor()
    try:
        if choice == '1':
            name = input("Введите имя: ").strip()
            cur.execute("DELETE FROM contacts WHERE first_name = %s", (name,))
        elif choice == '2':
            phone = input("Введите телефон: ").strip()
            cur.execute("DELETE FROM contacts WHERE phone = %s", (phone,))
        else:
            print("Неверный выбор")
            return
        conn.commit()
        print(f"Удалено {cur.rowcount} записей")
    finally:
        cur.close()
        conn.close()

# -----------------------------
# Главное меню
# -----------------------------
def menu():
    init_db()
    while True:
        print("\n=== PhoneBook ===")
        print("1. Добавить контакт из CSV")
        print("2. Добавить контакт вручную")
        print("3. Обновить контакт")
        print("4. Поиск контактов")
        print("5. Удалить контакт")
        print("0. Выход")
        choice = input("Выберите действие: ").strip()
        if choice == '1':
            insert_from_csv("contacts.csv")
        elif choice == '2':
            insert_from_console()
        elif choice == '3':
            update_contact()
        elif choice == '4':
            query_contacts()
        elif choice == '5':
            delete_contact()
        elif choice == '0':
            break
        else:
            print("Неверный выбор!")

if __name__ == "__main__":
    menu()
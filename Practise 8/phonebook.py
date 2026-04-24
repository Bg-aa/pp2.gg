import os
import csv
from connect import get_connection

def init_db():
    """Инициализация базы данных и создание таблицы"""
    conn = get_connection()
    cur = conn.cursor()
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(100) NOT NULL,
            last_name VARCHAR(100),
            phone VARCHAR(20) NOT NULL UNIQUE
        );
    """)
    
    execute_sql_file(cur, "functions.sql")
    execute_sql_file(cur, "procedures.sql")
    
    conn.commit()
    cur.close()
    conn.close()
    print("База данных и функции успешно инициализированы!")

def execute_sql_file(cursor, filename):
    """Выполнение SQL файла"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            sql_content = f.read()
            # Разделяем на отдельные команды
            commands = sql_content.split(';')
            for command in commands:
                if command.strip():
                    cursor.execute(command)
    except FileNotFoundError:
        print(f"Файл {filename} не найден")

def search_by_pattern():
    """1. Поиск по шаблону"""
    pattern = input("Введите шаблон для поиска: ").strip()
    
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM search_contacts(%s);", (pattern,))
        results = cur.fetchall()
        
        if not results:
            print("Ничего не найдено.")
        else:
            print(f"\nНайдено {len(results)} записей:")
            print("-" * 70)
            for row in results:
                print(f"ID: {row[0]}, Имя: {row[1]}, Фамилия: {row[2] or 'N/A'}, Телефон: {row[3]}")
            print("-" * 70)
    finally:
        cur.close()
        conn.close()

def insert_or_update():
    """2. Вставка или обновление контакта"""
    first_name = input("Введите имя: ").strip()
    last_name = input("Введите фамилию (Enter если нет): ").strip()
    phone = input("Введите телефон: ").strip()
    
    if not last_name:
        last_name = None
    
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("CALL insert_or_update_contact(%s, %s, %s);", (first_name, last_name, phone))
        conn.commit()
        print("Операция выполнена успешно!")
    except Exception as e:
        print(f"Ошибка: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

def insert_multiple():
    """3. Массовая вставка контактов"""
    print("Введите контакты в формате 'Имя [Фамилия] Телефон' (каждый с новой строки)")
    print("Для завершения введите пустую строку:")
    
    contacts = []
    while True:
        line = input().strip()
        if not line:
            break
        
        parts = line.split()
        if len(parts) >= 2:
            phone = parts[-1]
            name = ' '.join(parts[:-1])
            contacts.append([name, phone])
        else:
            print(f"Неверный формат: {line}. Пропускаем.")
    
    if not contacts:
        print("Нет данных для вставки.")
        return
    
    contacts_str = "{"
    for i, c in enumerate(contacts):
        if i > 0:
            contacts_str += ","
        contacts_str += f'{{"{c[0]}","{c[1]}"}}'
    contacts_str += "}"
    
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("CALL insert_multiple_contacts(%s::TEXT[][]);", (contacts_str,))
        conn.commit()
        print("Массовая вставка завершена!")
    except Exception as e:
        print(f"Ошибка: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

def view_paginated():
    """4. Просмотр с пагинацией"""
    try:
        page = int(input("Номер страницы (с 1): ").strip())
        page_size = int(input("Записей на странице: ").strip())
        
        conn = get_connection()
        cur = conn.cursor()
        try:
            cur.execute("SELECT * FROM get_contacts_paginated(%s, %s);", (page, page_size))
            results = cur.fetchall()
            
            if not results:
                print("Нет записей на этой странице.")
            else:
                total_count = results[0][4]
                total_pages = (total_count + page_size - 1) // page_size
                
                print(f"\n--- Страница {page} из {total_pages} (Всего: {total_count}) ---")
                print("-" * 70)
                for row in results:
                    print(f"ID: {row[0]}, Имя: {row[1]}, Фамилия: {row[2] or 'N/A'}, Телефон: {row[3]}")
                print("-" * 70)
        finally:
            cur.close()
            conn.close()
    except ValueError:
        print("Введите корректные числа.")

def delete_contact_proc():
    print("1. По телефону")
    print("2. По имени/фамилии")
    choice = input("Выберите: ").strip()
    
    if choice == '1':
        value = input("Введите телефон: ").strip()
        delete_type = 'phone'
    elif choice == '2':
        value = input("Введите имя или фамилию: ").strip()
        delete_type = 'name'
    else:
        print("Неверный выбор!")
        return
    
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("CALL delete_contact_by(%s, %s);", (value, delete_type))
        conn.commit()
        print("Удаление выполнено!")
    except Exception as e:
        print(f"Ошибка: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

def menu():
    """Главное меню"""
    init_db()
    while True:
        print("\n" + "="*50)
        print("PHONEBOOK MANAGER")
        print("="*50)
        print("1. Поиск по шаблону (функция)")
        print("2. Добавить/обновить контакт (процедура)")
        print("3. Массовое добавление (процедура)")
        print("4. Просмотр с пагинацией (функция)")
        print("5. Удалить контакт (процедура)")
        print("0. Выход")
        print("-"*50)
        
        choice = input("Выберите действие: ").strip()
        
        if choice == '1':
            search_by_pattern()
        elif choice == '2':
            insert_or_update()
        elif choice == '3':
            insert_multiple()
        elif choice == '4':
            view_paginated()
        elif choice == '5':
            delete_contact_proc()
        elif choice == '0':
            print("До свидания!")
            break
        else:
            print("Неверный выбор!")

if __name__ == "__main__":
    menu()
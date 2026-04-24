-- 2. Процедура вставки нового пользователя; если существует - обновить телефон
CREATE OR REPLACE PROCEDURE insert_or_update_contact(
    p_first_name VARCHAR,
    p_last_name VARCHAR,
    p_phone VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO contacts (first_name, last_name, phone)
    VALUES (p_first_name, p_last_name, p_phone)
    ON CONFLICT (phone) 
    DO UPDATE SET 
        first_name = EXCLUDED.first_name,
        last_name = EXCLUDED.last_name;
    
    RAISE NOTICE 'Контакт % % успешно добавлен/обновлен', 
                 p_first_name, COALESCE(p_last_name, '');
END;
$$;

-- 3. Процедура массовой вставки с валидацией телефона
CREATE OR REPLACE PROCEDURE insert_multiple_contacts(
    contacts_data TEXT[][]  -- Массив вида {{name, phone}, ...}
)
LANGUAGE plpgsql
AS $$
DECLARE
    i INTEGER;
    first_name_val VARCHAR;
    last_name_val VARCHAR;
    phone_val VARCHAR;
    invalid_data TEXT[][] := ARRAY[]::TEXT[][];
    phone_pattern TEXT := '^[0-9\+\-\(\)\s]+$';
BEGIN
    FOR i IN 1..array_length(contacts_data, 1)
    LOOP
        -- Разделяем имя и фамилию (если есть)
        first_name_val := split_part(contacts_data[i][1], ' ', 1);
        last_name_val := NULL;
        
        IF array_length(string_to_array(contacts_data[i][1], ' '), 1) > 1 THEN
            last_name_val := substring(contacts_data[i][1] from position(' ' in contacts_data[i][1]) + 1);
        END IF;
        
        phone_val := contacts_data[i][2];
        
        -- Проверка корректности телефона (минимум 10 цифр)
        IF phone_val ~ phone_pattern AND length(regexp_replace(phone_val, '[^0-9]', '', 'g')) >= 10 THEN
            BEGIN
                INSERT INTO contacts (first_name, last_name, phone)
                VALUES (first_name_val, last_name_val, phone_val)
                ON CONFLICT (phone) DO UPDATE SET 
                    first_name = EXCLUDED.first_name,
                    last_name = EXCLUDED.last_name;
            EXCEPTION WHEN OTHERS THEN
                invalid_data := array_cat(invalid_data, ARRAY[[contacts_data[i][1], phone_val]]);
            END;
        ELSE
            invalid_data := array_cat(invalid_data, ARRAY[[contacts_data[i][1], phone_val]]);
        END IF;
    END LOOP;
    
    -- Выводим некорректные данные
    IF array_length(invalid_data, 1) > 0 THEN
        RAISE NOTICE 'Некорректные данные (неверный формат телефона): %', invalid_data;
    ELSE
        RAISE NOTICE 'Все данные успешно обработаны';
    END IF;
END;
$$;

-- 5. Процедура удаления данных из таблицы по имени или телефону
CREATE OR REPLACE PROCEDURE delete_contact_by(
    p_value VARCHAR,
    p_type VARCHAR DEFAULT 'phone'  -- 'phone' или 'name'
)
LANGUAGE plpgsql
AS $$
DECLARE
    deleted_count INTEGER;
BEGIN
    IF p_type = 'phone' THEN
        DELETE FROM contacts WHERE phone = p_value;
        GET DIAGNOSTICS deleted_count = ROW_COUNT;
        RAISE NOTICE 'Удалено % записей по телефону %', deleted_count, p_value;
    ELSIF p_type = 'name' THEN
        DELETE FROM contacts WHERE first_name = p_value OR last_name = p_value;
        GET DIAGNOSTICS deleted_count = ROW_COUNT;
        RAISE NOTICE 'Удалено % записей по имени/фамилии %', deleted_count, p_value;
    ELSE
        RAISE EXCEPTION 'Неверный тип поиска. Используйте "phone" или "name"';
    END IF;
END;
$$;
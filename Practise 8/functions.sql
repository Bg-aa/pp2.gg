-- 1. Функция возвращает все записи, соответствующие шаблону
CREATE OR REPLACE FUNCTION search_contacts(pattern TEXT)
RETURNS TABLE(
    id INTEGER,
    first_name VARCHAR,
    last_name VARCHAR,
    phone VARCHAR
) AS $$
BEGIN
    RETURN QUERY
    SELECT c.id, c.first_name, c.last_name, c.phone
    FROM contacts c
    WHERE c.first_name ILIKE '%' || pattern || '%'
       OR c.last_name ILIKE '%' || pattern || '%'
       OR c.phone ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;

-- 4. Функция для пагинации (с LIMIT и OFFSET)
CREATE OR REPLACE FUNCTION get_contacts_paginated(
    p_page_number INTEGER,
    p_page_size INTEGER
)
RETURNS TABLE(
    id INTEGER,
    first_name VARCHAR,
    last_name VARCHAR,
    phone VARCHAR,
    total_count BIGINT
) AS $$
DECLARE
    offset_val INTEGER;
BEGIN
    offset_val := (p_page_number - 1) * p_page_size;
    
    RETURN QUERY
    SELECT c.id, c.first_name, c.last_name, c.phone,
           COUNT(*) OVER() AS total_count
    FROM contacts c
    ORDER BY c.id
    LIMIT p_page_size OFFSET offset_val;
END;
$$ LANGUAGE plpgsql;
def search_by_keyword(db_manager, keyword):
    query = """
    SELECT f.title, f.description, a.first_name, a.last_name, c.name AS category 
    FROM film f
    LEFT JOIN film_actor fa ON f.film_id = fa.film_id
    LEFT JOIN actor a ON fa.actor_id = a.actor_id
    LEFT JOIN film_category fc ON f.film_id = fc.film_id
    LEFT JOIN category c ON fc.category_id = c.category_id
    WHERE f.title LIKE %s OR f.description LIKE %s OR a.first_name LIKE %s OR a.last_name LIKE %s OR c.name LIKE %s
    LIMIT 10;
    """
    results = db_manager.execute_query(query, (f"%{keyword}%", f"%{keyword}%", f"%{keyword}%", f"%{keyword}%", f"%{keyword}%"))
    db_manager.insert_query_log('keyword', keyword)
    return results

def search_by_genre_and_year(db_manager, genre, year):
    query = """
    SELECT f.title, f.release_year, c.name AS category, a.first_name, a.last_name 
    FROM film f
    JOIN film_category fc ON f.film_id = fc.film_id
    JOIN category c ON fc.category_id = c.category_id
    LEFT JOIN film_actor fa ON f.film_id = fa.film_id
    LEFT JOIN actor a ON fa.actor_id = a.actor_id
    WHERE c.name = %s AND f.release_year = %s 
    LIMIT 10;
    """
    results = db_manager.execute_query(query, (genre, year))
    db_manager.insert_query_log('genre_year', f"{genre}_{year}")
    return results


def search_by_actor_last_name(db_manager, last_name):
    query = """
    SELECT f.title, f.description, a.first_name, a.last_name, c.name AS category 
    FROM film f
    JOIN film_actor fa ON f.film_id = fa.film_id
    JOIN actor a ON fa.actor_id = a.actor_id
    LEFT JOIN film_category fc ON f.film_id = fc.film_id
    LEFT JOIN category c ON fc.category_id = c.category_id
    WHERE a.last_name = %s 
    LIMIT 10;
    """
    results = db_manager.execute_query(query, (last_name,))
    db_manager.insert_query_log('actor_last_name', last_name)
    return results
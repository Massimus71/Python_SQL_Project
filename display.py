def display_results(results):
    if results:
        for result in results:
            title = result.get('title', 'N/A')
            description = result.get('description', 'N/A')
            release_year = result.get('release_year', 'N/A')
            category = result.get('category', 'N/A')
            first_name = result.get('first_name', 'N/A')
            last_name = result.get('last_name', 'N/A')
            print(f"Title: {title}, Description: {description}, Release Year: {release_year}, Category: {category}, Actor: {first_name} {last_name}")
    else:
        print("Нет результатов для отображения.")

def table_of_contents(chapters):
    for page, chapter in enumerate(chapters, 1):
        print(f"{page:.<5}{chapter:.>10}")
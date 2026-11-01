def get_cats_info(path):
    cats = [] # пустий словник для котів 

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line == "":
                    continue

                parts = line.split(",")
                if len(parts) != 3:
                    print("Неправильний рядок:", line)
                    continue

                cat = {
                    "id": parts[0],
                    "name": parts[1],
                    "age": parts[2]
                }
                cats.append(cat)
    except FileNotFoundError:
        print("Файл не знайдено")
        return []
    except OSError:
        print("Не вдалося прочитати файл")
        return []

    return cats


cats_info = get_cats_info("cats_file.txt")
print(cats_info)

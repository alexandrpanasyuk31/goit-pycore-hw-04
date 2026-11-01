def total_salary(path):
    total = 0 
    count = 0 

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line == "":
                    continue

                parts = line.split(",")
                salary = int(parts[1])

                total += salary
                count += 1
    except FileNotFoundError:
        print("Файл не знайдено")
        return 0, 0
    except ValueError:
        print("У файлі неправильні дані")
        return 0, 0

    if count == 0:
        return 0, 0

    average = total // count
    return total, average


total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

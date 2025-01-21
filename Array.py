def find_duplicates(arr):
    seen = set()
    duplicates = set()

    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return list(duplicates)


numbers = [1, 2, 3, 4, 5, 2, 6, 3, 7, 8, 8]
duplicates = find_duplicates(numbers)
print("Duplicates:", duplicates)
print("list:", list(numbers))
ddddddddddddd
git
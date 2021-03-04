num = int(input())

books = {}

for _ in range(num):
    book = input()

    if book not in books:
        books[book] = 1
    else:
        books[book] += 1

most_sell = max(books.values())

bestsellor = []

for book, number in books.items():
    if number == most_sell:
        bestsellor.append(book)


print(sorted(bestsellor)[0])

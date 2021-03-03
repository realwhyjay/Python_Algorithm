num = int(input())

book = []
max = 0
bestseller = ""
for _ in range(num):
    book.append(input())

book_set = list(set(book[:]))

for i in book_set:
    if max < book.count(book_set[i]):
        bestseller = book_set[i]

print(bestseller)

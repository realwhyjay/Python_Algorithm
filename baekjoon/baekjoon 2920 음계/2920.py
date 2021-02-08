scales = list(map(int, input().split()))

ascending = sorted(scales)

descending = sorted(scales)
descending.reverse()

if scales == ascending:
    print("ascending")
elif scales == descending:
    print("descending")
else:
    print("mixed")

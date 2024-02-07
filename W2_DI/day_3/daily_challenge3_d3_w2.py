data = []
for _ in range(5):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    score = int(input("Enter score: "))
    data.append((name, age, score))
sorted_data = sorted(data, key=lambda x: (x[0], x[1], x[2]))
print(sorted_data)

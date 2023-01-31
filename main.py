import pandas as pd

df = pd.read_excel('file.xlsx')

print(df[df['score'].isnull()])

a = float(input("Enter value for a: "))
b = float(input("Enter value for b: "))
print(df[(df['score'] >= a) & (df['score'] <= b)])

print(df.sort_values('score'))

print(df.sort_values('name'))

name = input("Enter name: ")
score = float(input("Enter score: "))
df = df.append({'name': name, 'score': score}, ignore_index=True)

index = int(input("Enter index to remove: "))
df = df.drop(index)

qualified = df[df['score'] >= 60]
qualified.to_excel('qualified_students.xlsx', columns=['name', 'score'], index=False)

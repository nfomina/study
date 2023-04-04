def top_grade(grades: dict[str, str | list[int]]) -> dict[str, str | int]:
    return {'name': grades['name'], 'top_grade': max(grades['grades'])}


info = {'name': 'Timur', 'grades': [30, 57, 99]}

print(top_grade(info))

print(top_grade({'name': 'Ruslan', 'grades': [19, 48, 86, 45, 32]}))

annotations = top_grade.__annotations__

print(annotations['grades'])

# TEST_8:
print(*top_grade.__annotations__.values())

# # TEST_8:
# dict[str, str | list[int]] dict[str, str | int]
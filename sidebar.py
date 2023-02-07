import pyperclip

names = input("Enter a series of names separated by commas: ").split(",")

result = ""
for name in names:
  name = name.strip().replace(" ", "-")
  result += f"<a href='#{name}-page'>{name}</a>"

pyperclip.copy(result)
print(result)

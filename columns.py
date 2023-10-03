import pyperclip

num_columns = int(input("Enter the number of columns: "))
width_ratios = [float(x.strip()) for x in input("Enter the width ratios separated by commas: ").split(",")]

content = [x.strip() for x in input("Enter the content separated by commas: ").split(",")]

result = "<div style='display: flex;' alt='' >"
for i in range(num_columns):
  result += f"<div style='flex: {width_ratios[i]};' class=''>{content[i]}</div>"
result += "</div>"

pyperclip.copy(result)
print(result)

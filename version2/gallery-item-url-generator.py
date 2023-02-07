import pyperclip
urls = input("Enter a list of URLs separated by commas: ")

url_list = urls.split(",")
output = ""

for url in url_list:
    output += '<div class="gallery-item" style="width:50%" >\n\t\t\t\t\t<img src="' + url.strip() + '">\n\t\t\t\t</div>\n'

print(output)
pyperclip.copy(output)
print("HTML code copied to clipboard.")
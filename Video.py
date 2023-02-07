import pyperclip
urls = input("Enter the url of the video separated by commas: ")

url_list = urls.split(",")
output = ""

for url in url_list:
      
    output += '<div class="responsive-container">'+'<iframe src="'+ url.strip() + '" width="1920" height="1080" frameborder="0" allow="fullscreen" allowfullscreen="" class=""></iframe>'+'</div>\n'

print(output)
pyperclip.copy(output)
print("HTML code copied to clipboard.")
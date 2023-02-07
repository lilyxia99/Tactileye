import pyperclip

template = '<div  class=" project-card Z"id="Y" href="#Y-page" ><img style="width:110%" src="X" alt="Y"></div>'

results = []
while True:
    image_input = input("Enter the image information separated by commas (name, link, type) or type 'done' to finish: ")
    if image_input.lower() == 'done':
        break
    
    name, link, img_type = image_input.split(',')
    result = template.replace('X', link.strip()).replace('Y', name.strip()).replace('Z', img_type.strip())
    results.append(result)
    print(result)

pyperclip.copy("\n".join(results))

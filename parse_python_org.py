import requests

# Get the HTML code of the page
response = requests.get("https://www.python.org")
html = response.text

# Count characters in HTML code
characters = {}
for char in html:
    if char in characters:
        characters[char] += 1
    else:
        characters[char] = 1

# Write the results to the readme.md file
with open("readme.md", "w") as file:
    file.write("The result of counting characters in the HTML code of the page www.python.org:\n\n")
    for char, count in characters.items():
        file.write(f"Character '{char}' occurs {count} times\n")

import webbrowser

with open("urls.txt", "r") as file:
    lines = file.readlines() #turns file into string
    count = 1
    for line in lines:
        print("count: ", count)
        url = line.strip() #strips newline chars 
        webbrowser.open(url, new=2, autoraise=True)
        count += 1

import re


# Create a function to check for integers, later to use it to filter the serial number in the HTML file.
def find_num(s):
    # This pattern indicates the search pattern
    int_pattern = re.compile(r'\b\d+\b')
    """This does the search on every iteration, if the element is an int, it returns True else, it returns False."""
    if int_pattern.search(s):
        return True
    else:
        return False

# I used open here because I don't want to be bothered about closing the file at the end of the operation.
with open("baby2008.html") as name_file:
    # This reads the content of the file.
    data = name_file.read()
    # This is the search pattern.
    td_pattern = re.compile(r'<td>(.*?)</td>', re.DOTALL)
    # This matches the value
    matches = td_pattern.findall(data)
    # An empty list to hold the result of the matches.
    names = []
    # A for loop to loop through the matches
    for i in matches:
        # Here find_num func comes in handy, it discards the iteration if it's an int and retains it if it's not.
        if find_num(i):
            pass
        else:
            names.append(i)

    male_name = []
    female_name = []
    for i in range(len(names)):
        if i % 2 == 0:
            male_name.append(names[i])
        else:
            female_name.append(names[i])
    print(f'Male Name: {male_name}')
    print(f'Female Name: {female_name}')

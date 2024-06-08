with (open("name_file.txt", mode='r') as file):
    data = file.read()
    if '' in data:
        result = data.replace(' ', "\n")
        with open("sorted_names.txt", mode='w') as names:
            names.write(result)
        with open("sorted_names.txt", mode='r') as name_file:
            list_of_name = name_file.readlines()
        i = 0
        for name in list_of_name:
            if i == 0:
                print(f'First name: {name}')
                i += 1
            elif i == 1:
                print(f'Middle name: {name}')
                i += 1
            else:
                print(f'Last name: {name}')


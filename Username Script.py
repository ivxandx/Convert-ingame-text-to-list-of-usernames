# Takes in a string of names and text in the style of name: text and writes each name to a file
# Also prints each name separately to terminal
def username_script(text):
    new_list = text.split()
    new_list2 = []
    final_list = []
    for element in new_list:
        if ':' in element:
            new_list2.append(element)
    for element in new_list2:
        if '.' not in element and element.strip(':') not in final_list:
            with open('Final List', 'a') as username_file:
                username_file.write('\n' + element.strip(':'))
            final_list.append(element.strip(':'))
            print(element.strip(':'))

# Add all the text in between the ''' '''
username_script('''

''')

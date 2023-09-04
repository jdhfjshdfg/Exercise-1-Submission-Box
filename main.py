# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


with open('file_to_read.txt', 'r') as file:
    text = file.read()

    count = text.count("terrible")
    print("“terrible”出现的次数为:", count)

def replace_word(word, index):
    if index % 2 == 0:
        return "pathetic"
    else:
        return "marvellous"

def replace_terrible(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        words = text.split()
        count = 0
        for i in range(len(words)):
            if words[i].strip('.,?!') == "terrible":
                count += 1
                replacement = replace_word("terrible", count)
                words[i] = replacement

        new_text = ' '.join(words)

    with open("result.txt", 'w') as new_file:
        new_file.write(new_text)

file_path = "file_to_read.txt"
replace_terrible(file_path)
import urllib.request

def profanity_check_text(text):
    parsed_text = urllib.parse.quote_plus(text)
    connection = urllib.request.urlopen('http://www.wdylike.appspot.com/?q=' + parsed_text)
    output = connection.read()
    connection.close()
    if "true" in str(output):
        print("Inappropriate word(s) found in text")
    else:
        print("No inappropriate words found")

def profanity_check_lines(lines):
    file_is_clean = True
    for index, line in enumerate(lines):
        parsed_text = urllib.parse.quote_plus(line)
        connection = urllib.request.urlopen('http://www.wdylike.appspot.com/?q=' + parsed_text)
        output = connection.read()
        connection.close()
        if "true" in str(output):
            print("Inappropriate word(s) found in line "
                  + str(index)
                  + ": "
                  + line )
        else:
            file_is_clean = False
    if (file_is_clean == True):
        print("No inappropriate words found")
    

def text_checker():
    #is input from a text file or from the console?
    source = input("Text source is file(F) or console(C)? F/C").lower()
    #check file for profanity
    if source == 'f':
        handle = open("text_for_checking.txt","r")
        text = handle.read()
        handle.close()

        line_info = input("Do you need line information on where profanity is? Y/N?").lower()
        if line_info == 'y':
            lines = text.splitlines()
            profanity_check_lines(lines)
        elif line_info == 'n':
            profanity_check_text(text)
        else:
            print("Invalid input")
        
    elif source == 'c':
        text = input("Input text for checking: ")
        profanity_check_text(text)
    else:
        print("Invalid input")

text_checker()

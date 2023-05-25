command = []
arguments = []
text = []

def steryliseinput(_input):
    if type(_input) == list:
        _input = " ".join(e for e in _input)
        return _input


def get_input(input_prefix="> ", argument_prefix="-"):
    
    global command
    global arguments
    global text

    user_input = input(input_prefix).split()
    
    command = user_input[0]

    for word in user_input:
        
        if argument_prefix in word:
            arguments.append(word)
        
        elif word in command or word in argument_prefix:
            pass

        elif len(command) >= 1 and argument_prefix not in word:
            text.append(word)
        
        else:
            print(f"error for word {word}")



def get_resoult(type,sterylise=False):
    if type == "command":
        content = command

    elif type == "arguments":
        content = arguments

    elif type == "text":
        content = text

    if sterylise and len(content) >= 1:
        to_send = steryliseinput(content)
    
    else:
        to_send = content

    return to_send

def del_input(type):
    
    global command
    global arguments
    global text

    if type == "command":
        command = []

    elif type == "arguments":
        arguments = []

    elif type == "text":
        text = []

    elif type == "all":
        command = []
        arguments = []
        text = []

    else:
        print("Del Error")

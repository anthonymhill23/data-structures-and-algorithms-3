def multi_bracket_validation(input_str):

    stack = []

    for character in input_str:

        if character == "(" or character == "[" or character == "{":
            stack.append(character)
        else:

            if not stack:
                return False
            else:

                top = stack[-1]
                if character == ')' and top == '(' or character == ']' and top == '[' or character == '}' and top == '{':
                    stack.pop()

    if not stack:
        return True
    else:
        return False

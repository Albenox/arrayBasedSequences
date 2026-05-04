# infix_converter.py
# This file contains the InfixToPostfixConverter class.
# This class uses a Stack to convert infix expressions into postfix expressions.

from stack import Stack


class InfixToPostfixConverter:
    def precedence(self, operator):
        # Returns the precedence value of the operator
        if operator in ["*", "/"]:
            return 2
        elif operator in ["+", "-"]:
            return 1
        else:
            return 0

    def convert(self, expression):
        # Creates a stack to hold operators while converting
        stack = Stack()

        # Creates a list to hold the postfix output
        output = []

        # Splits the expression into individual tokens
        tokens = expression.split()

        # Goes through each token in the expression
        for token in tokens:

            # If the token is an operand, add it directly to the output
            if token.isalnum():
                output.append(token)

            # If the token is an opening parenthesis, push it onto the stack
            elif token == "(":
                stack.push(token)

            # If the token is a closing parenthesis, pop until the opening parenthesis
            elif token == ")":
                while not stack.is_empty() and stack.peek() != "(":
                    output.append(stack.pop())

                # Removes the opening parenthesis from the stack
                stack.pop()

            # If the token is an operator, handle precedence
            elif token in ["+", "-", "*", "/"]:
                while (not stack.is_empty() and
                       stack.peek() != "(" and
                       self.precedence(stack.peek()) >= self.precedence(token)):
                    output.append(stack.pop())

                stack.push(token)

        # Pop any remaining operators from the stack
        while not stack.is_empty():
            output.append(stack.pop())

        # Returns the final postfix expression as a string
        return " ".join(output)

    # Temporary test code
if __name__ == "__main__":
    converter = InfixToPostfixConverter()

    print(converter.convert("A + B"))
    print(converter.convert("A + B * C"))
    print(converter.convert("( A + B ) * C"))
    print(converter.convert("A * B + C / D"))
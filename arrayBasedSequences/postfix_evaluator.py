# postfix_evaluator.py
# This file contains the PostfixEvaluator class.
# This class uses a Stack to evaluate postfix expressions.

from stack import Stack


class PostfixEvaluator:
    def evaluate(self, expression):
        # Creates a stack to hold numbers while solving the expression
        stack = Stack()

        # Splits the expression into individual tokens
        tokens = expression.split()

        # Goes through each token in the expression
        for token in tokens:

            # If the token is a number, push it onto the stack
            if token.replace(".", "", 1).isdigit():
                stack.push(float(token))

            # If the token is an operator, pop two numbers and solve
            elif token in ["+", "-", "*", "/"]:
                right = stack.pop()
                left = stack.pop()

                if token == "+":
                    result = left + right
                elif token == "-":
                    result = left - right
                elif token == "*":
                    result = left * right
                elif token == "/":
                    result = left / right

                stack.push(result)

        # The last number left in the stack is the answer
        answer = stack.pop()

        # If the answer is a whole number, return it as an int
        if answer.is_integer():
            return int(answer)

        return answer

    # Test code
if __name__ == "__main__":
    evaluator = PostfixEvaluator()

    print(evaluator.evaluate("5 3 +"))
    print(evaluator.evaluate("8 2 - 3 +"))
    print(evaluator.evaluate("5 3 8 * +"))
    print(evaluator.evaluate("6 2 / 3 +"))
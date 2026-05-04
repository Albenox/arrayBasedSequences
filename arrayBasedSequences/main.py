# main.py
# This file runs both the postfix evaluator and infix converter tests

from postfix_evaluator import PostfixEvaluator
from infix_converter import InfixToPostfixConverter

# Runs postfix to infix conversion test
def run_postfix_tests():
    evaluator = PostfixEvaluator()

    postfix = [
        "5 3 +",
        "8 2 - 3 +",
        "5 3 8 * +",
        "6 2 / 3 +",
        "5 8 + 3 -",
        "5 3 + 8 *",
        "8 2 3 * + 6 -",
        "5 3 8 * + 2 /",
        "8 2 + 3 6 * -",
        "5 3 + 8 2 / -"
    ]

    print("----- Postfix Evaluator -----")

    for expr in postfix:
        result = evaluator.evaluate(expr)
        print(f"[{expr}] = {result}")

# Runs infix to postfix conversion test
def run_infix_tests():
    converter = InfixToPostfixConverter()

    infix = [
        "A + B",
        "A + B * C",
        "( A + B ) * C",
        "A * B + C / D",
        "( A + B ) * ( C - D )",
        "A + B * C - D / E",
        "A * ( B + C ) / D",
        "( A + B * C ) / ( D - E )",
        "A + ( B - C ) * D",
        "( A + B * ( C - D ) ) / E"
    ]

    print("\n----- Infix to Postfix Converter -----")

    for expr in infix:
        result = converter.convert(expr)
        print(f"[{expr}] -> [{result}]")


if __name__ == "__main__":
    run_postfix_tests()
    run_infix_tests()
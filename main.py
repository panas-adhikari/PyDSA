from stack import Stack
from stackPostfixExp import infix_to_postfix, infix_to_prefix, post_pre_to_infix


def main():
    expression = input("Enter a infix expression: ")
    
    #  infix to postfix
    postfix = infix_to_postfix(expression)
    print("Obtained expression Postfix:", postfix)
    
    #        infix to prefix
    prefix = infix_to_prefix(expression)
    print("Obtained expression Prefix:", prefix)
    
    #  postfix back to infix
    final_infix_from_postfix = post_pre_to_infix(postfix, 'postfix')
    print("Converted back to Infix from Postfix:", final_infix_from_postfix)
    
    # prefix back to infix
    final_infix_from_prefix = post_pre_to_infix(prefix, 'prefix')
    print("Converted back to Infix from Prefix:", final_infix_from_prefix)


if __name__ == "__main__":
    main()
    stack = Stack()
    stack.push(1)
    stack.push(3)
    stack.display()
    print("Popped item: ",stack.pop())
    stack.display()
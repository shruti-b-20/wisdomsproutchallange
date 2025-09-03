def insert_sorted(stack, element):
    # Base case: If stack is empty or top of stack <= element
    if not stack or stack[-1] <= element:
        stack.append(element)
        return

    # Otherwise, pop the top element and recur
    temp = stack.pop()
    insert_sorted(stack, element)

    # Push back the popped element
    stack.append(temp)


def sort_stack(stack):
    # Base case: if stack is empty
    if not stack:
        return

    # Remove the top element
    temp = stack.pop()

    # Sort the remaining stack
    sort_stack(stack)

    # Insert the popped element back in sorted order
    insert_sorted(stack, temp)


# -------- Test Cases --------
stack1 = [3, 1, 4, 2]
sort_stack(stack1)
print(stack1)  # [1, 2, 3, 4]

stack2 = [7, 1, 5]
sort_stack(stack2)
print(stack2)  # [1, 5, 7]

stack3 = [5]
sort_stack(stack3)
print(stack3)  # [5]

stack4 = [-3, 14, 8, 2]
sort_stack(stack4)
print(stack4)  # [-3, 2, 8, 14]

stack5 = []
sort_stack(stack5)
print(stack5)  # []

stack6 = [3, 3, 3]
sort_stack(stack6)
print(stack6)  # [3, 3, 3]

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def __str__(self):
        return str(self.items)


def insert_at_bottom(stack, item):
    if stack.is_empty():
        stack.push(item)
    else:
        temp = stack.pop()
        insert_at_bottom(stack, item)
        stack.push(temp)


def reverse_stack(stack):
    if not stack.is_empty():
        temp = stack.pop()
        reverse_stack(stack)
        insert_at_bottom(stack, temp)


s1 = Stack()
for i in [1, 2, 3, 4]:
    s1.push(i)
reverse_stack(s1)
print(s1)

s2 = Stack()
for i in [3, 2, 1]:
    s2.push(i)
reverse_stack(s2)
print(s2)

s3 = Stack()
s3.push(5)
reverse_stack(s3)
print(s3)

s4 = Stack()
for i in [-5, -10, -15]:
    s4.push(i)
reverse_stack(s4)
print(s4)

s5 = Stack()
reverse_stack(s5)
print(s5)

s6 = Stack()
for i in [3, 3, 3]:
    s6.push(i)
reverse_stack(s6)
print(s6)

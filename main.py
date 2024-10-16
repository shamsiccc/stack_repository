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
        raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek from empty stack")

    def size(self):
        return len(self.items)


def is_balanced(sequence):
    stack = Stack()
    brackets = {'(': ')', '{': '}', '[': ']'}

    for char in sequence:
        if char in brackets:  # открывающая скобка
            stack.push(char)
        elif char in brackets.values():  # закрывающая скобка
            if stack.is_empty() or brackets[stack.pop()] != char:
                return "Несбалансированно"

    return "Сбалансированно" if stack.is_empty() else "Несбалансированно"

if __name__ == '__main__':
    input_sequence = input("Введите строку: ")
    print(is_balanced(input_sequence))

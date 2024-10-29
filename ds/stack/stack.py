class Stack:
    def __init__(self) -> None:
        self.stack: list[int] = []

    @property
    def is_empty(self):
        return len(self.stack) == 0

    def push(self, value: int) -> None:
        self.stack.append(value)

    def pop(self) -> int | None:
        if self.is_empty:
            return None
        return self.stack.pop(-1)

    def peak(self) -> int | None:
        if self.is_empty:
            return None
        return self.stack[-1]


if __name__ == "__main__":
    stack = Stack()
    print("stack is_empty:", stack.is_empty)
    for i in range(10):
        stack.push(i)

    for i in range(10):
        print(f"stack[{10 - i - 1}] -> {stack.pop()}")

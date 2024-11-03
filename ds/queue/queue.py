class Queue:
    def __init__(self) -> None:
        self._queue: list[int] = []

    def is_empty(self) -> bool:
        return not self._queue

    def enqueue(self, value: int):
        self._queue.append(value)

    def peak(self) -> None | int:
        if self.is_empty():
            return None
        return self._queue[0]

    def dequeue(self) -> int | None:
        if self.is_empty():
            return None
        return self._queue.pop(0)

import ctypes
import json
import random
from typing import Any


class Pointer:
    """Pointer classs kofti"""

    @staticmethod
    def reference(next: Any) -> int:
        """get &next"""
        return id(next)

    @staticmethod
    def de_reference(memory_id: int) -> Any:
        """dereference the id"""
        return ctypes.cast(memory_id, ctypes.py_object).value  # type: ignore

    __and__ = reference
    __mul__ = de_reference


class JPG:
    def __init__(self, size: tuple[int, int], metadata: dict[str, str]) -> None:
        self.size = size
        self.metadata = metadata
        self.data = [
            [random.randint(0, 255) for _i in range(size[0])] for _j in range(size[1])
        ]

    def __repr__(self) -> str:
        self.metadata["size"] = f"({','.join(map(str, self.size))})"
        return json.dumps(self.metadata, indent=2)

    # def __private_method(self):
    #     pass

    # def _protected_method(self):
    #     pass


jpg = JPG(
    size=(750, 750),
    metadata={
        "photographer": "niloofar",
        "editor": "abolfazl",
        "mal_kie": "attie",
    },
)


# memory_address = Pointer.reference(jpg)  # &jpg
memory_address = Pointer() & jpg
print(f"{memory_address=}")
original_jpg = Pointer() * memory_address  # *jpg
print(f"metadata={original_jpg}")

#!/usr/bin/python3
"""inherits from int"""


class MyInt(int):
    """inverts the operators """
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)

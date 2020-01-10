#!/usr/bin/env python
"""Hello package."""

class Hello:
    @staticmethod
    def say_hello(target) -> None:
        """This function says hello."""
        print(f'Hello {target}')

#!/usr/bin/env python
"""Hello World package."""
from hello.hello import Hello


def main() -> None:
    """This function says hello."""
    Hello.say_hello('World')


if __name__ == '__main__':
    main()
"""Tests for hello."""
import pytest
from hello.hello import Hello
from tests.testlibraries.captured_output import captured_output

class TestHello:
    """Tests for Hello."""
    # pylint: disable=unused-argument
    @staticmethod
    @pytest.mark.parametrize(
        'target, expect', [
            ('world', 'Hello world'),
            ('U.S.A', 'Hello U.S.A'),
        ])
    def test_hello(target, expect):
        """Constructor should leave to load yaml file."""
        with captured_output() as (out, err):
            Hello.say_hello(target)
        # This can go inside or outside the `with` block
        output = out.getvalue().strip()
        assert output == expect

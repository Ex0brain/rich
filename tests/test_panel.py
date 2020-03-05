import io
from rich.console import Console
from rich.panel import Panel

import pytest

tests = [
    Panel("Hello, World"),
    Panel("Hello, World", expand=False),
    Panel("Hello, World", width=8),
    Panel(Panel("Hello, World")),
]

expected = [
    "╭────────────────────────────────────────────────╮\n│Hello, World                                    │\n╰────────────────────────────────────────────────╯\n",
    "╭────────────╮\n│Hello, World│\n╰────────────╯\n",
    "╭──────╮\n│Hello,│\n│World │\n╰──────╯\n",
    "╭────────────────────────────────────────────────╮\n│╭──────────────────────────────────────────────╮│\n││Hello, World                                  ││\n│╰──────────────────────────────────────────────╯│\n╰────────────────────────────────────────────────╯\n",
]


def render(panel, width=50) -> str:
    console = Console(file=io.StringIO(), width=50)
    console.print(panel)
    return console.file.getvalue()


@pytest.mark.parametrize("panel,expected", zip(tests, expected))
def test_render_panel(panel, expected):
    assert render(panel) == expected


def test_console_width():
    console = Console(file=io.StringIO(), width=50)
    panel = Panel("Hello, World", expand=False)
    min_width, max_width = panel.__console_width__(50)
    assert min_width == 14
    assert max_width == 14


def test_console_width_expand():
    console = Console(file=io.StringIO(), width=50)
    panel = Panel("Hello, World")
    min_width, max_width = panel.__console_width__(50)
    assert min_width == 50
    assert max_width == 50


if __name__ == "__main__":
    expected = []
    for panel in tests:
        result = render(panel)
        print(result)
        expected.append(result)
    print("--")
    print()
    print(f"expected={repr(expected)}")


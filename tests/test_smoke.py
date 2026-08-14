__author__ = "Shuvam Banerji Seal"

import ch4114


def test_version_exists() -> None:
    assert isinstance(ch4114.__version__, str)
    assert ch4114.__version__  # non-empty

from typing import List
from pathlib import Path
from chubut.pipeline import collect


def main() -> None:
    resources: List[str] = [
        str(Path("~/Info/chubut/alpha/3603881.pdf").expanduser()),
        str(Path("~/Info/chubut/alpha/3643218.pdf").expanduser()),
        str(Path("~/Info/chubut/alpha/3717649.pdf").expanduser()),
        str(Path("~/Info/chubut/alpha/5656787.pdf").expanduser()),
        str(Path("~/Info/chubut/alpha/6786787.pdf").expanduser()),
        str(Path("~/Info/chubut/alpha/7898798.pdf").expanduser()),
    ]

    collect(resources, str(Path("~/Info/chubut/alpha/").expanduser()))


if __name__ == "__main__":
    main()

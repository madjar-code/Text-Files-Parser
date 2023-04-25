from typing import (
    TypeAlias,
)
from pathlib import Path
from django.conf import settings


PathStr: TypeAlias = str

RESUME_DIR: PathStr = f'{settings.BASE_DIR}/files/'
FILE_NAME: str = 'Resume {}.txt'
NUMBER_OF_RESUME: int = 5

class ResumeParser:
    def run_parser(self) -> None:
        id: int = 1
        while id <= NUMBER_OF_RESUME:
            resume_path = Path(
                f'{RESUME_DIR}/{FILE_NAME.format(str(id))}')
            print(resume_path)

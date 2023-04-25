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
            filename: str = FILE_NAME.format(str(id))
            resume_path = Path(f'{RESUME_DIR}/{filename}')
            with resume_path.open('r', encoding='utf-8') as resume_file:
                for line in resume_file.readlines():
                    print(line)
            id += 2

from typing import (
    TypeAlias,
    Tuple,
    List,
)
from pathlib import Path
from django.conf import settings


PathStr: TypeAlias = str
ProfNameType: TypeAlias = str
TimeType: TypeAlias = str
NameTimeType: TypeAlias =\
    Tuple[ProfNameType,TimeType]

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
                result: List[NameTimeType] =\
                    self._parse_file(resume_file.readlines())
            id += 2

    def _parse_file(self, lines: List[str]) -> List[NameTimeType]:
        result_list: List[NameTimeType] = []
        for i in range(0, len(lines), 3):
            name: str = lines[i].rstrip()
            time: str = lines[i+1].rstrip()
            name_and_time: NameTimeType = (name, time)
            result_list.append(name_and_time)
        return result_list

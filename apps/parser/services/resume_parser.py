from typing import (
    TypeAlias,
    Tuple,
    List,
)
from pathlib import Path
from django.conf import settings
from parser.models import\
    ResumeData, PositionTime


PathStr: TypeAlias = str
ProfNameType: TypeAlias = str
TimeType: TypeAlias = str
NameTimeType: TypeAlias =\
    Tuple[ProfNameType,TimeType]

RESUME_DIR: PathStr = f'{settings.BASE_DIR}/files/'
FILE_NAME: str = 'Resume {}.txt'
NUMBER_OF_RESUME: int = 5
LINE_STEP: int = 3
RESUME_STEP: int = 2


class ResumeParser:
    def run_parser(self, start_index: int = 1) -> None:
        id: int = start_index

        while id <= NUMBER_OF_RESUME:
            filename: str = FILE_NAME.format(str(id))
            resume_path = Path(f'{RESUME_DIR}/{filename}')

            if not ResumeData.objects.filter(link=resume_path).exists():
                resume_data = ResumeData.objects.create(link=resume_path)
                with resume_path.open('r', encoding='utf-8') as resume_file:
                    self._create_data(resume_data, resume_file.readlines())
                id += RESUME_STEP
            else:
                id += 1
                continue

    def _create_data(self, resume: ResumeData, lines: List[str]) -> None:
        for i in range(0, len(lines), LINE_STEP):
            name, time = self._parse_string(lines=lines, str_id=i)
            PositionTime.objects.create(resume=resume, position=name, time=time)  

    def _parse_string(self, lines: List[str], str_id: int) -> NameTimeType:
        name: str = lines[str_id].rstrip()
        time: str = lines[str_id+1].rstrip()
        return (name, time)

    def _parse_file(self, lines: List[str]) -> List[NameTimeType]:
        result_list: List[NameTimeType] = []
        for i in range(0, len(lines), 3):
            name: str = lines[i].rstrip()
            time: str = lines[i+1].rstrip()
            name_and_time: NameTimeType = (name, time)
            result_list.append(str(name_and_time))
        return result_list

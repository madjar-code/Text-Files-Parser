import time
from typing import (
    TypeAlias,
    Tuple,
    List,
)
from pathlib import Path
from django.conf import settings
from parser.models import ResumeData


PathStr: TypeAlias = str
ProfNameType: TypeAlias = str
TimeType: TypeAlias = str
NameTimeType: TypeAlias =\
    Tuple[ProfNameType,TimeType]

RESUME_DIR: PathStr = f'{settings.BASE_DIR}/files/'
FILE_NAME: str = 'Resume {}.txt'
NUMBER_OF_RESUME: int = 5


STATUSES = ResumeData.Status

class ResumeParser:
    def run_parser(self, start_index: int = 1) -> None:
        id: int = start_index
        while id <= NUMBER_OF_RESUME:
            filename: str = FILE_NAME.format(str(id))
            resume_path = Path(f'{RESUME_DIR}/{filename}')

            if not ResumeData.objects.filter(link=resume_path).exists():
                resume_data = ResumeData(link=resume_path,
                                        status=STATUSES.DURING)
                with resume_path.open('r', encoding='utf-8') as resume_file:
                    result: List[NameTimeType] =\
                        self._parse_file(resume_file.readlines())
                    resume_data.data: List[NameTimeType] = result
                    resume_data.status = STATUSES.READY
                    resume_data.save()
                    print(resume_data.data)
                    time.sleep(5)
                id += 2
            else:
                id += 2
                continue

    def _parse_file(self, lines: List[str]) -> List[NameTimeType]:
        result_list: List[NameTimeType] = []
        for i in range(0, len(lines), 3):
            name: str = lines[i].rstrip()
            time: str = lines[i+1].rstrip()
            name_and_time: NameTimeType = (name, time)
            result_list.append(str(name_and_time))
        return result_list

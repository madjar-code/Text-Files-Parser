from django.core.management.base import\
    BaseCommand, CommandParser
from parser.services.resume_parser import ResumeParser

class Command(BaseCommand):
    help = 'Start file parser'
    
    def add_arguments(self, parser: CommandParser) -> None:
        DEFAULT_QTY: int = 1
        qty_hint = 'The number of parser processes'
        parser.add_argument('--parsers', default=DEFAULT_QTY,
                            type=int, help=qty_hint)

        DEFAULT_ID: int = 1
        id_hint = 'The index of start resume'
        parser.add_argument('--id', default=DEFAULT_ID,
                            type=int, help=id_hint)
    
    def handle(self, *args, **kwargs) -> None:
        resume_parser = ResumeParser()
        start_index: int = kwargs['id']
        resume_parser.run_parser(start_index)

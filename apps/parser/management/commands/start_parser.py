from django.core.management.base import\
    BaseCommand, CommandParser
from parser.services.resume_parser import ResumeParser

class Command(BaseCommand):
    help = 'Start file parser'
    
    def add_arguments(self, parser: CommandParser) -> None:
        DEFAULT_QTY: int = 1
        block_hint = 'The number of parser processes'
        parser.add_argument('--parsers', default=DEFAULT_QTY,
                            type=int, help=block_hint)
    
    def handle(self, *args, **kwargs) -> None:
        resume_parser = ResumeParser()
        resume_parser.run_parser()

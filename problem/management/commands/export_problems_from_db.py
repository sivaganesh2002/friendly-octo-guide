from django.core.management.base import BaseCommand
from problem.models import Problem
import os

class Command(BaseCommand):
    help = 'Export all problem descriptions from the DB to exported_problems/problem_<id>.md files.'

    def handle(self, *args, **kwargs):
        output_dir = 'exported_problems'
        os.makedirs(output_dir, exist_ok=True)
        exported = 0
        for problem in Problem.objects.all():
            md_path = os.path.join(output_dir, f'problem_{problem.id}.md')
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(problem.description or '')
                exported += 1
        self.stdout.write(self.style.SUCCESS(f'Exported {exported} problems to markdown files.'))

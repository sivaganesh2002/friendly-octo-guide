from django.core.management.base import BaseCommand
from problem.models import Problem
import os

class Command(BaseCommand):
    help = 'Bulk update problem descriptions from exported_problems/problem_<id>.md files.'

    def handle(self, *args, **kwargs):
        input_dir = 'exported_problems'
        updated = 0
        for problem in Problem.objects.all():
            md_path = os.path.join(input_dir, f'problem_{problem.id}.md')
            if os.path.exists(md_path):
                with open(md_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    problem.description = content
                    problem.save()
                    updated += 1
                self.stdout.write(f'Updated problem {problem.id} from {md_path}')
            else:
                self.stdout.write(f'File not found for problem {problem.id}: {md_path}')
        self.stdout.write(self.style.SUCCESS(f'Updated {updated} problems from markdown files.'))

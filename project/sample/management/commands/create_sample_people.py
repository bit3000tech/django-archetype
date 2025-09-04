"""
Management command to create sample data for testing
"""
from django.core.management.base import BaseCommand, CommandError
from project.sample.models import Person


class Command(BaseCommand):
    help = 'Create sample people for testing purposes'

    def add_arguments(self, parser):
        parser.add_argument(
            '--count',
            type=int,
            default=5,
            help='Number of sample people to create (default: 5)',
        )
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear existing people before creating new ones',
        )

    def handle(self, *args, **options):
        count = options['count']
        
        if options['clear']:
            Person.objects.all().delete()
            self.stdout.write(
                self.style.WARNING('Cleared existing people from database')
            )
        
        # Sample data
        sample_people = [
            ('John', 'Doe', 'john.doe@example.com'),
            ('Jane', 'Smith', 'jane.smith@example.com'),
            ('Bob', 'Johnson', 'bob.johnson@example.com'),
            ('Alice', 'Brown', 'alice.brown@example.com'),
            ('Charlie', 'Wilson', 'charlie.wilson@example.com'),
            ('Diana', 'Davis', 'diana.davis@example.com'),
            ('Frank', 'Miller', 'frank.miller@example.com'),
            ('Grace', 'Garcia', 'grace.garcia@example.com'),
            ('Henry', 'Martinez', 'henry.martinez@example.com'),
            ('Ivy', 'Rodriguez', 'ivy.rodriguez@example.com'),
        ]
        
        created_count = 0
        for i in range(min(count, len(sample_people))):
            first_name, last_name, email = sample_people[i]
            
            # Check if person already exists
            if not Person.objects.filter(email=email).exists():
                Person.objects.create(
                    first_name=first_name,
                    last_name=last_name,
                    email=email
                )
                created_count += 1
                self.stdout.write(f'Created: {first_name} {last_name}')
            else:
                self.stdout.write(
                    self.style.WARNING(f'Skipped: {email} already exists')
                )
        
        if created_count > 0:
            self.stdout.write(
                self.style.SUCCESS(
                    f'Successfully created {created_count} sample people'
                )
            )
        else:
            self.stdout.write(
                self.style.WARNING('No new people were created')
            )

from django.core.management.base import BaseCommand
from sqlalchemy import create_engine, MetaData
from eralchemy import render_er

class Command(BaseCommand):
    help = 'Generates a database ERD diagram'

    def handle(self, *args, **kwargs):
        try:
            # Connect to the Django SQLite3 database using SQLAlchemy
            engine = create_engine('sqlite:///db.sqlite3')
            metadata = MetaData()
            metadata.reflect(bind=engine)

            # Generate the ER diagram
            render_er(metadata, 'erd_diagram.png')
            
            self.stdout.write(self.style.SUCCESS('Successfully generated ER diagram: erd_diagram.png'))
        
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error generating ER diagram: {e}"))
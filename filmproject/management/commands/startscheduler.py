from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore, register_events
from filmproject.cron_jobs import scheduler

class Command(BaseCommand):
    help = "Starts the APScheduler."

    def handle(self, *args, **options):
        # Add Django job store and register events
        scheduler.add_jobstore(DjangoJobStore(), 'default')
        register_events(scheduler)
        scheduler.start()
        self.stdout.write(self.style.SUCCESS("APScheduler started successfully."))
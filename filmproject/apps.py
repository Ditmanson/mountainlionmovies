from django.apps import AppConfig
from django.conf import settings

# class FilmprojectConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'filmproject'

#     def ready(self):
#         import filmproject.signals  # Import signals to register them
#         from filmproject.cron_jobs import start_scheduler
#         from django.db import connections
#         from django.db.migrations.executor import MigrationExecutor
#         from django.core.exceptions import ImproperlyConfigured

        # Check if there are pending migrations
        # connection = connections['default']
        # try:
        #     executor = MigrationExecutor(connection)
        #     if executor.migration_plan(executor.loader.graph.leaf_nodes()):
        #         print("Pending migrations detected. Skipping scheduler start.")
        #         return  # Skip starting the scheduler if migrations are pending
        # except ImproperlyConfigured:
        #     print("Database not ready. Skipping scheduler start.")
        #     return

        # Start the scheduler only if it's not already running
        # if not getattr(settings, 'SCHEDULER_RUNNING', False):
        #     start_scheduler()  # Use the start_scheduler function from cron_jobs.py
        #     settings.SCHEDULER_RUNNING = True
        #     print("Scheduler started successfully from apps.py.")
        # else:
        #     print("Scheduler already running. Skipping start.")
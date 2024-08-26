from django.apps import AppConfig


class IziskillConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'iziskill'



def ready(self):
        import iziskill.signals  # Importation des  fichier des signaux
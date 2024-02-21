from django.db import models


# Comunicação com BD. herdando Model de models, importada acima
class Todo(models.Model):
    # campos do TO DO. Traz os tipos de campos e argumentos para configuração
    title = models.CharField(
        verbose_name="Título", max_length=100, null=False, blank=False
    )
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    deadline = models.DateField(verbose_name="Data de entrega", null=True)
    finished_at = models.DateField(null=True)

from django.db import models

class WebScraping(models.Model):
    filter = models.TextField()
    website = models.URLField()

    def __str__(self) -> str:
        return f'{self.filter} from {self.website}'
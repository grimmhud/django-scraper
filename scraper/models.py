from django.db import models

class ScrapingResult(models.Model):
    csv_values = models.JSONField()
    
    @classmethod
    def create(cls, values):
        return cls(csv_values=values)

    def __str__(self) -> str:
        return self.csv_values

class ScrapingSearch(models.Model):
    filter = models.TextField()
    website = models.URLField()
    scraping_result = models.OneToOneField(ScrapingResult, on_delete=models.CASCADE, primary_key=True)
    
    @classmethod
    def create(cls, website, filter, result_id):
        return cls(website=website, filter=filter, scraping_result=result_id)

    def __str__(self) -> str:
        return f'{self.filter} from {self.website}'
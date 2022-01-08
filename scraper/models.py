from django.db import models
from datetime import datetime
from django.utils import timezone

class ScrapingResult(models.Model):
    values = models.JSONField()
    created_at = models.DateTimeField(default=timezone.now)
    
    @classmethod
    def create(cls, values):
        return cls(values=values, created_at=timezone.now())

    def __str__(self) -> str:
        return f'id: {self.id} created_at: {self.created_at} {self.values}'

class ScrapingSearch(models.Model):
    filter = models.TextField()
    website = models.URLField()
    created_at = models.DateTimeField(default=timezone.now)
    scraping_result = models.OneToOneField(ScrapingResult, on_delete=models.CASCADE)
    
    @classmethod
    def create(cls, website, filter, result_id):
        return cls(website=website, filter=filter, scraping_result=result_id, created_at=timezone.now())

    def __str__(self) -> str:
        return f'id: {self.id} created_at: {self.created_at} website: {self.website} '
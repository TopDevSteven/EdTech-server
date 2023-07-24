from django.db import models

# Create your models here.
class Document(models.Model):
    DOC = 'DOC'
    PDF = 'PDF'
    CSV = 'CSV'
    WEB = "WEB"

    DOCUMENT_TYPE = [
        (DOC, 'DOC'),
        (PDF, 'PDF'),
        (CSV, 'CSV'),
        (WEB, 'WEB')
    ]
    user_id = models.IntegerField()
    document_type = models.CharField(max_length=10, choices=DOCUMENT_TYPE, default=PDF)
    date = models.CharField(max_length=20)
    topic = models.CharField(max_length=100)

    def __str__(self):
        return self.document_type
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
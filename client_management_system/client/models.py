from django.db import models


class ClientInfo(models.Model):

    status = [
        ('Onboard', 'Onboard'),
        ('NotOnboard', 'NotOnboard'),
        ]

    project = [
        ('SAAS', 'SAAS'),
        ('Ecommerce','Ecommerce' ),
        ('CRM', 'CRM'),
        ('ERM', 'ERM'),
        ('Finance','Finance')
    ]
    cid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    company = models.CharField(max_length=30)
    email_id = models.EmailField()
    department = models.CharField(max_length=30)
    date_of_joining = models.DateField()
    status = models.CharField(max_length=30, choices=status)
    projectDomain = models.CharField(max_length=50, choices=project)

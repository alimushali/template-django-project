from django.db import models

# Create your models here.
class AbstractUnit1(models.Model):
    name = models.TextField()
    description = models.TextField()
    integer_property = models.IntegerField()


    class Meta:
        table_name="abstract_unit_1"


class LinkedUnit1(models.Model):
    abstract_unit_id = models.ForeignKey(
        AbstractUnit1,
        primary_key=True
    )
    name = models.TextField()
    description = models.TextField()
    integer_property = models.IntegerField()
    numeric_property = models.DecimalField()

    class Meta:
        table_name="linked_unit_1"


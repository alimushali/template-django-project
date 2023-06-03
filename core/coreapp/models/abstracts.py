from django.db import models

# Create your models here.
class AbstractUnit1(models.Model):
    name = models.TextField()
    description = models.TextField()
    integer_property = models.IntegerField()


    class Meta:
        db_table="coreapp_abstract_unit_1"


class LinkedUnit1(models.Model):
    abstract_unit = models.ForeignKey(
        AbstractUnit1,
        on_delete=models.CASCADE
    )
    name = models.TextField()
    description = models.TextField()
    integer_property = models.IntegerField()
    numeric_property = models.DecimalField(max_digits=19, decimal_places=10)

    class Meta:
        db_table="coreapp_linked_unit_1"

from tortoise.models import Model
from tortoise import fields


class TokenPrices(Model):
    id = fields.IntField(pk=True, unique=True)

    name_token = fields.CharField(max_length=10)
    price = fields.CharField(max_length=15)
    data = fields.CharField(max_length=80)

    def __str__(self):
        return self.name_token

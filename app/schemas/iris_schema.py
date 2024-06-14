# app/schemas/iris_schema.py
from marshmallow import Schema, fields, validate, ValidationError

class IrisSchema(Schema):
    sepal_length = fields.Float(required=True, validate=validate.Range(min=0))
    sepal_width = fields.Float(required=True, validate=validate.Range(min=0))
    petal_length = fields.Float(required=True, validate=validate.Range(min=0))
    petal_width = fields.Float(required=True, validate=validate.Range(min=0))

def validate_iris_data(data):
    schema = IrisSchema()
    errors = schema.validate(data)
    if errors:
        raise ValidationError(errors)
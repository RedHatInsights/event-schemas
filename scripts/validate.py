import os.path
from json import loads

import sys

import click
import jsonschema


def get_schema(uri):
    path = os.path.join('schemas', os.path.basename(uri))
    with open(path) as content:
        return loads(content.read())


def validate(schema_uri):
    instance = loads(sys.stdin.read())
    schema_store = { 'https://console.redhat.com/api/schemas/' + key: get_schema(key) for key in os.listdir('schemas') }
    resolver = jsonschema.validators.RefResolver("", {}, store=schema_store)
    validator = jsonschema.validators.Draft7Validator(schema_store[schema_uri], resolver=resolver)
    validator.validate(instance=instance)
    if 'dataschema' in instance:
        validator = jsonschema.validators.Draft7Validator(schema_store[instance['dataschema']], resolver=resolver)
        validator.validate(instance=instance['data'])

if __name__ == '__main__':
    validate('https://console.redhat.com/api/schemas/events.json')

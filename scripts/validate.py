#!/usr/bin/env python
import os.path
from json import loads
import sys
import jsonschema


def get_schema(path):
    with open(path) as content:
        return loads(content.read())


def validate(schema_uri):
    instance = loads(sys.stdin.read())
    schema_store = {}
    for dir, subdirs, files in os.walk("schemas"):
        for file in files:
            if file.endswith(".json"):
                path = dir + "/" + file
                schema = get_schema(path)
                schema_store[schema["$id"]] = schema
    resolver = jsonschema.validators.RefResolver("", {}, store=schema_store)
    validator = jsonschema.validators.Draft7Validator(
        schema_store[schema_uri], resolver=resolver
    )
    errors = list(validator.iter_errors(instance))
    if "dataschema" in instance:
        validator = jsonschema.validators.Draft7Validator(
            schema_store[instance["dataschema"]], resolver=resolver
        )
        errors += list(validator.iter_errors(instance['data']))
    for message in [error.message for error in errors]:
        print(f"❌ {message}")
    if len(errors) == 0:
        print("✅ Validation passed!")


if __name__ == "__main__":
    validate("https://console.redhat.com/api/schemas/events/v1/events.json")

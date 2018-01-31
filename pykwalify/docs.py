# -*- coding: utf-8 -*-

""" pyKwalify - docs.py """

import inflection
import os
import pkg_resources
import mako.template
import yaml
import yamlordereddictloader
from collections import OrderedDict


def generate_docs(schema, output=None):

    if not output:
        output = "."

    examples = generate_examples(schema)

    with open('schema-example.yaml', 'w') as file:
        yaml.dump(examples, file, Dumper=yamlordereddictloader.Dumper, default_flow_style=False)


def generate_examples(schema):

    if schema['type'] == 'map':
        examples = OrderedDict()
        for entry in schema['mapping']:
            example = generate_examples(schema['mapping'][entry])
            if example is not None:
                examples[entry] = example

        if len(examples):
            return examples
    elif schema['type'] == 'seq':
        examples = []
        for entry in schema['sequence']:
            examples.append(generate_examples(entry))

        if len(examples):
            return examples
    else:
        if 'example' in schema:
            if schema['type'] == 'int':
                return int(schema['example'])
            else:
                return schema['example']

    return None
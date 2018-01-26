# -*- coding: utf-8 -*-

""" pyKwalify - classes.py """

import inflection
import pkg_resources
import mako.template

def generate_classes(schema):

    if schema['type'] == 'map':

        imports = []
        for (name, entry) in schema['mapping'].iteritems():
            imports += _find_imports(entry)

        with open(pkg_resources.resource_filename('pykwalify', 'data/python_classes.template')) as f:
            template = f.read()

            class_name = schema['class']
            class_filename = "{0}.py".format(inflection.underscore(class_name))
            with open(class_filename, 'w') as class_file:

                class_file.write((mako.template.Template(template).render(
                    imports=imports,
                    items=schema['mapping'],
                    class_name=class_name)))

        for (name, mapping) in schema['mapping'].iteritems():
            generate_classes(mapping)

    elif schema['type'] == 'seq':
        generate_classes(schema['sequence'][0])


def _find_imports(schema):
    imports = []

    if schema['type'] == 'map':
        imports.append((
            inflection.underscore(schema['class']),
            schema['class']))

    elif schema['type'] == 'seq':
        entry = schema['sequence'][0]

        imports += _find_imports(entry)

    return imports

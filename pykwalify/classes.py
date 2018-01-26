# -*- coding: utf-8 -*-

""" pyKwalify - classes.py """

import inflection
import pkg_resources
import mako.template

def generate_classes(schema):

    if schema['type'] == 'map':
        # template_values = _generate_template_values(schema)
        # print template_values

        with open(pkg_resources.resource_filename('pykwalify', 'data/python_classes.template')) as f:
            template = f.read()

            class_name = schema['class']
            class_filename = "{0}.py".format(inflection.underscore(class_name))
            with open(class_filename, 'w') as class_file:

                class_file.write((mako.template.Template(template).render(
                    items=schema['mapping'],
                    class_name=class_name)))

        for (name, mapping) in schema['mapping'].iteritems():
            generate_classes(mapping)

    # elif schema['type'] == 'seq':
    #     for entry in schema['sequence']:
    #         generate_classes(entry)


# def _generate_template_values(schema):

#     class_name = schema['class']

#     template_values = {
#         'class': class_name,
#         'maps': [],
#         'seqs': [],
#         'simple': [],
#     }

#     for (name, entry) in schema['mapping'].iteritems():
#         print "{0} {1}".format(name, entry['type'])

#         if entry['type'] == "map":
#             template_values['maps'].append({
#                 'name': name,
#                 'class': entry['class']
#             })

#         elif entry['type'] == "seq":
#             assert(len(entry['sequence']) == 1)

#             template_values['seqs'].append({
#                 'name': name,
#                 'entries': _generate_template_values(entry['sequence'][0])
#             })

#         else:
#             template_values['simple'].append({
#                 'name': name,
#                 'default': entry.get('default'),
#             })

#     return template_values
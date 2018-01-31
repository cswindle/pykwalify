import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.md') as f:
    readme = f.read()
with open(os.path.join('docs', 'release-notes.rst')) as f:
    history = f.read()

setup(
    name="pykwalify",
    version="1.6.0-3",
    description='Python lib/cli for JSON/YAML schema validation',
    long_description=readme + '\n\n' + history,
    author="Johan Andersson",
    author_email="Grokzen@gmail.com",
    maintainer='Johan Andersson',
    maintainer_email='Grokzen@gmail.com',
    license='MIT',
    packages=['pykwalify'],
    package_dir={'pykwalify': 'pykwalify'},
    package_data={'pykwalify': ['data/*.template']},
    url='http://github.com/grokzen/pykwalify',
    extras_require={
        'ruamel': ["ruamel.yaml>=0.11.0,<0.12.0"],
    },
    entry_points={
        'console_scripts': [
            'pykwalify = pykwalify.cli:cli_entrypoint',
        ],
    },
    install_requires=[
        'docopt>=0.6.2',
        'PyYAML>=3.11',
        'python-dateutil>=2.4.2',
        'inflection>=0.3.1',
        'Mako>=1.0.7',
        'yamlordereddictloader>=0.4.0',
    ],
    classifiers=(
        # 'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        # 'Development Status :: 4 - Beta',
        'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    )
)

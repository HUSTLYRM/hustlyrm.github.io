# Configuration file for the Sphinx documentation builder.
project = 'CodeHelper'
copyright = '2024, '
author = 'Sango'
release = '1.0.2.0'
version = '1.0.2.0'

extensions = [ 
    'breathe',
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages'
]

templates_path = ['_templates']
exclude_patterns = []
language = 'zh_CN'
html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
breathe_default_project = "CodeHelper"

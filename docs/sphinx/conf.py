import os
import sys

sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.abspath('../..'))
sys.path.insert(0, os.path.abspath('../../rtdtest'))

extensions = [
    'sphinx.ext.autodoc',
]

# Add any other necessary configurations

# -- Project information -----------------------------------------------------

project = 'Read The Docs Test'
author = 'Felipe Santana'



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'

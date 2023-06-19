import os
import sys
from pathlib import Path

#sys.path.insert(0, os.path.abspath('../..'))
#sys.path.insert(0, Path(os.path.abspath(__file__)).parent.parent.parent.absolute())

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

"""Sphinx configuration."""
project = "Oliver_Huber"
author = "Oliver Huber"
copyright = "2022, Oliver Huber"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
    "sphinx.ext.viewcode",
]
autodoc_typehints = "description"
html_theme = "furo"

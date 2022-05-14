# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath("../.."))

from sphinx.builders.html import StandaloneHTMLBuilder

import saliency_metrics

# -- Project information -----------------------------------------------------

project = "saliency-metrics"
copyright = "2022, Yawei Li"
author = "Yawei Li"

# The full version, including alpha/beta/rc tags
release = saliency_metrics.__version__

version = saliency_metrics.__version__


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_parser",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.autosectionlabel",
    "sphinx_autodoc_typehints",
]

autoclass_content = "class"
add_module_names = True
source_encoding = "utf-8"
autosectionlabel_prefix_document = True
napoleon_use_param = True
napoleon_include_init_with_doc = False
set_type_checking_flag = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

# The master toctree document.
master_doc = "index"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_title = f"{project} {version} Documentation"
html_theme = "pydata_sphinx_theme"
html_context = {"default_mode": "auto"}
html_theme_options = {
    "icon_links": [
        {"name": "GitHub", "url": "https://github.com/sandylaker/saliancy-metrics", "icon": "fab fa-github-square"},
    ],
    "collapse_navigation": True,
    "navigation_depth": 3,
    "show_toc_level": 1,
    "footer_items": ["copyright"],
    "navbar_align": "content",
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]


# set priority when building html
StandaloneHTMLBuilder.supported_image_types = ["image/svg+xml", "image/gif", "image/png", "image/jpeg"]
# -- Extension configuration -------------------------------------------------
# Ignore >>> when copying code
copybutton_prompt_text = r">>> |\.\.\. "
copybutton_prompt_is_regexp = True

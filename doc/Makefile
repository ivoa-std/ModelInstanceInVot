# ivoatex Makefile.  The ivoatex/README for the targets available.

# short name of your document (edit $DOCNAME.tex; would be like RegTAP)
DOCNAME = mivot

# count up; you probably do not want to bother with versions <1.0
DOCVERSION = 1.0

# Publication date, ISO format; update manually for "releases"
DOCDATE = 2022-10-05

# What is it you're writing: NOTE, WD, PR, REC, PEN, or EN
DOCTYPE = PR

# An e-mail address of the person doing the submission to the document
# repository (can be empty until a make upload is being made)
AUTHOR_EMAIL=laurent.michel@astro.unistra.fr

# Source files for the TeX document (but the main file must always
# be called $(DOCNAME).tex
SOURCES = $(DOCNAME).tex role_diagram.pdf appendix*.tex element*tex\
	introduction.tex syntax.tex api.tex validation.tex

# List of image files to be included in submitted package (anything that
# can be rendered directly by common web browsers)
FIGURES = role_diagram.svg

# List of PDF figures (figures that must be converted to pixel images to
# work in web browsers).
VECTORFIGURES =

# Additional files to distribute (e.g., CSS, schema files, examples...)
AUX_FILES = ../schema/xsd/mivot-v1.0.xsd

include ivoatex/Makefile

# Valid some XML snippets against both VOTable and MIVOT schemas
valid_snippet:
	# Install the Python validator
	pip3 install git+https://github.com/ivoa/mivot-validator.git#egg=mivot-validator
	# Remove the escaped _ required by latex to have links from and to the code block 
	sed -e s/\\\\_/_/g appendix_D.xml  > nobackslash_appendix_D.xml
	# validate
	mivot-validate  nobackslash_appendix_D.xml
	# clean up
	rm nobackslash_appendix_D.xml
# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SPHINXDOC   ?= sphinx-apidoc
SOURCEDIR     = source
PACKAGEDIR    = ../datastructs
BUILDDIR      = ../../sphinxdoc-test-docs
	

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

package:
	rm $(SOURCEDIR)/*.rst
	@$(SPHINXDOC) -o $(SOURCEDIR) $(PACKAGEDIR)
	mv $(SOURCEDIR)/modules.rst $(SOURCEDIR)/index.rst
	make html

buildandcommithtml: html
	cd $(BUILDDIR)/html; git add . ; git commit -m "rebuilt docs"; git push origin gh-pages

make packageandpublish:
	make package
	make buildandcommithtml

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

PDFLATEX ?= pdflatex
BIBER ?= biber

ifndef V
Q = @
RUN = >$@.build.log 2>&1 || { cat $@.build.log; exit 1; }
else
Q =
RUN =
endif

.PHONY: all build clean

all: thesis.pdf
build: thesis.pdf

thesis.pdf: thesis.tex refs.bib abstract.tex appendix.tex chapter_*.tex eth-template/*.tex
	$(Q)$(PDFLATEX) -interaction=nonstopmode -file-line-error thesis.tex $(RUN)
	$(Q)$(BIBER) thesis $(RUN)
	$(Q)$(PDFLATEX) -interaction=nonstopmode -file-line-error thesis.tex $(RUN)
	$(Q)$(PDFLATEX) -interaction=nonstopmode -file-line-error thesis.tex $(RUN)

clean:
	rm -f thesis.aux thesis.bbl thesis.bcf thesis.blg thesis.fdb_latexmk thesis.fls thesis.log thesis.out thesis.run.xml thesis.thm thesis.toc thesis.pdf
	rm -f thesis.lof thesis.lol thesis.lot thesis.synctex.gz thesis.pdf.build.log

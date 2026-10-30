proposal.pdf: proposal.tex
	latexmk -pdfxe -shell-escape -interaction=nonstopmode $<

midterm.pdf: midterm.tex $(shell find src/midterm -name '*.tex') reference.bib
	latexmk -pdfxe -shell-escape -interaction=nonstopmode $<

midterm-with-cover.pdf: resource/midterm-cover.pdf midterm.pdf
	pdfunite resource/midterm-cover.pdf midterm.pdf midterm-with-cover.pdf

proposal-with-cover.pdf: resource/proposal-cover.pdf proposal.pdf
	pdfunite resource/proposal-cover.pdf proposal.pdf proposal-with-cover.pdf

clean:
	latexmk -CA
.PHONY: pptx
PYTHON ?= python3
pptx:
	$(PYTHON) scripts/build_midterm_pptx.py

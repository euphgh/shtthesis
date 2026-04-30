proposal.pdf: proposal.tex
	latexmk -pdfxe -shell-escape -interaction=nonstopmode $<

proposal-with-cover.pdf: resource/proposal-cover.pdf proposal.pdf
	pdfunite resource/proposal-cover.pdf proposal.pdf proposal-with-cover.pdf

clean:
	latexmk -CA
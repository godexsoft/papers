BUILDDIR      = build

.PHONY: html clean linkcheck
default: html

clean:
	rm -rf $(BUILDDIR)/*

html: clean
	bikeshed update
	find ./source/ -name "*.bs" -type f | xargs -I{} -t -n1 bikeshed spec {}
	mkdir -p $(BUILDDIR)/html
	mv ./source/*.html $(BUILDDIR)/html/
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."

linkcheck:
	find $(BUILDDIR)/html -name '*.html' | xargs linkchecker

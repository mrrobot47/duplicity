help:
	@echo	"MAKE TARGETS"
	@echo 	"help         -- this text"
	@echo	"clean        -- remove generated files"
	@echo 	"docs         -- build Sphinx docs"
	@echo	"ext          -- build C extensions"
	@echo   "xlate-export -- update pot and make tar to export to LP translators"
	@echo   "xlate-import -- process LP tranlator's export file into duplicity"

clean:
	for i in '.tox' '_build' 'build' 'apsw' 'work' 'megatestresults' '.eggs' '*.egg-info' \
		'__pycache__' '*.pyc' '*.pyo' '*~' '*.o' '*.so' '*.pyd' '*.gcov' '*.gcda' \
		'*.gcno' '*.orig' '*.tmp' 'testdb*' 'testextension.sqlext' \
		'duplicity*.rst' 'testing*.rst'; do \
		find . -name "$$i" | xargs -t -r rm -rf ; \
	done

docs:
	sphinx-apidoc -o docs/ --separate --private . \
		apsw duplicity/backends/pyrax_identity/* setup.* testing/overrides testing/manual
	$(MAKE) -C docs html

ext:
	./setup.py build_ext
	
xlate-export:
	(cd po ; ./update-pot ; cd -)
	rm -rf /tmp/duplicity /tmp/duplicity.tgz
	mkdir -p /tmp/duplicity/
	cp -rp po /tmp/duplicity/
	(cd /tmp ; tar czf duplicity.tgz duplicity/po/duplicity.pot duplicity/po/*.po ; cd -)

xlate-import:
	rm -rf /tmp/duplicity /tmp/po
	mkdir -p /tmp/duplicity/
	(cd /tmp/duplicity ; tar xzf ~/Downloads/launchpad-export.tar.gz ; cd -)
	(cd /tmp/duplicity/po ; rename s/duplicity-//g *.po ; cd -)
	cp /tmp/duplicity/po/* po

.PHONY: clean docs ext help

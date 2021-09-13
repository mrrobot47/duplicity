clean:
	for i in '.tox' 'build' 'apsw' 'work' 'megatestresults' '.eggs' '*.egg-info' '__pycache__'; do \
		find . -type d -name "$$i" | xargs -t -r rm -rf ; \
	done

	for i in '*.pyc' '*.pyo' '*~' '*.o' '*.so' '*.pyd' '*.gcov' '*.gcda' \
		'*.gcno' '*.orig' '*.tmp' 'testdb*' 'testextension.sqlext' ; do \
		find . -type f -name "$$i" | xargs -t -r rm -f ; \
	done

docs:
	sphinx-apidoc -o docs/ --separate . apsw duplicity/backends/pyrax_identity/* setup.* testing/overrides testing/manual
	( cd docs ; make html )

ext:
	./setup.py build_ext

.PHONY: clean docs ext

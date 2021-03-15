.PHONY: clean docs

clean:
	for i in '.tox' 'build' 'work' 'megatestresults' '.eggs' '*.egg-info' '__pycache__'; do \
		find . -type d -name "$$i" | xargs -t -r rm -rf ; \
	done

	for i in '*.pyc' '*.pyo' '*~' '*.o' '*.so' '*.dll' '*.pyd' '*.gcov' '*.gcda' '*.gcno' '*.orig' '*.tmp' 'testdb*' 'testextension.sqlext' ; do \
		find . -type f -name "$$i" | xargs -t -r rm -f ; \
	done

docs:
	sphinx-apidoc -o docs/ -e -f .

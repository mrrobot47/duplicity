.PHONY: clean docs

clean:
	for i in '*.pyc' '*.pyo' '*~' '*.o' '*.so' '*.dll' '*.pyd' '*.gcov' '*.gcda' '*.gcno' '*.orig' '*.tmp' 'testdb*' 'testextension.sqlext' ; do \
		find . -type f -name "$$i" -print0 | xargs -0t -r rm -f ; done

	for i in 'build' 'work/*' 'megatestresults' '*.egg-info' '__pycache__' '.tox'; do \
		find . -type d -name "$$i" -print0 | xargs -0t -r rm -rf ; done

docs:
	sphinx-apidoc -o docs/ -e -f .

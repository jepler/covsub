.PHONY: all test%
coverage: test1 test2 test3 test4 test5 test6 test7 test8 test9 test0
	python -mcoverage combine
	python -mcoverage report --fail-under=100

test%:
	python -mcoverage run -m randsleep
	python -mcoverage run -m subfunctions --start=$$(($* * 10)) --stop=$$(($* * 10 + 10))

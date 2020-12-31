all: run

geckodriver:
	wget https://github.com/mozilla/geckodriver/releases/download/v0.28.0/geckodriver-v0.28.0-linux32.tar.gz
	tar xzvf geckodriver-v0.28.0-linux32.tar.gz

run: geckodriver
	bash run.sh

clean:
	rm -rf geckodriver*

.PHONY: run clean

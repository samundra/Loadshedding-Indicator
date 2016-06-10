SOURCES = main.py
SUPPORT = README.md .version
PKG_NAME = loadshedding
FILE_CONFIG="${HOME}/.cache/routine.xml"

default:
	./main.py

all:
	@echo "# Not implemented"
	@echo "build programs lib, doc."

unlink:
	rm -f /usr/local/bin/${PKG_NAME}

uninstall: unlink
	rm -rf /opt/${PKG_NAME}

link: unlink
	ln -s "$(PWD)/main.sh" /usr/local/bin/${PKG_NAME}

alias:
	@echo "add alias in to '.bashrc'"
	@echo "alias ${PKG_NAME}='$PWD/main.sh'"

install: unlink uninstall
	mkdir -p /opt/${PKG_NAME}
	install -m 755 ${SOURCES} -t /opt/${PKG_NAME}/
	cp ${SUPPORT} /opt/${PKG_NAME}/
	ln -s /opt/${PKG_NAME}/main.py /usr/local/bin/${PKG_NAME}

installcheck:
	@echo "# Not implemented"
	@echo ${SOURCES}

clean: deb-clean
	@echo "erase what has been buit (opposite of make all)"

dist:
	@echo "# Not implemented"
	@echo "create PACKAGE-VERSION.tar.gz"

distclean: clean
	@echo "# Not implemented"
	@echo "erase what ever done by make all, then clean what ever done by ./configure"

distcheck:
	@echo "# Not implemented"
	@echo "do sanity check"

check:
	@echo "# Not implemented"
	@echo "run the test suite if any"

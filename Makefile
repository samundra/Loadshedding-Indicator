SOURCES     = converter.py main.py nepali_calendar.py preference.py
SUPPORT     = README.md .version config.txt icon.png loadshedding.desktop
PKG_NAME    = loadshedding
FILE_CONFIG = ${HOME}/.cache/config.txt
APP_INSTALL_DIR = /opt/${PKG_NAME}
APP_BIN_PATH = /usr/local/bin/${PKG_NAME}
APP_ICON = /usr/share/applications/loadshedding.desktop

default:
	./update.sh
	./main.py

all:
	@echo "# Not implemented"
	@echo "build programs lib, doc."

delete_config_file: SHELL:=/bin/sh
delete_config_file: 
	@echo "Check config file:" ${FILE_CONFIG};
	if [ -e "${FILE_CONFIG}" ] ; then \
		echo "Remove" ${FILE_CONFIG}; \
		rm ${FILE_CONFIG}; \
	fi

delete_app_icon: SHELL:=/bin/sh
delete_app_icon:
	echo "Check application icon file:" ${APP_ICON};
	@if [ -e "${APP_ICON}" ]; then \
		@echo "Remove" ${APP_ICON}; \
		rm ${APP_ICON} ; \
	fi

delete_application_executable:
	rm -f "${APP_BIN_PATH}"

unlink: delete_config_file	delete_app_icon	delete_application_executable

uninstall: unlink
	rm -rf ${APP_INSTALL_DIR}

link: unlink
	ln -s "$(PWD)/main.sh" "${APP_BIN_PATH}"

alias:
	@echo "add alias in to '.bashrc'"
	@echo "alias ${PKG_NAME}='$PWD/main.sh'"

install: uninstall
	mkdir -p ${APP_INSTALL_DIR}
	install -m 0755 ${SOURCES} -t ${APP_INSTALL_DIR}
	@echo "Copy python source files"
	install -m 0755 ${SUPPORT} -t ${APP_INSTALL_DIR}
	install -m 0755 "${APP_INSTALL_DIR}/config.txt" -T "${FILE_CONFIG}"
	install -m 0755 "${APP_INSTALL_DIR}/loadshedding.desktop" -T "${APP_ICON}"
	ln -s "${APP_INSTALL_DIR}/main.py" "${APP_BIN_PATH}"

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

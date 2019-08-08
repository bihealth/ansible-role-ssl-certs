.PHONY: lint ansible-lint yamllint molecule

lint: ansible-lint yamllint

ansible-lint:
	ansible-lint .

yamllint:
	yamllint -s .

molecule:
	molecule test

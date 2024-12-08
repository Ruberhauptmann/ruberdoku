SHELL:=/bin/bash

# Variables to test the conda environment
ifeq (,$(shell which uv))
	HAS_UV=False
else
	HAS_UV=True
endif

build:
	uv build

.PHONY: help
help: # Show help for each of the Makefile recipes.
	@grep -E '^[a-zA-Z0-9 -]+:.*#'  Makefile | sort | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done


.PHONY: clean
clean: # Clean up build files.
	@rm -r dist/

environment: # Install the development environment.
ifeq (True,$(HAS_UV))
	@echo ">>> Installing "
	uv sync
	uv tool install tox --with tox-uv
	uv run pre-commit install
	@echo ">>> Everything installed."
else
	@echo ">>> Install uv first."
	exit
endif

#!/usr/bin/env bash

# specifies a set of variables to declare files to be used for code assessment
PACKAGE="pypi_org"

# specifies a set of variables to declare CLI output color
FAILED_OUT="\033[0;31m"
PASSED_OUT="\033[0;32m"
NONE_OUT="\033[0m"


pretty-printer-box() {
:<<DOC
    Provides pretty-printer check box
DOC
    echo "Start ${1} analysis ..."
}


remove-pycache() {
:<<DOC
    Removes python cache directories
DOC
    ( find . -depth -name __pycache__ | xargs rm -r )
}


check-black() {
:<<DOC
    Runs "black" code analyser
DOC
    pretty-printer-box "black" && ( black --check ${PACKAGE} )
}


check-flake() {
:<<DOC
    Runs "flake8" code analysers
DOC
    pretty-printer-box "flake" && ( flake8 ./ )
}


check-tests() {
:<<DOC
    Runs web app tests
DOC
    pretty-printer-box "web tests" && pytest
}



main() {
:<<DOC
    Runs "main" code analyser
DOC
    remove-pycache
    check-black && \
    check-flake && \
    check-tests
}

main
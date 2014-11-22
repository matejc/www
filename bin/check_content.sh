#!/bin/bash

BASEDIR="$(dirname $(dirname $(readlink -f $0)))"
CONTENT="$BASEDIR/content"

run_tests()
{
    {
        test_md_line_length &&
        test_no_spaces_in_filenames &&
        test_tags_are_valid &&
        test_categories_are_valid &&
        test_no_rst_files &&
        test_all_required_headers_present &&
        true
    } || {
        error "Some tests have failed. $CONTENT is not well-behaved."
        false
    }
}

error()  { echo "Error: $@" >&2; }
warning()  { echo "Warning: $@" >&2; }
warning_tbd()  { warning "$@ unimplemented"; }
indent() { sed 's/^/    /' >&2; }

test_md_line_length()
{
    MAX_LINE_LENGTH=120
    max_md_line_length=$(wc --max-line-length $(find $CONTENT -name "*.md") |
                         sort --reverse --numeric-sort |
                         awk '{print $1; exit}')
    [ $max_md_line_length -lt $MAX_LINE_LENGTH ] || {
        error "Max line length in *.md files is $MAX_LINE_LENGTH characters"
        false
    }
}

test_no_spaces_in_filenames()
{
    space_filenames="$(find -name "* *")"
    [ ! "$space_filenames" ] || {
        error "Some file names contain whitespace:"
        echo "$space_filenames" | indent
        false
    }
}

test_no_rst_files()
{
    warning_tbd "$FUNCNAME()"
}



run_tests

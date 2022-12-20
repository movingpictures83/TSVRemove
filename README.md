# TSVRemove
# Language: Python
# Input: TXT (keyword-value pairs)
# Output: TSV (indexed)
# Tested with: PluMA 1.0, Python 3.6

A PluMA plugin that takes a TSV file and removes a set of user-specified
rows and columns..

The plugin takes as input a tab-separated file of two keyword value
pairs: csvfile (name of the input TSV file) and index file, a file containing
the row and column indices to remove, tab-delimited, in the format:

row X
column Y
column Z
...

The output TSV file will be the same as the input TSV, but with the appropriate rows (i.e. X) and columns (i.e. Y, Z) removed


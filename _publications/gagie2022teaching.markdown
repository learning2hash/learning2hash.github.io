---
layout: publication
title: Teaching The Burrows-wheeler Transform Via The Positional Burrows-wheeler Transform
authors: Travis Gagie, Giovanni Manzini, Marinella Sciortino
conference: Arxiv
year: 2022
bibkey: gagie2022teaching
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2208.09840'}]
tags: []
short_authors: Travis Gagie, Giovanni Manzini, Marinella Sciortino
---
The Burrows-Wheeler Transform (BWT) is often taught in undergraduate courses
on algorithmic bioinformatics, because it underlies the FM-index and thus
important tools such as Bowtie and BWA. Its admirers consider the BWT a thing
of beauty but, despite thousands of pages being written about it over nearly
thirty years, to undergraduates seeing it for the first time it still often
seems like magic. Some who persevere are later shown the Positional BWT (PBWT),
which was published twenty years after the BWT. In this paper we argue that the
PBWT should be taught \{\em before\} the BWT.
  We first use the PBWT's close relation to a right-to-left radix sort to
explain how to use it as a fast and space-efficient index for \{\em positional
search\} on a set of strings (that is, given a pattern and a position, quickly
list the strings containing that pattern starting in that position). We then
observe that \{\em prefix search\} (listing all the strings that start with the
pattern) is an easy special case of positional search, and that prefix search
on the suffixes of a single string is equivalent to \{\em substring search\} in
that string (listing all the starting positions of occurrences of the pattern
in the string).
  Storing na\"ively a PBWT of the suffixes of a string is space-\{\em
inefficient\} but, in even reasonably small examples, most of its columns are
nearly the same. It is not difficult to show that if we store a PBWT of the
cyclic shifts of the string, instead of its suffixes, then all the columns are
exactly the same -- and equal to the BWT of the string. Thus we can teach the
BWT and the FM-index via the PBWT.
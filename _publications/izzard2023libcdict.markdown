---
layout: publication
title: 'Libcdict: Fast Dictionaries In C'
authors: Robert G. Izzard, David D. Hendriks, Daniel P. Nemergut
conference: Journal of Open Source Software
year: 2023
bibkey: izzard2023libcdict
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2401.14272'}]
tags: ["Tools & Libraries"]
short_authors: Robert G. Izzard, David D. Hendriks, Daniel P. Nemergut
---
A common requirement in science is to store and share large sets of
simulation data in an efficient, nested, flexible and human-readable way. Such
datasets contain number counts and distributions, i.e. histograms and maps, of
arbitrary dimension and variable type, e.g. floating-point number, integer or
character string. Modern high-level programming languages like Perl and Python
have associated arrays, knowns as dictionaries or hashes, respectively, to
fulfil this storage need. Low-level languages used more commonly for fast
computational simulations, such as C and Fortran, lack this functionality. We
present libcdict, a C dictionary library, to solve this problem. Libcdict
provides C and Fortran application programming interfaces (APIs) to native
dictionaries, called cdicts, and functions for cdicts to load and save these as
JSON and hence for easy interpretation in other software and languages like
Perl, Python and R.
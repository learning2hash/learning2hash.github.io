---
layout: publication
title: Breaking Imphash
authors: Chris Balles, Ateeq Sharfuddin
conference: Arxiv
year: 2019
bibkey: balles2019breaking
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1909.07630'}]
tags: ["Hashing Methods", "Locality Sensitive Hashing", "Neural Hashing", "Similarity Search"]
short_authors: Chris Balles, Ateeq Sharfuddin
---
There are numerous schemes to generically signature artifacts. We
specifically consider how to circumvent signatures based on imphash. Imphash is
used to signature Portable Executable (PE) files and an imphash of a PE file is
an MD5 digest over all the symbols that PE file imports. Imphash has been used
in numerous cases to accurately tie a PE file seen in one environment to PE
files in other environments, although each of these PE files' contents was
different. An argument made for imphash is that alteration of imphashes of
derived PE file artifacts is unlikely since it is an expensive process, such
that you will need to either modify the source code and recompile or relink in
a different order. Nevertheless, we present a novel algorithm that generates
derivative PE files such that its imphash is different from the original PE
file. This straightforward algorithm produces feasible solutions that defeat
approaches relying on the impash algorithm to signature PE files.
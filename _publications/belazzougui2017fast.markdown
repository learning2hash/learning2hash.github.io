---
layout: publication
title: Fast Label Extraction In The CDAWG
authors: Djamal Belazzougui, Fabio Cunial
conference: Lecture Notes in Computer Science
year: 2017
bibkey: belazzougui2017fast
citations: 24
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1707.08197'}]
tags: ["Datasets"]
short_authors: Djamal Belazzougui, Fabio Cunial
---
The compact directed acyclic word graph (CDAWG) of a string \(T\) of length \(n\)
takes space proportional just to the number \(e\) of right extensions of the
maximal repeats of \(T\), and it is thus an appealing index for highly repetitive
datasets, like collections of genomes from similar species, in which \(e\) grows
significantly more slowly than \(n\). We reduce from \(O(mlog\{log\{n\}\})\) to
\(O(m)\) the time needed to count the number of occurrences of a pattern of
length \(m\), using an existing data structure that takes an amount of space
proportional to the size of the CDAWG. This implies a reduction from
\(O(mlog\{log\{n\}\}+\mathtt\{occ\})\) to \(O(m+\mathtt\{occ\})\) in the time needed to
locate all the \(\mathtt\{occ\}\) occurrences of the pattern. We also reduce from
\(O(klog\{log\{n\}\})\) to \(O(k)\) the time needed to read the \(k\) characters of the
label of an edge of the suffix tree of \(T\), and we reduce from
\(O(mlog\{log\{n\}\})\) to \(O(m)\) the time needed to compute the matching
statistics between a query of length \(m\) and \(T\), using an existing
representation of the suffix tree based on the CDAWG. All such improvements
derive from extracting the label of a vertex or of an arc of the CDAWG using a
straight-line program induced by the reversed CDAWG.
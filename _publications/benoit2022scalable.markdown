---
layout: publication
title: Scalable Program Clone Search Through Spectral Analysis
authors: "Tristan Benoit, Jean-yves Marion, S\xE9bastien Bardin"
conference: Proceedings of the 31st ACM Joint European Software Engineering Conference
  and Symposium on the Foundations of Software Engineering
year: 2023
bibkey: benoit2022scalable
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2210.13063'}]
tags: []
short_authors: "Tristan Benoit, Jean-yves Marion, S\xE9bastien Bardin"
---
We consider the problem of program clone search, i.e. given a target program
and a repository of known programs (all in executable format), the goal is to
find the program in the repository most similar to the target program - with
potential applications in terms of reverse engineering, program clustering,
malware lineage and software theft detection. Recent years have witnessed a
blooming in code similarity techniques, yet most of them focus on
function-level similarity and function clone search, while we are interested in
program-level similarity and program clone search. Actually, our study shows
that prior similarity approaches are either too slow to handle large program
repositories, or not precise enough, or yet not robust against slight
variations introduced by compilers, source code versions or light obfuscations.
We propose a novel spectral analysis method for program-level similarity and
program clone search called Programs Spectral Similarity (PSS). In a nutshell,
PSS one-time spectral feature extraction is tailored for large repositories,
making it a perfect fit for program clone search. We have compared the
different approaches with extensive benchmarks, showing that PSS reaches a
sweet spot in terms of precision, speed and robustness.
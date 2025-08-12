---
layout: publication
title: Synthetic Datasets For Program Similarity Research
authors: Alexander Interrante-Grant, Michael Wang, Lisa Baer, Ryan Whelan, Tim Leek
conference: Arxiv
year: 2024
bibkey: interrantegrant2024synthetic
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2405.03478'}]
tags: ["Datasets"]
short_authors: Interrante-Grant et al.
---
Program similarity has become an increasingly popular area of research with
various security applications such as plagiarism detection, author
identification, and malware analysis. However, program similarity research
faces a few unique dataset quality problems in evaluating the effectiveness of
novel approaches. First, few high-quality datasets for binary program
similarity exist and are widely used in this domain. Second, there are
potentially many different, disparate definitions of what makes one program
similar to another and in many cases there is often a large semantic gap
between the labels provided by a dataset and any useful notion of behavioral or
semantic similarity. In this paper, we present HELIX - a framework for
generating large, synthetic program similarity datasets. We also introduce
Blind HELIX, a tool built on top of HELIX for extracting HELIX components from
library code automatically using program slicing. We evaluate HELIX and Blind
HELIX by comparing the performance of program similarity tools on a HELIX
dataset to a hand-crafted dataset built from multiple, disparate notions of
program similarity. Using Blind HELIX, we show that HELIX can generate
realistic and useful datasets of virtually infinite size for program similarity
research with ground truth labels that embody practical notions of program
similarity. Finally, we discuss the results and reason about relative tool
ranking.
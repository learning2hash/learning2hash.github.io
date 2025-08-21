---
layout: publication
title: Situating Sentence Embedders With Nearest Neighbor Overlap
authors: Lucy H. Lin, Noah A. Smith
conference: Arxiv
year: 2019
bibkey: lin2019situating
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1909.10724'}]
tags: ["Evaluation"]
short_authors: Lucy H. Lin, Noah A. Smith
---
As distributed approaches to natural language semantics have developed and
diversified, embedders for linguistic units larger than words have come to play
an increasingly important role. To date, such embedders have been evaluated
using benchmark tasks (e.g., GLUE) and linguistic probes. We propose a
comparative approach, nearest neighbor overlap (N2O), that quantifies
similarity between embedders in a task-agnostic manner. N2O requires only a
collection of examples and is simple to understand: two embedders are more
similar if, for the same set of inputs, there is greater overlap between the
inputs' nearest neighbors. Though applicable to embedders of texts of any size,
we focus on sentence embedders and use N2O to show the effects of different
design choices and architectures.
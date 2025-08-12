---
layout: publication
title: Bootstrapping Text Anonymization Models With Distant Supervision
authors: "Anthi Papadopoulou, Pierre Lison, Lilja \xD8vrelid, Ildik\xF3 Pil\xE1n"
conference: Arxiv
year: 2022
bibkey: papadopoulou2022bootstrapping
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2205.06895'}]
tags: []
short_authors: Papadopoulou et al.
---
We propose a novel method to bootstrap text anonymization models based on
distant supervision. Instead of requiring manually labeled training data, the
approach relies on a knowledge graph expressing the background information
assumed to be publicly available about various individuals. This knowledge
graph is employed to automatically annotate text documents including personal
data about a subset of those individuals. More precisely, the method determines
which text spans ought to be masked in order to guarantee \(k\)-anonymity,
assuming an adversary with access to both the text documents and the background
information expressed in the knowledge graph. The resulting collection of
labeled documents is then used as training data to fine-tune a pre-trained
language model for text anonymization. We illustrate this approach using a
knowledge graph extracted from Wikidata and short biographical texts from
Wikipedia. Evaluation results with a RoBERTa-based model and a manually
annotated collection of 553 summaries showcase the potential of the approach,
but also unveil a number of issues that may arise if the knowledge graph is
noisy or incomplete. The results also illustrate that, contrary to most
sequence labeling problems, the text anonymization task may admit several
alternative solutions.
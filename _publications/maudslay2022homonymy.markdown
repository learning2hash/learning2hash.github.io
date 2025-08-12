---
layout: publication
title: Homonymy Information For English Wordnet
authors: Rowan Hall Maudslay, Simone Teufel
conference: Arxiv
year: 2022
bibkey: maudslay2022homonymy
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2212.08388'}]
tags: ["Evaluation"]
short_authors: Rowan Hall Maudslay, Simone Teufel
---
A widely acknowledged shortcoming of WordNet is that it lacks a distinction
between word meanings which are systematically related (polysemy), and those
which are coincidental (homonymy). Several previous works have attempted to
fill this gap, by inferring this information using computational methods. We
revisit this task, and exploit recent advances in language modelling to
synthesise homonymy annotation for Princeton WordNet. Previous approaches treat
the problem using clustering methods; by contrast, our method works by linking
WordNet to the Oxford English Dictionary, which contains the information we
need. To perform this alignment, we pair definitions based on their proximity
in an embedding space produced by a Transformer model. Despite the simplicity
of this approach, our best model attains an F1 of .97 on an evaluation set that
we annotate. The outcome of our work is a high-quality homonymy annotation
layer for Princeton WordNet, which we release.
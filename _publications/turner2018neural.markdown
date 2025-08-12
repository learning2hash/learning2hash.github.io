---
layout: publication
title: A Neural Network To Classify Metaphorical Violence On Cable News
authors: Matthew A. Turner
conference: Arxiv
year: 2018
bibkey: turner2018neural
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1810.08677'}]
tags: ["Evaluation", "Supervised"]
short_authors: Matthew A. Turner
---
I present here an experimental system for identifying and annotating metaphor
in corpora. It is designed to plug in to Metacorps, an experimental web app for
annotating metaphor. As Metacorps users annotate metaphors, the system will use
user annotations as training data. When the system is confident, it will
suggest an identification and an annotation. Once approved by the user, this
becomes more training data. This naturally allows for transfer learning, where
the system can, with some known degree of reliability, classify one class of
metaphor after only being trained on another class of metaphor. For example, in
our metaphorical violence project, metaphors may be classified by the network
they were observed on, the grammatical subject or object of the violence
metaphor, or the violent word used (hit, attack, beat, etc.).
---
layout: publication
title: Recent Advances In The Self-referencing Embedding Strings (SELFIES) Library
authors: "Alston Lo, Robert Pollice, Akshatkumar Nigam, Andrew D. White, Mario Krenn,\
  \ Al\xE1n Aspuru-Guzik"
conference: Digital Discovery
year: 2023
bibkey: lo2023recent
citations: 13
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2302.03620'}]
tags: ["Tools & Libraries"]
short_authors: Lo et al.
---
String-based molecular representations play a crucial role in cheminformatics
applications, and with the growing success of deep learning in chemistry, have
been readily adopted into machine learning pipelines. However, traditional
string-based representations such as SMILES are often prone to syntactic and
semantic errors when produced by generative models. To address these problems,
a novel representation, SELF-referencIng Embedded Strings (SELFIES), was
proposed that is inherently 100% robust, alongside an accompanying open-source
implementation. Since then, we have generalized SELFIES to support a wider
range of molecules and semantic constraints and streamlined its underlying
grammar. We have implemented this updated representation in subsequent versions
of \selfieslib, where we have also made major advances with respect to design,
efficiency, and supported features. Hence, we present the current status of
\selfieslib (version 2.1.1) in this manuscript.
---
layout: publication
title: 'The Text Anonymization Benchmark (TAB): A Dedicated Corpus And Evaluation
  Framework For Text Anonymization'
authors: "Ildik\xF3 Pil\xE1n, Pierre Lison, Lilja \xD8vrelid, Anthi Papadopoulou,\
  \ David S\xE1nchez, Montserrat Batet"
conference: Computational Linguistics
year: 2022
bibkey: "pil\xE1n2022text"
citations: 37
additional_links: [{name: Code, url: 'https://github.com/NorskRegnesentral/text-anonymisation-benchmark'},
  {name: Paper, url: 'https://arxiv.org/abs/2202.00443'}]
tags: ["Evaluation", "Tools & Libraries"]
short_authors: "Pil\xE1n et al."
---
We present a novel benchmark and associated evaluation metrics for assessing
the performance of text anonymization methods. Text anonymization, defined as
the task of editing a text document to prevent the disclosure of personal
information, currently suffers from a shortage of privacy-oriented annotated
text resources, making it difficult to properly evaluate the level of privacy
protection offered by various anonymization methods. This paper presents TAB
(Text Anonymization Benchmark), a new, open-source annotated corpus developed
to address this shortage. The corpus comprises 1,268 English-language court
cases from the European Court of Human Rights (ECHR) enriched with
comprehensive annotations about the personal information appearing in each
document, including their semantic category, identifier type, confidential
attributes, and co-reference relations. Compared to previous work, the TAB
corpus is designed to go beyond traditional de-identification (which is limited
to the detection of predefined semantic categories), and explicitly marks which
text spans ought to be masked in order to conceal the identity of the person to
be protected. Along with presenting the corpus and its annotation layers, we
also propose a set of evaluation metrics that are specifically tailored towards
measuring the performance of text anonymization, both in terms of privacy
protection and utility preservation. We illustrate the use of the benchmark and
the proposed metrics by assessing the empirical performance of several baseline
text anonymization models. The full corpus along with its privacy-oriented
annotation guidelines, evaluation scripts and baseline models are available on:
https://github.com/NorskRegnesentral/text-anonymisation-benchmark
---
layout: publication
title: A Benchmark Of Nested Named Entity Recognition Approaches In Historical Structured
  Documents
authors: "Solenn Tual, Nathalie Abadie, J Chazalon, Bertrand Dum\xE9nieu, Edwin Carlinet"
conference: Lecture Notes in Computer Science
year: 2023
bibkey: tual2023benchmark
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2302.10204'}]
tags: ["Evaluation"]
short_authors: Tual et al.
---
Named Entity Recognition (NER) is a key step in the creation of structured
data from digitised historical documents. Traditional NER approaches deal with
flat named entities, whereas entities often are nested. For example, a postal
address might contain a street name and a number. This work compares three
nested NER approaches, including two state-of-the-art approaches using
Transformer-based architectures. We introduce a new Transformer-based approach
based on joint labelling and semantic weighting of errors, evaluated on a
collection of 19 th-century Paris trade directories. We evaluate approaches
regarding the impact of supervised fine-tuning, unsupervised pre-training with
noisy texts, and variation of IOB tagging formats. Our results show that while
nested NER approaches enable extracting structured data directly, they do not
benefit from the extra knowledge provided during training and reach a
performance similar to the base approach on flat entities. Even though all 3
approaches perform well in terms of F1 scores, joint labelling is most suitable
for hierarchically structured data. Finally, our experiments reveal the
superiority of the IO tagging format on such data.
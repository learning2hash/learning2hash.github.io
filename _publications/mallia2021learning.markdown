---
layout: publication
title: Learning Passage Impacts For Inverted Indexes
authors: Antonio Mallia, Omar Khattab, Nicola Tonellotto, Torsten Suel
conference: Proceedings of the 44th International ACM SIGIR Conference on Research
  and Development in Information Retrieval
year: 2021
bibkey: mallia2021learning
citations: 140
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.12016'}]
tags: ["Efficiency", "Hybrid ANN Methods", "Re-Ranking", "SIGIR", "Similarity Search"]
short_authors: Mallia et al.
---
Neural information retrieval systems typically use a cascading pipeline, in
which a first-stage model retrieves a candidate set of documents and one or
more subsequent stages re-rank this set using contextualized language models
such as BERT. In this paper, we propose DeepImpact, a new document
term-weighting scheme suitable for efficient retrieval using a standard
inverted index. Compared to existing methods, DeepImpact improves impact-score
modeling and tackles the vocabulary-mismatch problem. In particular, DeepImpact
leverages DocT5Query to enrich the document collection and, using a
contextualized language model, directly estimates the semantic importance of
tokens in a document, producing a single-value representation for each token in
each document. Our experiments show that DeepImpact significantly outperforms
prior first-stage retrieval approaches by up to 17% on effectiveness metrics
w.r.t. DocT5Query, and, when deployed in a re-ranking scenario, can reach the
same effectiveness of state-of-the-art approaches with up to 5.1x speedup in
efficiency.
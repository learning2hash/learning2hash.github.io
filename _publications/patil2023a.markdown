---
layout: publication
title: A Comparative Study Of Text Embedding Models For Semantic Text Similarity In
  Bug Reports
authors: Avinash Patil, Kihwan Han, Aryan Jadon
conference: Arxiv
year: 2023
bibkey: patil2023a
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2308.09193'}]
tags: ["Evaluation", "Survey Paper"]
short_authors: Avinash Patil, Kihwan Han, Aryan Jadon
---
Bug reports are an essential aspect of software development, and it is
crucial to identify and resolve them quickly to ensure the consistent
functioning of software systems. Retrieving similar bug reports from an
existing database can help reduce the time and effort required to resolve bugs.
In this paper, we compared the effectiveness of semantic textual similarity
methods for retrieving similar bug reports based on a similarity score. We
explored several embedding models such as TF-IDF (Baseline), FastText, Gensim,
BERT, and ADA. We used the Software Defects Data containing bug reports for
various software projects to evaluate the performance of these models. Our
experimental results showed that BERT generally outperformed the rest of the
models regarding recall, followed by ADA, Gensim, FastText, and TFIDF. Our
study provides insights into the effectiveness of different embedding methods
for retrieving similar bug reports and highlights the impact of selecting the
appropriate one for this task. Our code is available on GitHub.
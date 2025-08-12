---
layout: publication
title: Flexible Operator Embeddings Via Deep Learning
authors: Ryan Marcus, Olga Papaemmanouil
conference: Arxiv
year: 2019
bibkey: marcus2019flexible
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1901.09090'}]
tags: ["Neural Hashing"]
short_authors: Ryan Marcus, Olga Papaemmanouil
---
Integrating machine learning into the internals of database management
systems requires significant feature engineering, a human effort-intensive
process to determine the best way to represent the pieces of information that
are relevant to a task. In addition to being labor intensive, the process of
hand-engineering features must generally be repeated for each data management
task, and may make assumptions about the underlying database that are not
universally true. We introduce flexible operator embeddings, a deep learning
technique for automatically transforming query operators into feature vectors
that are useful for a multiple data management tasks and is custom-tailored to
the underlying database. Our approach works by taking advantage of an
operator's context, resulting in a neural network that quickly transforms
sparse representations of query operators into dense, information-rich feature
vectors. Experimentally, we show that our flexible operator embeddings perform
well across a number of data management tasks, using both synthetic and
real-world datasets.
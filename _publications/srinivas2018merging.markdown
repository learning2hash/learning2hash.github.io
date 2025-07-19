---
layout: publication
title: Merging datasets through deep learning
authors: Srinivas Kavitha, Gale Abraham, Dolby Julian
conference: Arxiv
year: 2018
bibkey: srinivas2018merging
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1809.01604'}]
tags: [Datasets]
---
Merging datasets is a key operation for data analytics. A frequent
requirement for merging is joining across columns that have different surface
forms for the same entity (e.g., the name of a person might be represented as
"Douglas Adams" or "Adams, Douglas"). Similarly, ontology alignment can require
recognizing distinct surface forms of the same entity, especially when
ontologies are independently developed. However, data management systems are
currently limited to performing merges based on string equality, or at best
using string similarity. We propose an approach to performing merges based on
deep learning models. Our approach depends on (a) creating a deep learning
model that maps surface forms of an entity into a set of vectors such that
alternate forms for the same entity are closest in vector space, (b) indexing
these vectors using a nearest neighbors algorithm to find the forms that can be
potentially joined together. To build these models, we had to adapt techniques
from metric learning due to the characteristics of the data; specifically we
describe novel sample selection techniques and loss functions that work for
this problem. To evaluate our approach, we used Wikidata as ground truth and
built models from datasets with approximately 1.1M people's names (200K
identities) and 130K company names (70K identities). We developed models that
allow for joins with precision@1 of .75-.81 and recall of .74-.81. We make the
models available for aligning people or companies across multiple datasets.
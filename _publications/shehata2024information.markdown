---
layout: publication
title: Information Retrieval With Entity Linking
authors: Dahlia Shehata
conference: Arxiv
year: 2024
bibkey: shehata2024information
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2404.08678'}]
tags: ["Efficiency", "Evaluation", "Few Shot & Zero Shot"]
short_authors: Dahlia Shehata
---
Despite the advantages of their low-resource settings, traditional sparse
retrievers depend on exact matching approaches between high-dimensional
bag-of-words (BoW) representations of both the queries and the collection. As a
result, retrieval performance is restricted by semantic discrepancies and
vocabulary gaps. On the other hand, transformer-based dense retrievers
introduce significant improvements in information retrieval tasks by exploiting
low-dimensional contextualized representations of the corpus. While dense
retrievers are known for their relative effectiveness, they suffer from lower
efficiency and lack of generalization issues, when compared to sparse
retrievers. For a lightweight retrieval task, high computational resources and
time consumption are major barriers encouraging the renunciation of dense
models despite potential gains. In this work, I propose boosting the
performance of sparse retrievers by expanding both the queries and the
documents with linked entities in two formats for the entity names: 1) explicit
and 2) hashed. A zero-shot end-to-end dense entity linking system is employed
for entity recognition and disambiguation to augment the corpus. By leveraging
the advanced entity linking methods, I believe that the effectiveness gap
between sparse and dense retrievers can be narrowed. Experiments are conducted
on the MS MARCO passage dataset using the original qrel set, the re-ranked
qrels favoured by MonoT5 and the latter set further re-ranked by DuoT5. Since I
am concerned with the early stage retrieval in cascaded ranking architectures
of large information retrieval systems, the results are evaluated using
recall@1000. The suggested approach is also capable of retrieving documents for
query subsets judged to be particularly difficult in prior work.
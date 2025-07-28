---
layout: publication
title: Word Embeddings For Entity-annotated Texts
authors: Satya Almasian, Andreas Spitz, Michael Gertz
conference: Lecture Notes in Computer Science
year: 2019
bibkey: almasian2019word
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1902.02078'}]
tags: []
short_authors: Satya Almasian, Andreas Spitz, Michael Gertz
---
Learned vector representations of words are useful tools for many information
retrieval and natural language processing tasks due to their ability to capture
lexical semantics. However, while many such tasks involve or even rely on named
entities as central components, popular word embedding models have so far
failed to include entities as first-class citizens. While it seems intuitive
that annotating named entities in the training corpus should result in more
intelligent word features for downstream tasks, performance issues arise when
popular embedding approaches are naively applied to entity annotated corpora.
Not only are the resulting entity embeddings less useful than expected, but one
also finds that the performance of the non-entity word embeddings degrades in
comparison to those trained on the raw, unannotated corpus. In this paper, we
investigate approaches to jointly train word and entity embeddings on a large
corpus with automatically annotated and linked entities. We discuss two
distinct approaches to the generation of such embeddings, namely the training
of state-of-the-art embeddings on raw-text and annotated versions of the
corpus, as well as node embeddings of a co-occurrence graph representation of
the annotated corpus. We compare the performance of annotated embeddings and
classical word embeddings on a variety of word similarity, analogy, and
clustering evaluation tasks, and investigate their performance in
entity-specific tasks. Our findings show that it takes more than training
popular word embedding models on an annotated corpus to create entity
embeddings with acceptable performance on common test cases. Based on these
results, we discuss how and when node embeddings of the co-occurrence graph
representation of the text can restore the performance.
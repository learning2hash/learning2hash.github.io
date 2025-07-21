---
layout: publication
title: Span-Aggregatable, Contextualized Word Embeddings for Effective Phrase Mining
authors: Orbach et al.
conference: 'Proceedings of the 59th Annual Meeting of the Association for Computational
  Linguistics and the 11th International Joint Conference on Natural Language Processing
  (Volume 1: Long Papers)'
year: 2024
bibkey: orbach2024span
citations: 19
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2405.07263'}]
tags: []
---
Dense vector representations for sentences made significant progress in
recent years as can be seen on sentence similarity tasks. Real-world phrase
retrieval applications, on the other hand, still encounter challenges for
effective use of dense representations. We show that when target phrases reside
inside noisy context, representing the full sentence with a single dense
vector, is not sufficient for effective phrase retrieval. We therefore look
into the notion of representing multiple, sub-sentence, consecutive word spans,
each with its own dense vector. We show that this technique is much more
effective for phrase mining, yet requires considerable compute to obtain useful
span representations. Accordingly, we make an argument for contextualized
word/token embeddings that can be aggregated for arbitrary word spans while
maintaining the span's semantic meaning. We introduce a modification to the
common contrastive loss used for sentence embeddings that encourages word
embeddings to have this property. To demonstrate the effect of this method we
present a dataset based on the STS-B dataset with additional generated text,
that requires finding the best matching paraphrase residing in a larger context
and report the degree of similarity to the origin phrase. We demonstrate on
this dataset, how our proposed method can achieve better results without
significant increase to compute.
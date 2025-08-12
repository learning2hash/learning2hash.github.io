---
layout: publication
title: 'Better Than Whitespace: Information Retrieval For Languages Without Custom
  Tokenizers'
authors: Odunayo Ogundepo, Xinyu Zhang, Jimmy Lin
conference: Arxiv
year: 2022
bibkey: ogundepo2022better
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2210.05481'}]
tags: []
short_authors: Odunayo Ogundepo, Xinyu Zhang, Jimmy Lin
---
Tokenization is a crucial step in information retrieval, especially for
lexical matching algorithms, where the quality of indexable tokens directly
impacts the effectiveness of a retrieval system. Since different languages have
unique properties, the design of the tokenization algorithm is usually
language-specific and requires at least some lingustic knowledge. However, only
a handful of the 7000+ languages on the planet benefit from specialized,
custom-built tokenization algorithms, while the other languages are stuck with
a "default" whitespace tokenizer, which cannot capture the intricacies of
different languages. To address this challenge, we propose a different approach
to tokenization for lexical matching retrieval algorithms (e.g., BM25): using
the WordPiece tokenizer, which can be built automatically from unsupervised
data. We test the approach on 11 typologically diverse languages in the MrTyDi
collection: results show that the mBERT tokenizer provides strong relevance
signals for retrieval "out of the box", outperforming whitespace tokenization
on most languages. In many cases, our approach also improves retrieval
effectiveness when combined with existing custom-built tokenizers.
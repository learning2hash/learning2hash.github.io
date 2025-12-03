---
layout: publication
title: Dimension Projection Among Languages Based On Pseudo-relevant Documents For
  Query Translation
authors: Javid Dadashkarimi, Mahsa S. Shahshahani, Amirhossein Tebbifakhr, Heshaam
  Faili, Azadeh Shakery
conference: Arxiv
year: 2016
bibkey: dadashkarimi2016dimension
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1605.07844'}]
tags: ["Evaluation"]
short_authors: Dadashkarimi et al.
---
Using top-ranked documents in response to a query has been shown to be an
effective approach to improve the quality of query translation in
dictionary-based cross-language information retrieval. In this paper, we
propose a new method for dictionary-based query translation based on dimension
projection of embedded vectors from the pseudo-relevant documents in the source
language to their equivalents in the target language. To this end, first we
learn low-dimensional vectors of the words in the pseudo-relevant collections
separately and then aim to find a query-dependent transformation matrix between
the vectors of translation pairs appeared in the collections. At the next step,
representation of each query term is projected to the target language and then,
after using a softmax function, a query-dependent translation model is built.
Finally, the model is used for query translation. Our experiments on four CLEF
collections in French, Spanish, German, and Italian demonstrate that the
proposed method outperforms a word embedding baseline based on bilingual
shuffling and a further number of competitive baselines. The proposed method
reaches up to 87% performance of machine translation (MT) in short queries and
considerable improvements in verbose queries.
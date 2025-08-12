---
layout: publication
title: Unsupervised Discovery Of Morphologically Related Words Based On Orthographic
  And Semantic Similarity
authors: Marco Baroni, Johannes Matiasek, Harald Trost
conference: Proceedings of the ACL-02 workshop on Morphological and phonological learning  -
year: 2002
bibkey: baroni2002unsupervised
citations: 118
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/cs/0205006'}]
tags: ["Unsupervised"]
short_authors: Marco Baroni, Johannes Matiasek, Harald Trost
---
We present an algorithm that takes an unannotated corpus as its input, and
returns a ranked list of probable morphologically related pairs as its output.
The algorithm tries to discover morphologically related pairs by looking for
pairs that are both orthographically and semantically similar, where
orthographic similarity is measured in terms of minimum edit distance, and
semantic similarity is measured in terms of mutual information. The procedure
does not rely on a morpheme concatenation model, nor on distributional
properties of word substrings (such as affix frequency). Experiments with
German and English input give encouraging results, both in terms of precision
(proportion of good pairs found at various cutoff points of the ranked list),
and in terms of a qualitative analysis of the types of morphological patterns
discovered by the algorithm.
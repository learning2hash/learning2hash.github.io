---
layout: publication
title: Semantic Relatedness Based Re-ranker For Text Spotting
authors: "Ahmed Sabir, Francesc Moreno-Noguer, Llu\xEDs Padr\xF3"
conference: Proceedings of the 2019 Conference on Empirical Methods in Natural Language
  Processing and the 9th International Joint Conference on Natural Language Processing
  (EMNLP-IJCNLP)
year: 2019
bibkey: sabir2019semantic
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1909.07950'}]
tags: ["EMNLP"]
short_authors: "Ahmed Sabir, Francesc Moreno-Noguer, Llu\xEDs Padr\xF3"
---
Applications such as textual entailment, plagiarism detection or document
clustering rely on the notion of semantic similarity, and are usually
approached with dimension reduction techniques like LDA or with embedding-based
neural approaches. We present a scenario where semantic similarity is not
enough, and we devise a neural approach to learn semantic relatedness. The
scenario is text spotting in the wild, where a text in an image (e.g. street
sign, advertisement or bus destination) must be identified and recognized. Our
goal is to improve the performance of vision systems by leveraging semantic
information. Our rationale is that the text to be spotted is often related to
the image context in which it appears (word pairs such as Delta-airplane, or
quarters-parking are not similar, but are clearly related). We show how
learning a word-to-word or word-to-sentence relatedness score can improve the
performance of text spotting systems up to 2.9 points, outperforming other
measures in a benchmark dataset.
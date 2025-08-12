---
layout: publication
title: Combining A Context Aware Neural Network With A Denoising Autoencoder For Measuring
  String Similarities
authors: Mehdi Ben Lazreg, Morten Goodwin
conference: Computer Speech &amp; Language
year: 2019
bibkey: lazreg2018combining
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1807.06414'}]
tags: ["Evaluation"]
short_authors: Mehdi Ben Lazreg, Morten Goodwin
---
Measuring similarities between strings is central for many established and
fast growing research areas including information retrieval, biology, and
natural language processing. The traditional approach for string similarity
measurements is to define a metric over a word space that quantifies and sums
up the differences between characters in two strings. The state-of-the-art in
the area has, surprisingly, not evolved much during the last few decades. The
majority of the metrics are based on a simple comparison between character and
character distributions without consideration for the context of the words.
This paper proposes a string metric that encompasses similarities between
strings based on (1) the character similarities between the words including.
Non-Standard and standard spellings of the same words, and (2) the context of
the words. Our proposal is a neural network composed of a denoising autoencoder
and what we call a context encoder specifically designed to find similarities
between the words based on their context. The experimental results show that
the resulting metrics succeeds in 85.4% of the cases in finding the correct
version of a non-standard spelling among the closest words, compared to 63.2%
with the established Normalised-Levenshtein distance. Besides, we show that
words used in similar context are with our approach calculated to be similar
than words with different contexts, which is a desirable property missing in
established string metrics.
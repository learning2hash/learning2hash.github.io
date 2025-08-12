---
layout: publication
title: Domain-specific Lexical Grounding In Noisy Visual-textual Documents
authors: Gregory Yauney, Jack Hessel, David Mimno
conference: Published in EMNLP 2020
year: 2020
bibkey: yauney2020domain
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2010.16363'}]
tags: ["Datasets", "EMNLP"]
short_authors: Gregory Yauney, Jack Hessel, David Mimno
---
Images can give us insights into the contextual meanings of words, but
current image-text grounding approaches require detailed annotations. Such
granular annotation is rare, expensive, and unavailable in most domain-specific
contexts. In contrast, unlabeled multi-image, multi-sentence documents are
abundant. Can lexical grounding be learned from such documents, even though
they have significant lexical and visual overlap? Working with a case study
dataset of real estate listings, we demonstrate the challenge of distinguishing
highly correlated grounded terms, such as "kitchen" and "bedroom", and
introduce metrics to assess this document similarity. We present a simple
unsupervised clustering-based method that increases precision and recall beyond
object detection and image tagging baselines when evaluated on labeled subsets
of the dataset. The proposed method is particularly effective for local
contextual meanings of a word, for example associating "granite" with
countertops in the real estate dataset and with rocky landscapes in a Wikipedia
dataset.
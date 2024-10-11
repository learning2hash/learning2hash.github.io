---
layout: publication
title: Accurate And Efficient Suffix Tree Based Privacy-preserving String Matching
authors: Vaiwsri Sirintra, Ranbaduge Thilina, Christen Peter, Ng Kee Siong
conference: "Arxiv"
year: 2021
bibkey: vaiwsri2021accurate
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2104.03018"}
tags: ['ARXIV']
---
The task of calculating similarities between strings held by different organizations without revealing these strings is an increasingly important problem in areas such as health informatics, national censuses, genomics, and fraud detection. Most existing privacy-preserving string comparison functions are either based on comparing sets of encoded character q-grams, allow only exact matching of encrypted strings, or they are aimed at long genomic sequences that have a small alphabet. The set-based privacy-preserving similarity functions commonly used to compare name and address strings in the context of privacy-preserving record linkage do not take the positions of sub-strings into account. As a result, two very different strings can potentially be considered as an exact match leading to wrongly linked records. Existing set-based techniques also cannot identify the length of the longest common sub-string across two strings. In this paper we propose a novel approach for accurate and efficient privacy-preserving string matching based on suffix trees that are encoded using chained hashing. We incorporate a hashing based encoding technique upon the encoded suffixes to improve privacy against frequency attacks such as those exploiting Benford's law. Our approach allows various operations to be performed without the strings to be compared being revealed: the length of the longest common sub-string, do two strings have the same beginning, middle or end, and the longest common sub-string similarity between two strings. These functions allow a more accurate comparison of, for example, bank account, credit card, or telephone numbers, which cannot be compared appropriately with existing privacy-preserving string matching techniques. Our evaluation on several data sets with different types of strings validates the privacy and accuracy of our proposed approach.

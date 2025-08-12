---
layout: publication
title: 'Semstamp: A Semantic Watermark With Paraphrastic Robustness For Text Generation'
authors: Abe Bohan Hou, Jingyu Zhang, Tianxing He, Yichen Wang, Yung-sung Chuang,
  Hongwei Wang, Lingfeng Shen, Benjamin van Durme, Daniel Khashabi, Yulia Tsvetkov
conference: 'Proceedings of the 2024 Conference of the North American Chapter of the
  Association for Computational Linguistics: Human Language Technologies (Volume 1:
  Long Papers)'
year: 2024
bibkey: hou2023semstamp
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2310.03991'}]
tags: ["NAACL", "Robustness"]
short_authors: Hou et al.
---
Existing watermarking algorithms are vulnerable to paraphrase attacks because
of their token-level design. To address this issue, we propose SemStamp, a
robust sentence-level semantic watermarking algorithm based on
locality-sensitive hashing (LSH), which partitions the semantic space of
sentences. The algorithm encodes and LSH-hashes a candidate sentence generated
by an LLM, and conducts sentence-level rejection sampling until the sampled
sentence falls in watermarked partitions in the semantic embedding space. A
margin-based constraint is used to enhance its robustness. To show the
advantages of our algorithm, we propose a "bigram" paraphrase attack using the
paraphrase that has the fewest bigram overlaps with the original sentence. This
attack is shown to be effective against the existing token-level watermarking
method. Experimental results show that our novel semantic watermark algorithm
is not only more robust than the previous state-of-the-art method on both
common and bigram paraphrase attacks, but also is better at preserving the
quality of generation.
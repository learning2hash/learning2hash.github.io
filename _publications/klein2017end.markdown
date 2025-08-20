---
layout: publication
title: End-to-end Supervised Product Quantization For Image Search And Retrieval
authors: Benjamin Klein, Lior Wolf
conference: 2019 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2019
bibkey: klein2017end
citations: 59
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1711.08589'}]
tags: [Hashing Methods, Quantization, CVPR, Unsupervised, Image Retrieval, Supervised,
  Memory Efficiency, Neural Hashing]
short_authors: Benjamin Klein, Lior Wolf
---
Product Quantization, a dictionary based hashing method, is one of the
leading unsupervised hashing techniques. While it ignores the labels, it
harnesses the features to construct look up tables that can approximate the
feature space. In recent years, several works have achieved state of the art
results on hashing benchmarks by learning binary representations in a
supervised manner. This work presents Deep Product Quantization (DPQ), a
technique that leads to more accurate retrieval and classification than the
latest state of the art methods, while having similar computational complexity
and memory footprint as the Product Quantization method. To our knowledge, this
is the first work to introduce a dictionary-based representation that is
inspired by Product Quantization and which is learned end-to-end, and thus
benefits from the supervised signal. DPQ explicitly learns soft and hard
representations to enable an efficient and accurate asymmetric search, by using
a straight-through estimator. Our method obtains state of the art results on an
extensive array of retrieval and classification experiments.
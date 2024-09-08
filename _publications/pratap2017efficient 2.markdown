---
layout: publication
title: Efficient Compression Technique for Sparse Sets
authors: Pratap Rameshwar, Sohony Ishan, Kulkarni Raghav
conference: Arxiv
year: 2017
bibkey: pratap2017efficient
additional_links:
   - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/1708.04799"}
tags: ['Arxiv']
---
Recent technological advancements have led to the generation of huge amounts of data over the web, such as text, image, audio and video. Most of this data is high dimensional and sparse, for e.g., the bag-of-words representation used for representing text. Often, an efficient search for similar data points needs to be performed in many applications like clustering, nearest neighbour search, ranking and indexing. Even though there have been significant increases in computational power, a simple brute-force similarity-search on such datasets is inefficient and at times impossible. Thus, it is desirable to get a compressed representation which preserves the similarity between data points. In this work, we consider the data points as sets and use Jaccard similarity as the similarity measure. Compression techniques are generally evaluated on the following parameters --1) Randomness required for compression, 2) Time required for compression, 3) Dimension of the data after compression, and 4) Space required to store the compressed data. Ideally, the compressed representation of the data should be such, that the similarity between each pair of data points is preserved, while keeping the time and the randomness required for compression as low as possible. We show that the compression technique suggested by Pratap and Kulkarni also works well for Jaccard similarity. We present a theoretical proof of the same and complement it with rigorous experimentations on synthetic as well as real-world datasets. We also compare our results with the state-of-the-art "min-wise independent permutation", and show that our compression algorithm achieves almost equal accuracy while significantly reducing the compression time and the randomness.

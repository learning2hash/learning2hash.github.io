---
layout: publication
title: Constant Sequence Extension for Fast Search Using Weighted Hamming Distance
authors: Weng Zhenyu, Zhuang Huiping, Li Haizhou, Lin Zhiping
conference: "Arxiv"
year: 2023
bibkey: weng2023constant
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2306.03612"}
tags: ['ARXIV', 'General']
---
Representing visual data using compact binary codes is attracting increasing attention as binary codes are used as direct indices into hash table(s) for fast non-exhaustive search. Recent methods show that ranking binary codes using weighted Hamming distance (WHD) rather than Hamming distance (HD) by generating query-adaptive weights for each bit can better retrieve query-related items. However search using WHD is slower than that using HD. One main challenge is that the complexity of extending a monotone increasing sequence using WHD to probe buckets in hash table(s) for existing methods is at least proportional to the square of the sequence length while that using HD is proportional to the sequence length. To overcome this challenge we propose a novel fast non-exhaustive search method using WHD. The key idea is to design a constant sequence extension algorithm to perform each sequence extension in constant computational complexity and the total complexity is proportional to the sequence length which is justified by theoretical analysis. Experimental results show that our method is faster than other WHD-based search methods. Also compared with the HD-based non-exhaustive search method our method has comparable efficiency but retrieves more query-related items for the dataset of up to one billion items.

---
layout: publication
title: Lempel-Ziv Jaccard Distance an Effective Alternative to Ssdeep and Sdhash
authors: Raff Edward, Nicholas Charles K.
conference: "Arxiv"
year: 2017
bibkey: raff2017lempelziv
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1708.03346"}
tags: ['ARXIV']
---
Recent work has proposed the Lempel-Ziv Jaccard Distance (LZJD) as a method to measure the similarity between binary byte sequences for malware classification. We propose and test LZJDs effectiveness as a similarity digest hash for digital forensics. To do so we develop a high performance Java implementation with the same command-line arguments as sdhash making it easy to integrate into existing workflows. Our testing shows that LZJD is effective for this task and significantly outperforms sdhash and ssdeep in its ability to match related file fragments and files corrupted with random noise. In addition LZJD is up to 60x faster than sdhash at comparison time.

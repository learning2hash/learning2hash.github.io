---
layout: publication
title: 'Deepsketch: A New Machine Learning-based Reference Search Technique For Post-deduplication
  Delta Compression'
authors: Jisung Park, Jeoggyun Kim, Yeseong Kim, Sungjin Lee, Onur Mutlu
conference: Arxiv
year: 2022
bibkey: park2022deepsketch
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2202.10584'}]
tags: ["Efficiency", "Neural Hashing", "Similarity Search"]
short_authors: Park et al.
---
Data reduction in storage systems is becoming increasingly important as an
effective solution to minimize the management cost of a data center. To
maximize data-reduction efficiency, existing post-deduplication
delta-compression techniques perform delta compression along with traditional
data deduplication and lossless compression. Unfortunately, we observe that
existing techniques achieve significantly lower data-reduction ratios than the
optimal due to their limited accuracy in identifying similar data blocks.
  In this paper, we propose DeepSketch, a new reference search technique for
post-deduplication delta compression that leverages the learning-to-hash method
to achieve higher accuracy in reference search for delta compression, thereby
improving data-reduction efficiency. DeepSketch uses a deep neural network to
extract a data block's sketch, i.e., to create an approximate data signature of
the block that can preserve similarity with other blocks. Our evaluation using
eleven real-world workloads shows that DeepSketch improves the data-reduction
ratio by up to 33% (21% on average) over a state-of-the-art post-deduplication
delta-compression technique.
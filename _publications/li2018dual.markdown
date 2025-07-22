---
layout: publication
title: Dual Asymmetric Deep Hashing Learning
authors: Li Jinxing, Zhang Bob, Lu Guangming, Zhang David
conference: IEEE Access
year: 2019
bibkey: li2018dual
citations: 16
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1801.08360'}]
tags: ["Hashing-Methods", "Neural-Hashing", "Compact-Codes", "Datasets", "Supervised", "Evaluation"]
short_authors: Li et al.
---
Due to the impressive learning power, deep learning has achieved a remarkable
performance in supervised hash function learning. In this paper, we propose a
novel asymmetric supervised deep hashing method to preserve the semantic
structure among different categories and generate the binary codes
simultaneously. Specifically, two asymmetric deep networks are constructed to
reveal the similarity between each pair of images according to their semantic
labels. The deep hash functions are then learned through two networks by
minimizing the gap between the learned features and discrete codes.
Furthermore, since the binary codes in the Hamming space also should keep the
semantic affinity existing in the original space, another asymmetric pairwise
loss is introduced to capture the similarity between the binary codes and
real-value features. This asymmetric loss not only improves the retrieval
performance, but also contributes to a quick convergence at the training phase.
By taking advantage of the two-stream deep structures and two types of
asymmetric pairwise functions, an alternating algorithm is designed to optimize
the deep features and high-quality binary codes efficiently. Experimental
results on three real-world datasets substantiate the effectiveness and
superiority of our approach as compared with state-of-the-art.
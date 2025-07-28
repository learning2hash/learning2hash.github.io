---
layout: publication
title: Distribution-consistency-guided Multi-modal Hashing
authors: Jin-yu Liu, Xian-ling Mao, Tian-yi Che, Rong-cheng Tu
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2025
bibkey: liu2024distribution
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.11216'}]
tags: ["AAAI", "Hashing Methods"]
short_authors: Liu et al.
---
Multi-modal hashing methods have gained popularity due to their fast speed
and low storage requirements. Among them, the supervised methods demonstrate
better performance by utilizing labels as supervisory signals compared with
unsupervised methods. Currently, for almost all supervised multi-modal hashing
methods, there is a hidden assumption that training sets have no noisy labels.
However, labels are often annotated incorrectly due to manual labeling in
real-world scenarios, which will greatly harm the retrieval performance. To
address this issue, we first discover a significant distribution consistency
pattern through experiments, i.e., the 1-0 distribution of the presence or
absence of each category in the label is consistent with the high-low
distribution of similarity scores of the hash codes relative to category
centers. Then, inspired by this pattern, we propose a novel
Distribution-Consistency-Guided Multi-modal Hashing (DCGMH), which aims to
filter and reconstruct noisy labels to enhance retrieval performance.
Specifically, the proposed method first randomly initializes several category
centers, which are used to compute the high-low distribution of similarity
scores; Noisy and clean labels are then separately filtered out via the
discovered distribution consistency pattern to mitigate the impact of noisy
labels; Subsequently, a correction strategy, which is indirectly designed via
the distribution consistency pattern, is applied to the filtered noisy labels,
correcting high-confidence ones while treating low-confidence ones as unlabeled
for unsupervised learning, thereby further enhancing the model's performance.
Extensive experiments on three widely used datasets demonstrate the superiority
of the proposed method compared to state-of-the-art baselines in multi-modal
retrieval tasks. The code is available at
https://github.com/LiuJinyu1229/DCGMH.
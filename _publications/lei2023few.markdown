---
layout: publication
title: Few-shot Learning From Augmented Label-uncertain Queries In Bongard-hoi
authors: Qinqian Lei, Bo Wang, Robby T. Tan
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2024
bibkey: lei2023few
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2312.10586'}]
tags: ["AAAI"]
short_authors: Qinqian Lei, Bo Wang, Robby T. Tan
---
Detecting human-object interactions (HOI) in a few-shot setting remains a
challenge. Existing meta-learning methods struggle to extract representative
features for classification due to the limited data, while existing few-shot
HOI models rely on HOI text labels for classification. Moreover, some query
images may display visual similarity to those outside their class, such as
similar backgrounds between different HOI classes. This makes learning more
challenging, especially with limited samples. Bongard-HOI (Jiang et al. 2022)
epitomizes this HOI few-shot problem, making it the benchmark we focus on in
this paper. In our proposed method, we introduce novel label-uncertain query
augmentation techniques to enhance the diversity of the query inputs, aiming to
distinguish the positive HOI class from the negative ones. As these augmented
inputs may or may not have the same class label as the original inputs, their
class label is unknown. Those belonging to a different class become hard
samples due to their visual similarity to the original ones. Additionally, we
introduce a novel pseudo-label generation technique that enables a mean teacher
model to learn from the augmented label-uncertain inputs. We propose to augment
the negative support set for the student model to enrich the semantic
information, fostering diversity that challenges and enhances the student's
learning. Experimental results demonstrate that our method sets a new
state-of-the-art (SOTA) performance by achieving 68.74% accuracy on the
Bongard-HOI benchmark, a significant improvement over the existing SOTA of
66.59%. In our evaluation on HICO-FS, a more general few-shot recognition
dataset, our method achieves 73.27% accuracy, outperforming the previous SOTA
of 71.20% in the 5-way 5-shot task.
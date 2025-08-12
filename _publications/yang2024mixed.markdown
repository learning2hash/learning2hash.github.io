---
layout: publication
title: 'Mixed Blessing: Class-wise Embedding Guided Instance-dependent Partial Label
  Learning'
authors: Fuchao Yang, Jianhong Cheng, Hui Liu, Yongqiang Dong, Yuheng Jia, Junhui
  Hou
conference: Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and
  Data Mining V.1
year: 2025
bibkey: yang2024mixed
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.05029'}]
tags: ["KDD"]
short_authors: Yang et al.
---
In partial label learning (PLL), every sample is associated with a candidate
label set comprising the ground-truth label and several noisy labels. The
conventional PLL assumes the noisy labels are randomly generated
(instance-independent), while in practical scenarios, the noisy labels are
always instance-dependent and are highly related to the sample features,
leading to the instance-dependent partial label learning (IDPLL) problem.
Instance-dependent noisy label is a double-edged sword. On one side, it may
promote model training as the noisy labels can depict the sample to some
extent. On the other side, it brings high label ambiguity as the noisy labels
are quite undistinguishable from the ground-truth label. To leverage the
nuances of IDPLL effectively, for the first time we create class-wise
embeddings for each sample, which allow us to explore the relationship of
instance-dependent noisy labels, i.e., the class-wise embeddings in the
candidate label set should have high similarity, while the class-wise
embeddings between the candidate label set and the non-candidate label set
should have high dissimilarity. Moreover, to reduce the high label ambiguity,
we introduce the concept of class prototypes containing global feature
information to disambiguate the candidate label set. Extensive experimental
comparisons with twelve methods on six benchmark data sets, including four
fine-grained data sets, demonstrate the effectiveness of the proposed method.
The code implementation is publicly available at
https://github.com/Yangfc-ML/CEL.
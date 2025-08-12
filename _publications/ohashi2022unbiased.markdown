---
layout: publication
title: Unbiased Scene Graph Generation Using Predicate Similarities
authors: Misaki Ohashi, Yusuke Matsui
conference: IEEE Access
year: 2024
bibkey: ohashi2022unbiased
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2210.00920'}]
tags: ["Datasets", "Evaluation"]
short_authors: Misaki Ohashi, Yusuke Matsui
---
Scene Graphs are widely applied in computer vision as a graphical
representation of relationships between objects shown in images. However, these
applications have not yet reached a practical stage of development owing to
biased training caused by long-tailed predicate distributions. In recent years,
many studies have tackled this problem. In contrast, relatively few works have
considered predicate similarities as a unique dataset feature which also leads
to the biased prediction. Due to the feature, infrequent predicates (e.g.,
parked on, covered in) are easily misclassified as closely-related frequent
predicates (e.g., on, in). Utilizing predicate similarities, we propose a new
classification scheme that branches the process to several fine-grained
classifiers for similar predicate groups. The classifiers aim to capture the
differences among similar predicates in detail. We also introduce the idea of
transfer learning to enhance the features for the predicates which lack
sufficient training samples to learn the descriptive representations. The
results of extensive experiments on the Visual Genome dataset show that the
combination of our method and an existing debiasing approach greatly improves
performance on tail predicates in challenging SGCls/SGDet tasks. Nonetheless,
the overall performance of the proposed approach does not reach that of the
current state of the art, so further analysis remains necessary as future work.
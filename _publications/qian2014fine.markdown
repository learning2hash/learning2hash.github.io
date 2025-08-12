---
layout: publication
title: Fine-grained Visual Categorization Via Multi-stage Metric Learning
authors: Qi Qian, Rong Jin, Shenghuo Zhu, Yuanqing Lin
conference: 2015 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2015
bibkey: qian2014fine
citations: 155
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1402.0453'}]
tags: ["CVPR", "Distance Metric Learning"]
short_authors: Qian et al.
---
Fine-grained visual categorization (FGVC) is to categorize objects into
subordinate classes instead of basic classes. One major challenge in FGVC is
the co-occurrence of two issues: 1) many subordinate classes are highly
correlated and are difficult to distinguish, and 2) there exists the large
intra-class variation (e.g., due to object pose). This paper proposes to
explicitly address the above two issues via distance metric learning (DML). DML
addresses the first issue by learning an embedding so that data points from the
same class will be pulled together while those from different classes should be
pushed apart from each other; and it addresses the second issue by allowing the
flexibility that only a portion of the neighbors (not all data points) from the
same class need to be pulled together. However, feature representation of an
image is often high dimensional, and DML is known to have difficulty in dealing
with high dimensional feature vectors since it would require \\(\mathcal\{O\}(d^2)\\)
for storage and \\(\mathcal\{O\}(d^3)\\) for optimization. To this end, we proposed a
multi-stage metric learning framework that divides the large-scale high
dimensional learning problem to a series of simple subproblems, achieving
\\(\mathcal\{O\}(d)\\) computational complexity. The empirical study with FVGC
benchmark datasets verifies that our method is both effective and efficient
compared to the state-of-the-art FGVC approaches.
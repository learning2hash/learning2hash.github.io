---
layout: publication
title: 'PPR-FCN: Weakly Supervised Visual Relation Detection Via Parallel Pairwise
  R-FCN'
authors: Hanwang Zhang, Zawlin Kyaw, Jinyang Yu, Shih-Fu Chang
conference: 2017 IEEE International Conference on Computer Vision (ICCV)
year: 2017
bibkey: zhang2017ppr
citations: 142
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1708.01956'}]
tags: ["ICCV", "Supervised"]
short_authors: Zhang et al.
---
We aim to tackle a novel vision task called Weakly Supervised Visual Relation
Detection (WSVRD) to detect "subject-predicate-object" relations in an image
with object relation groundtruths available only at the image level. This is
motivated by the fact that it is extremely expensive to label the combinatorial
relations between objects at the instance level. Compared to the extensively
studied problem, Weakly Supervised Object Detection (WSOD), WSVRD is more
challenging as it needs to examine a large set of regions pairs, which is
computationally prohibitive and more likely stuck in a local optimal solution
such as those involving wrong spatial context. To this end, we present a
Parallel, Pairwise Region-based, Fully Convolutional Network (PPR-FCN) for
WSVRD. It uses a parallel FCN architecture that simultaneously performs pair
selection and classification of single regions and region pairs for object and
relation detection, while sharing almost all computation shared over the entire
image. In particular, we propose a novel position-role-sensitive score map with
pairwise RoI pooling to efficiently capture the crucial context associated with
a pair of objects. We demonstrate the superiority of PPR-FCN over all baselines
in solving the WSVRD challenge by using results of extensive experiments over
two visual relation benchmarks.
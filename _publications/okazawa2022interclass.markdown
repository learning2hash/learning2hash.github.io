---
layout: publication
title: Interclass Prototype Relation For Few-shot Segmentation
authors: Atsuro Okazawa
conference: Lecture Notes in Computer Science
year: 2022
bibkey: okazawa2022interclass
citations: 17
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2211.08681'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Atsuro Okazawa
---
Traditional semantic segmentation requires a large labeled image dataset and
can only be predicted within predefined classes. To solve this problem,
few-shot segmentation, which requires only a handful of annotations for the new
target class, is important. However, with few-shot segmentation, the target
class data distribution in the feature space is sparse and has low coverage
because of the slight variations in the sample data. Setting the classification
boundary that properly separates the target class from other classes is an
impossible task. In particular, it is difficult to classify classes that are
similar to the target class near the boundary. This study proposes the
Interclass Prototype Relation Network (IPRNet), which improves the separation
performance by reducing the similarity between other classes. We conducted
extensive experiments with Pascal-5i and COCO-20i and showed that IPRNet
provides the best segmentation performance compared with previous research.
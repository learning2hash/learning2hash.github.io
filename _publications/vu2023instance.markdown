---
layout: publication
title: Instance-level Few-shot Learning With Class Hierarchy Mining
authors: Anh-Khoa Nguyen Vu, Thanh-Toan Do, Nhat-Duy Nguyen, Vinh-Tiep Nguyen, Thanh
  Duc Ngo, Tam V. Nguyen
conference: IEEE Transactions on Image Processing
year: 2023
bibkey: vu2023instance
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2304.07459'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Vu et al.
---
Few-shot learning is proposed to tackle the problem of scarce training data
in novel classes. However, prior works in instance-level few-shot learning have
paid less attention to effectively utilizing the relationship between
categories. In this paper, we exploit the hierarchical information to leverage
discriminative and relevant features of base classes to effectively classify
novel objects. These features are extracted from abundant data of base classes,
which could be utilized to reasonably describe classes with scarce data.
Specifically, we propose a novel superclass approach that automatically creates
a hierarchy considering base and novel classes as fine-grained classes for
few-shot instance segmentation (FSIS). Based on the hierarchical information,
we design a novel framework called Soft Multiple Superclass (SMS) to extract
relevant features or characteristics of classes in the same superclass. A new
class assigned to the superclass is easier to classify by leveraging these
relevant features. Besides, in order to effectively train the
hierarchy-based-detector in FSIS, we apply the label refinement to further
describe the associations between fine-grained classes. The extensive
experiments demonstrate the effectiveness of our method on FSIS benchmarks.
Code is available online.
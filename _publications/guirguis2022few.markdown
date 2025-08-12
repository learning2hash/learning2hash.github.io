---
layout: publication
title: Few-shot Object Detection In Unseen Domains
authors: Karim Guirguis, George Eskandar, Matthias Kayser, Bin Yang, Juergen Beyerer
conference: 2022 16th International Conference on Signal-Image Technology &amp; Internet-Based
  Systems (SITIS)
year: 2022
bibkey: guirguis2022few
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2204.05072'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Guirguis et al.
---
Few-shot object detection (FSOD) has thrived in recent years to learn novel
object classes with limited data by transferring knowledge gained on abundant
base classes. FSOD approaches commonly assume that both the scarcely provided
examples of novel classes and test-time data belong to the same domain.
However, this assumption does not hold in various industrial and robotics
applications, where a model can learn novel classes from a source domain while
inferring on classes from a target domain. In this work, we address the task of
zero-shot domain adaptation, also known as domain generalization, for FSOD.
Specifically, we assume that neither images nor labels of the novel classes in
the target domain are available during training. Our approach for solving the
domain gap is two-fold. First, we leverage a meta-training paradigm, where we
learn the domain shift on the base classes, then transfer the domain knowledge
to the novel classes. Second, we propose various data augmentations techniques
on the few shots of novel classes to account for all possible domain-specific
information. To constraint the network into encoding domain-agnostic
class-specific representations only, a contrastive loss is proposed to maximize
the mutual information between foreground proposals and class embeddings and
reduce the network's bias to the background information from target domain. Our
experiments on the T-LESS, PASCAL-VOC, and ExDark datasets show that the
proposed approach succeeds in alleviating the domain gap considerably without
utilizing labels or images of novel categories from the target domain.
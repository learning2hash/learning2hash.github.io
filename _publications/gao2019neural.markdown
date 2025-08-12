---
layout: publication
title: Neural Snowball For Few-shot Relation Learning
authors: Tianyu Gao, Xu Han, Ruobing Xie, Zhiyuan Liu, Fen Lin, Leyu Lin, Maosong
  Sun
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2020
bibkey: gao2019neural
citations: 61
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1908.11007'}]
tags: ["AAAI", "Few Shot & Zero Shot"]
short_authors: Gao et al.
---
Knowledge graphs typically undergo open-ended growth of new relations. This
cannot be well handled by relation extraction that focuses on pre-defined
relations with sufficient training data. To address new relations with few-shot
instances, we propose a novel bootstrapping approach, Neural Snowball, to learn
new relations by transferring semantic knowledge about existing relations. More
specifically, we use Relational Siamese Networks (RSN) to learn the metric of
relational similarities between instances based on existing relations and their
labeled data. Afterwards, given a new relation and its few-shot instances, we
use RSN to accumulate reliable instances from unlabeled corpora; these
instances are used to train a relation classifier, which can further identify
new facts of the new relation. The process is conducted iteratively like a
snowball. Experiments show that our model can gather high-quality instances for
better few-shot relation learning and achieves significant improvement compared
to baselines. Codes and datasets are released on
https://github.com/thunlp/Neural-Snowball.
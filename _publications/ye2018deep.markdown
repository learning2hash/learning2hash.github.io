---
layout: publication
title: Deep Triplet Ranking Networks For One-shot Recognition
authors: Meng Ye, Yuhong Guo
conference: Arxiv
year: 2018
bibkey: ye2018deep
citations: 32
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1804.07275'}]
tags: ["Supervised"]
short_authors: Meng Ye, Yuhong Guo
---
Despite the breakthroughs achieved by deep learning models in conventional
supervised learning scenarios, their dependence on sufficient labeled training
data in each class prevents effective applications of these deep models in
situations where labeled training instances for a subset of novel classes are
very sparse -- in the extreme case only one instance is available for each
class. To tackle this natural and important challenge, one-shot learning, which
aims to exploit a set of well labeled base classes to build classifiers for the
new target classes that have only one observed instance per class, has recently
received increasing attention from the research community. In this paper we
propose a novel end-to-end deep triplet ranking network to perform one-shot
learning. The proposed approach learns class universal image embeddings on the
well labeled base classes under a triplet ranking loss, such that the instances
from new classes can be categorized based on their similarity with the one-shot
instances in the learned embedding space. Moreover, our approach can naturally
incorporate the available one-shot instances from the new classes into the
embedding learning process to improve the triplet ranking model. We conduct
experiments on two popular datasets for one-shot learning. The results show the
proposed approach achieves better performance than the state-of-the- art
comparison methods.
---
layout: publication
title: Instance Image Retrieval By Learning Purely From Within The Dataset
authors: Zhang Zhongyan, Wang Lei, Wang Yang, Zhou Luping, Zhang Jianjia, Wang Peng,
  Chen Fang
conference: Arxiv
year: 2023
bibkey: zhang2022instance
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2208.06119'}]
tags: ["Datasets", "Evaluation", "Image Retrieval", "Self-Supervised"]
short_authors: Zhang et al.
---
Quality feature representation is key to instance image retrieval. To attain
it, existing methods usually resort to a deep model pre-trained on benchmark
datasets or even fine-tune the model with a task-dependent labelled auxiliary
dataset. Although achieving promising results, this approach is restricted by
two issues: 1) the domain gap between benchmark datasets and the dataset of a
given retrieval task; 2) the required auxiliary dataset cannot be readily
obtained. In light of this situation, this work looks into a different approach
which has not been well investigated for instance image retrieval previously:
\{can we learn feature representation \textit\{specific to\} a given retrieval
task in order to achieve excellent retrieval?\} Our finding is encouraging. By
adding an object proposal generator to generate image regions for
self-supervised learning, the investigated approach can successfully learn
feature representation specific to a given dataset for retrieval. This
representation can be made even more effective by boosting it with image
similarity information mined from the dataset. As experimentally validated,
such a simple ``self-supervised learning + self-boosting'' approach can well
compete with the relevant state-of-the-art retrieval methods. Ablation study is
conducted to show the appealing properties of this approach and its limitation
on generalisation across datasets.
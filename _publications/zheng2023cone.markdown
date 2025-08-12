---
layout: publication
title: 'Cone: Contrast Your Neighbours For Supervised Image Classification'
authors: Mingkai Zheng, Shan You, Lang Huang, Xiu Su, Fei Wang, Chen Qian, Xiaogang
  Wang, Chang Xu
conference: Arxiv
year: 2023
bibkey: zheng2023cone
citations: 1
additional_links: [{name: Code, url: 'https://github.com/mingkai-zheng/CoNe\}\{https://github.com/mingkai-zheng/CoNe\'},
  {name: Paper, url: 'https://arxiv.org/abs/2308.10761'}]
tags: []
short_authors: Zheng et al.
---
Image classification is a longstanding problem in computer vision and machine
learning research. Most recent works (e.g. SupCon , Triplet, and max-margin)
mainly focus on grouping the intra-class samples aggressively and compactly,
with the assumption that all intra-class samples should be pulled tightly
towards their class centers. However, such an objective will be very hard to
achieve since it ignores the intra-class variance in the dataset. (i.e.
different instances from the same class can have significant differences).
Thus, such a monotonous objective is not sufficient. To provide a more
informative objective, we introduce Contrast Your Neighbours (CoNe) - a simple
yet practical learning framework for supervised image classification.
Specifically, in CoNe, each sample is not only supervised by its class center
but also directly employs the features of its similar neighbors as anchors to
generate more adaptive and refined targets. Moreover, to further boost the
performance, we propose ``distributional consistency" as a more informative
regularization to enable similar instances to have a similar probability
distribution. Extensive experimental results demonstrate that CoNe achieves
state-of-the-art performance across different benchmark datasets, network
architectures, and settings. Notably, even without a complicated training
recipe, our CoNe achieves 80.8% Top-1 accuracy on ImageNet with ResNet-50,
which surpasses the recent Timm training recipe (80.4%). Code and pre-trained
models are available at
\href\{https://github.com/mingkai-zheng/CoNe\}\{https://github.com/mingkai-zheng/CoNe\}.
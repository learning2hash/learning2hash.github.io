---
layout: publication
title: Adversarial Learning For Personalized Tag Recommendation
authors: Erik Quintanilla, Yogesh Rawat, Andrey Sakryukin, Mubarak Shah, Mohan Kankanhalli
conference: IEEE Transactions on Multimedia
year: 2020
bibkey: quintanilla2020adversarial
citations: 27
additional_links: [{name: Code, url: 'https://github.com/vyzuer/ALTReco'}, {name: Paper,
    url: 'https://arxiv.org/abs/2004.00698'}]
tags: ["Recommender Systems"]
short_authors: Quintanilla et al.
---
We have recently seen great progress in image classification due to the
success of deep convolutional neural networks and the availability of
large-scale datasets. Most of the existing work focuses on single-label image
classification. However, there are usually multiple tags associated with an
image. The existing works on multi-label classification are mainly based on lab
curated labels. Humans assign tags to their images differently, which is mainly
based on their interests and personal tagging behavior. In this paper, we
address the problem of personalized tag recommendation and propose an
end-to-end deep network which can be trained on large-scale datasets. The
user-preference is learned within the network in an unsupervised way where the
network performs joint optimization for user-preference and visual encoding. A
joint training of user-preference and visual encoding allows the network to
efficiently integrate the visual preference with tagging behavior for a better
user recommendation. In addition, we propose the use of adversarial learning,
which enforces the network to predict tags resembling user-generated tags. We
demonstrate the effectiveness of the proposed model on two different
large-scale and publicly available datasets, YFCC100M and NUS-WIDE. The
proposed method achieves significantly better performance on both the datasets
when compared to the baselines and other state-of-the-art methods. The code is
publicly available at https://github.com/vyzuer/ALTReco.
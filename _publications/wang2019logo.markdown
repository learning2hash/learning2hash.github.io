---
layout: publication
title: 'Logo-2k+: A Large-scale Logo Dataset For Scalable Logo Classification'
authors: Jing Wang, Weiqing Min, Sujuan Hou, Shengnan Ma, Yuanjie Zheng, Haishuai
  Wang, Shuqiang Jiang
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2020
bibkey: wang2019logo
citations: 41
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1911.07924'}]
tags: ["AAAI", "Datasets", "Scalability"]
short_authors: Wang et al.
---
Logo classification has gained increasing attention for its various
applications, such as copyright infringement detection, product recommendation
and contextual advertising. Compared with other types of object images, the
real-world logo images have larger variety in logo appearance and more
complexity in their background. Therefore, recognizing the logo from images is
challenging. To support efforts towards scalable logo classification task, we
have curated a dataset, Logo-2K+, a new large-scale publicly available
real-world logo dataset with 2,341 categories and 167,140 images. Compared with
existing popular logo datasets, such as FlickrLogos-32 and LOGO-Net, Logo-2K+
has more comprehensive coverage of logo categories and larger quantity of logo
images. Moreover, we propose a Discriminative Region Navigation and
Augmentation Network (DRNA-Net), which is capable of discovering more
informative logo regions and augmenting these image regions for logo
classification. DRNA-Net consists of four sub-networks: the navigator
sub-network first selected informative logo-relevant regions guided by the
teacher sub-network, which can evaluate its confidence belonging to the
ground-truth logo class. The data augmentation sub-network then augments the
selected regions via both region cropping and region dropping. Finally, the
scrutinizer sub-network fuses features from augmented regions and the whole
image for logo classification. Comprehensive experiments on Logo-2K+ and other
three existing benchmark datasets demonstrate the effectiveness of proposed
method. Logo-2K+ and the proposed strong baseline DRNA-Net are expected to
further the development of scalable logo image recognition, and the Logo-2K+
dataset can be found at https://github.com/msn199959/Logo-2k-plus-Dataset.
---
layout: publication
title: Towards Efficient Unconstrained Palmprint Recognition Via Deep Distillation
  Hashing
authors: Huikai Shao, Dexing Zhong, Xuefeng Du
conference: Arxiv
year: 2020
bibkey: shao2020towards
citations: 8
additional_links: [{name: Code, url: 'http://gr.xjtu.edu.cn/web/bell/resource'}, {
    name: Paper, url: 'https://arxiv.org/abs/2004.03303'}]
tags: [Compact Codes, Evaluation, Efficiency, Datasets, Hashing Methods]
short_authors: Huikai Shao, Dexing Zhong, Xuefeng Du
---
Deep palmprint recognition has become an emerging issue with great potential
for personal authentication on handheld and wearable consumer devices. Previous
studies of palmprint recognition are mainly based on constrained datasets
collected by dedicated devices in controlled environments, which has to reduce
the flexibility and convenience. In addition, general deep palmprint
recognition algorithms are often too heavy to meet the real-time requirements
of embedded system. In this paper, a new palmprint benchmark is established,
which consists of more than 20,000 images collected by 5 brands of smart phones
in an unconstrained manner. Each image has been manually labeled with 14 key
points for region of interest (ROI) extraction. Further, the approach called
Deep Distillation Hashing (DDH) is proposed as benchmark for efficient deep
palmprint recognition. Palmprint images are converted to binary codes to
improve the efficiency of feature matching. Derived from knowledge
distillation, novel distillation loss functions are constructed to compress
deep model to further improve the efficiency of feature extraction on light
network. Comprehensive experiments are conducted on both constrained and
unconstrained palmprint databases. Using DDH, the accuracy of palmprint
identification can be increased by up to 11.37%, and the Equal Error Rate (EER)
of palmprint verification can be reduced by up to 3.11%. The results indicate
the feasibility of our database, and DDH can outperform other baselines to
achieve the state-of-the-art performance. The collected dataset and related
source codes are publicly available at http://gr.xjtu.edu.cn/web/bell/resource.
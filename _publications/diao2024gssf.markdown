---
layout: publication
title: 'GSSF: Generalized Structural Sparse Function For Deep Cross-modal Metric Learning'
authors: Haiwen Diao, Ying Zhang, Shang Gao, Jiawen Zhu, Long Chen, Huchuan Lu
conference: IEEE Transactions on Image Processing
year: 2024
bibkey: diao2024gssf
citations: 4
additional_links: [{name: Code, url: 'https://github.com/Paranioar/GSSF'}, {name: Paper,
    url: 'https://arxiv.org/abs/2410.15266'}]
tags: ["Distance Metric Learning", "Image Retrieval", "Text Retrieval", "Tools & Libraries"]
short_authors: Diao et al.
---
Cross-modal metric learning is a prominent research topic that bridges the
semantic heterogeneity between vision and language. Existing methods frequently
utilize simple cosine or complex distance metrics to transform the pairwise
features into a similarity score, which suffers from an inadequate or
inefficient capability for distance measurements. Consequently, we propose a
Generalized Structural Sparse Function to dynamically capture thorough and
powerful relationships across modalities for pair-wise similarity learning
while remaining concise but efficient. Specifically, the distance metric
delicately encapsulates two formats of diagonal and block-diagonal terms,
automatically distinguishing and highlighting the cross-channel relevancy and
dependency inside a structured and organized topology. Hence, it thereby
empowers itself to adapt to the optimal matching patterns between the paired
features and reaches a sweet spot between model complexity and capability.
Extensive experiments on cross-modal and two extra uni-modal retrieval tasks
(image-text retrieval, person re-identification, fine-grained image retrieval)
have validated its superiority and flexibility over various popular retrieval
frameworks. More importantly, we further discover that it can be seamlessly
incorporated into multiple application scenarios, and demonstrates promising
prospects from Attention Mechanism to Knowledge Distillation in a plug-and-play
manner. Our code is publicly available at: https://github.com/Paranioar/GSSF.
---
layout: publication
title: 'PC\(^2\): Pseudo-classification Based Pseudo-captioning For Noisy Correspondence
  Learning In Cross-modal Retrieval'
authors: Yue Duan, Zhangxuan Gu, Zhenzhe Ying, Lei Qi, Changhua Meng, Yinghuan Shi
conference: Proceedings of the 32nd ACM International Conference on Multimedia
year: 2024
bibkey: duan2024pc
citations: 1
additional_links: [{name: Code, url: 'https://github.com/alipay/PC2-NoiseofWeb'},
  {name: Paper, url: 'https://arxiv.org/abs/2408.01349'}]
tags: ["Datasets", "Evaluation", "Multimodal Retrieval"]
short_authors: Duan et al.
---
In the realm of cross-modal retrieval, seamlessly integrating diverse
modalities within multimedia remains a formidable challenge, especially given
the complexities introduced by noisy correspondence learning (NCL). Such noise
often stems from mismatched data pairs, which is a significant obstacle
distinct from traditional noisy labels. This paper introduces
Pseudo-Classification based Pseudo-Captioning (PC\(^2\)) framework to address
this challenge. PC\(^2\) offers a threefold strategy: firstly, it establishes an
auxiliary "pseudo-classification" task that interprets captions as categorical
labels, steering the model to learn image-text semantic similarity through a
non-contrastive mechanism. Secondly, unlike prevailing margin-based techniques,
capitalizing on PC\(^2\)'s pseudo-classification capability, we generate
pseudo-captions to provide more informative and tangible supervision for each
mismatched pair. Thirdly, the oscillation of pseudo-classification is borrowed
to assistant the correction of correspondence. In addition to technical
contributions, we develop a realistic NCL dataset called Noise of Web (NoW),
which could be a new powerful NCL benchmark where noise exists naturally.
Empirical evaluations of PC\(^2\) showcase marked improvements over existing
state-of-the-art robust cross-modal retrieval techniques on both simulated and
realistic datasets with various NCL settings. The contributed dataset and
source code are released at https://github.com/alipay/PC2-NoiseofWeb.
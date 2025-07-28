---
layout: publication
title: 'COMAE: Comprehensive Attribute Exploration For Zero-shot Hashing'
authors: Yuqi Li, Qingqing Long, Yihang Zhou, Ran Zhang, Zhiyuan Ning, Zhihong Zhu,
  Yuanchun Zhou, Xuezhi Wang, Meng Xiao
conference: Arxiv
year: 2024
bibkey: li2024comae
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2402.16424'}]
tags: ["Few Shot & Zero Shot", "Hashing Methods"]
short_authors: Li et al.
---
Zero-shot hashing (ZSH) has shown excellent success owing to its efficiency and generalization in large-scale retrieval scenarios. While considerable success has been achieved, there still exist urgent limitations. Existing works ignore the locality relationships of representations and attributes, which have effective transferability between seeable classes and unseeable classes. Also, the continuous-value attributes are not fully harnessed. In response, we conduct a COMprehensive Attribute Exploration for ZSH, named COMAE, which depicts the relationships from seen classes to unseen ones through three meticulously designed explorations, i.e., point-wise, pair-wise and class-wise consistency constraints. By regressing attributes from the proposed attribute prototype network, COMAE learns the local features that are relevant to the visual attributes. Then COMAE utilizes contrastive learning to comprehensively depict the context of attributes, rather than instance-independent optimization. Finally, the class-wise constraint is designed to cohesively learn the hash code, image representation, and visual attributes more effectively. Experimental results on the popular ZSH datasets demonstrate that COMAE outperforms state-of-the-art hashing techniques, especially in scenarios with a larger number of unseen label classes.
---
layout: publication
title: "COMAE: COMprehensive Attribute Exploration for Zero-shot Hashing"
authors: Li Yuqi, Long Qingqing, Zhou Yihang, Cao Ning, Liu Shuai, Zheng Fang, Zhu Zhihong, Ning Zhiyuan, Xiao Meng, Wang Xuezhi, Wang Pengfei, Zhou Yuanchun
conference: Arxiv
year: 2024
bibkey: li2024comae
additional_links:
- {name: "Paper", url: "https://arxiv.org/abs/2402.16424"}
tags: ['ARXIV']
---
Zero-shot hashing (ZSH) has shown excellent success owing to its efficiency and generalization in large-scale retrieval scenarios. While considerable success has been achieved, there still exist urgent limitations. Existing works ignore the locality relationships of representations and attributes, which have effective transferability between seeable classes and unseeable classes. Also, the continuous-value attributes are not fully harnessed. In response, we conduct a COMprehensive Attribute Exploration for ZSH, named COMAE, which depicts the relationships from seen classes to unseen ones through three meticulously designed explorations, i.e., point-wise, pair-wise and class-wise consistency constraints. By regressing attributes from the proposed attribute prototype network, COMAE learns the local features that are relevant to the visual attributes. Then COMAE utilizes contrastive learning to comprehensively depict the context of attributes, rather than instance-independent optimization. Finally, the class-wise constraint is designed to cohesively learn the hash code, image representation, and visual attributes more effectively. Experimental results on the popular ZSH datasets demonstrate that COMAE outperforms state-of-the-art hashing techniques, especially in scenarios with a larger number of unseen label classes.
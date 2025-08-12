---
layout: publication
title: 'Pgnet: Real-time Arbitrarily-shaped Text Spotting With Point Gathering Network'
authors: Pengfei Wang, Chengquan Zhang, Fei Qi, Shanshan Liu, Xiaoqiang Zhang, Pengyuan
  Lyu, Junyu Han, Jingtuo Liu, Errui Ding, Guangming Shi
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2021
bibkey: wang2021pgnet
citations: 68
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.05458'}]
tags: ["AAAI", "Efficiency"]
short_authors: Wang et al.
---
The reading of arbitrarily-shaped text has received increasing research
attention. However, existing text spotters are mostly built on two-stage
frameworks or character-based methods, which suffer from either Non-Maximum
Suppression (NMS), Region-of-Interest (RoI) operations, or character-level
annotations. In this paper, to address the above problems, we propose a novel
fully convolutional Point Gathering Network (PGNet) for reading
arbitrarily-shaped text in real-time. The PGNet is a single-shot text spotter,
where the pixel-level character classification map is learned with proposed
PG-CTC loss avoiding the usage of character-level annotations. With a PG-CTC
decoder, we gather high-level character classification vectors from
two-dimensional space and decode them into text symbols without NMS and RoI
operations involved, which guarantees high efficiency. Additionally, reasoning
the relations between each character and its neighbors, a graph refinement
module (GRM) is proposed to optimize the coarse recognition and improve the
end-to-end performance. Experiments prove that the proposed method achieves
competitive accuracy, meanwhile significantly improving the running speed. In
particular, in Total-Text, it runs at 46.7 FPS, surpassing the previous
spotters with a large margin.
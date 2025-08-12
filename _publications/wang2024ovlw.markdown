---
layout: publication
title: 'OVLW-DETR: Open-vocabulary Light-weighted Detection Transformer'
authors: Yu Wang, Xiangbo Su, Qiang Chen, Xinyu Zhang, Teng Xi, Kun Yao, Errui Ding,
  Gang Zhang, Jingdong Wang
conference: Arxiv
year: 2024
bibkey: wang2024ovlw
citations: 0
additional_links: [{name: Code, url: 'https://github.com/Atten4Vis/LW-DETR]'}, {name: Paper,
    url: 'https://arxiv.org/abs/2407.10655'}]
tags: ["Efficiency", "Few Shot & Zero Shot", "Transformer Based ANN"]
short_authors: Wang et al.
---
Open-vocabulary object detection focusing on detecting novel categories
guided by natural language. In this report, we propose Open-Vocabulary
Light-Weighted Detection Transformer (OVLW-DETR), a deployment friendly
open-vocabulary detector with strong performance and low latency. Building upon
OVLW-DETR, we provide an end-to-end training recipe that transferring knowledge
from vision-language model (VLM) to object detector with simple alignment. We
align detector with the text encoder from VLM by replacing the fixed
classification layer weights in detector with the class-name embeddings
extracted from the text encoder. Without additional fusing module, OVLW-DETR is
flexible and deployment friendly, making it easier to implement and modulate.
improving the efficiency of interleaved attention computation. Experimental
results demonstrate that the proposed approach is superior over existing
real-time open-vocabulary detectors on standard Zero-Shot LVIS benchmark.
Source code and pre-trained models are available at
[https://github.com/Atten4Vis/LW-DETR].
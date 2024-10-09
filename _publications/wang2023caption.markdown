---
layout: publication
title: Caption Anything Interactive Image Description With Diverse Multimodal Controls
authors: Teng Wang, Jinrui Zhang, Junjie Fei, Hao Zheng, Yunlong Tang, Zhe Li, Mingqi Gao, Shanshan Zhao
conference: "Arxiv"
year: 2023
bibkey: wang2023caption
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2305.02677v3"}
  - {name: "Code", url: "https://github.com/ttengwang/Caption-Anything"}
tags: ['ARXIV', 'Case Study', 'Cross Modal', 'Has Code']
---
Controllable image captioning is an emerging multimodal topic that aims to describe the image with natural language following human purpose () looking at the specified regions or telling in a particular text style. State-of-the-art methods are trained on annotated pairs of input controls and output captions. However the scarcity of such well-annotated multimodal data largely limits their usability and scalability for interactive AI systems. Leveraging unimodal instruction-following foundation models is a promising alternative that benefits from broader sources of data. In this paper we present Caption AnyThing (CAT) a foundation model augmented image captioning framework supporting a wide range of multimodel controls 1) visual controls including points boxes and trajectories; 2) language controls such as sentiment length language and factuality. Powered by Segment Anything Model (SAM) and ChatGPT we unify the visual and language prompts into a modularized framework enabling the flexible combination between different controls. Extensive case studies demonstrate the user intention alignment capabilities of our framework shedding light on effective user interaction modeling in vision-language applications. Our code is publicly available at https://github.com/ttengwang/Caption-Anything.

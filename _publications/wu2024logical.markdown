---
layout: publication
title: Logical Closed Loop Uncovering Object Hallucinations In Large Vision-language Models
authors: Junfei Wu, Qiang Liu, Ding Wang, Jinghao Zhang, Shu Wu, Liang Wang, Tieniu Tan
conference: "Arxiv"
year: 2024
bibkey: wu2024logical
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2402.11622v2"}
tags: ['ARXIV', 'Cross Modal']
---
Object hallucination has been an Achilles heel which hinders the broader applications of large vision-language models (LVLMs). Object hallucination refers to the phenomenon that the LVLMs claim non-existent objects in the image. To mitigate the object hallucinations instruction tuning and external model-based detection methods have been proposed which either require large-scare computational resources or depend on the detection result of external models. However there remains an under-explored field to utilize the LVLM itself to alleviate object hallucinations. In this work we adopt the intuition that the LVLM tends to respond logically consistently for existent objects but inconsistently for hallucinated objects. Therefore we propose a Logical Closed Loop-based framework for Object Hallucination Detection and Mitigation namely LogicCheckGPT. In specific we devise logical consistency probing to raise questions with logical correlations inquiring about attributes from objects and vice versa. Whether their responses can form a logical closed loop serves as an indicator of object hallucination. As a plug-and-play method it can be seamlessly applied to all existing LVLMs. Comprehensive experiments conducted on three benchmarks across four LVLMs have demonstrated significant improvements brought by our method indicating its effectiveness and generality.

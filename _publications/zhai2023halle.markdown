---
layout: publication
title: Halle-control Controlling Object Hallucination In Large Multimodal Models
authors: Bohan Zhai, Shijia Yang, Chenfeng Xu, Sheng Shen, Kurt Keutzer, Chunyuan Li, Manling Li
conference: "Arxiv"
year: 2023
bibkey: zhai2023halle
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2310.01779v3"}
tags: ['ARXIV', 'Cross Modal']
---
Current Large Multimodal Models (LMMs) achieve remarkable progress yet there remains significant uncertainty regarding their ability to accurately apprehend visual details that is in performing detailed captioning. To address this we introduce () a GPT-4 assisted evaluation method for detailed captioning. Interestingly while LMMs demonstrate minimal object existence hallucination in existing VQA benchmarks our proposed evaluation reveals continued susceptibility to such hallucinations. In this paper we make the first attempt to investigate such hallucination from different aspects including image resolution the language decoder size and instruction data amount quality granularity. Our findings underscore the unwarranted inference when the language description includes details at a finer object granularity than what the vision module can ground or verify thus inducing hallucination. To control such hallucinations we further attribute the reliability of captioning to contextual knowledge (involving only contextually grounded objects) and parametric knowledge (containing inferred objects by the model). Thus we introduce () a controllable LMM in terms of ()ucination in object ()xistence. HallE-Control can condition the captioning to shift between (i) exclusively depicting contextual knowledge for grounded objects and (ii) blending it with parametric knowledge to imagine inferred objects. Our method reduces hallucination by 4437; compared to LLaVA(_7B) and maintains the object coverage.

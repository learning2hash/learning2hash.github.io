---
layout: publication
title: FIHA Autonomous Hallucination Evaluation In Vision-language Models With Davidson Scene Graphs
authors: Bowen Yan, Zhengsong Zhang, Liqiang Jing, Eftekhar Hossain, Xinya Du
conference: "Arxiv"
year: 2024
bibkey: yan2024fiha
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2409.13612v1"}
tags: ['ARXIV', 'Cross Modal', 'Graph']
---
The rapid development of Large Vision-Language Models (LVLMs) often comes with widespread hallucination issues making cost-effective and comprehensive assessments increasingly vital. Current approaches mainly rely on costly annotations and are not comprehensive -- in terms of evaluating all aspects such as relations attributes and dependencies between aspects. Therefore we introduce the FIHA (autonomous Fine-graIned Hallucination evAluation evaluation in LVLMs) which could access hallucination LVLMs in the LLM-free and annotation-free way and model the dependency between different types of hallucinations. FIHA can generate Qamp;A pairs on any image dataset at minimal cost enabling hallucination assessment from both image and caption. Based on this approach we introduce a benchmark called FIHA-v1 which consists of diverse questions on various images from MSCOCO and Foggy. Furthermore we use the Davidson Scene Graph (DSG) to organize the structure among Qamp;A pairs in which we can increase the reliability of the evaluation. We evaluate representative models using FIHA-v1 highlighting their limitations and challenges. We released our code and data.

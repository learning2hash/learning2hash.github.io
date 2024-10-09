---
layout: publication
title: Explainable Multimodal Emotion Recognition
authors: Zheng Lian, Haiyang Sun, Licai Sun, Hao Gu, Zhuofan Wen, Siyuan Zhang, Shun Chen, Mingyu Xu, Ke Xu, Kang Chen, Lan Chen, Shan Liang, Ya Li, Jiangyan Yi, Bin Liu, Jianhua Tao
conference: "Arxiv"
year: 2023
bibkey: lian2023explainable
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2306.15401v6"}
tags: ['ARXIV', 'Cross Modal']
---
Multimodal emotion recognition is an important research topic in artificial intelligence whose main goal is to integrate multimodal clues to identify human emotional states. Current works generally assume accurate labels for benchmark datasets and focus on developing more effective architectures. However emotion annotation relies on subjective judgment. To obtain more reliable labels existing datasets usually restrict the label space to some basic categories then hire plenty of annotators and use majority voting to select the most likely label. However this process may result in some correct but non-candidate or non-majority labels being ignored. To ensure reliability without ignoring subtle emotions we propose a new task called Explainable Multimodal Emotion Recognition (EMER). Unlike traditional emotion recognition EMER takes a step further by providing explanations for these predictions. Through this task we can extract relatively reliable labels since each label has a certain basis. Meanwhile we borrow large language models (LLMs) to disambiguate unimodal clues and generate more complete multimodal explanations. From them we can extract richer emotions in an open-vocabulary manner. This paper presents our initial attempt at this task including introducing a new dataset establishing baselines and defining evaluation metrics. In addition EMER can serve as a benchmark task to evaluate the audio-video-text understanding performance of multimodal LLMs.

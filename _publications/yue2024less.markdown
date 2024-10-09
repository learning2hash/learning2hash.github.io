---
layout: publication
title: Less Is More Mitigating Multimodal Hallucination From An EOS Decision Perspective
authors: Zihao Yue, Liang Zhang, Qin Jin
conference: "Arxiv"
year: 2024
bibkey: yue2024less
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2402.14545v2"}
tags: ['ARXIV', 'Cross Modal', 'Supervised']
---
Large Multimodal Models (LMMs) often suffer from multimodal hallucinations wherein they may create content that is not present in the visual inputs. In this paper we explore a new angle of this issue overly detailed training data hinders the models ability to timely terminate generation leading to continued outputs beyond visual perception limits. By investigating how the model decides to terminate generation with EOS the special end-of-sentence token we find that the model assesses the completeness of the entire sequence by comparing the generated text with the image. This observation suggests that the model possesses an inherent potential of making proper EOS decisions based on its visual perception to avoid overly lengthy outputs. To take advantage of such potential we explore two methods to mitigate multimodal hallucinations a training objective that enables the model to reduce hallucinations by learning from regular instruction data and a data filtering strategy to prevent harmful training data from exacerbating model hallucinations. Both methods significantly improve the hallucination performance of LMMs without requiring any additional data or knowledge.

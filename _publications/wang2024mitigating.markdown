---
layout: publication
title: Mitigating Hallucinations In Large Vision-language Models With Instruction Contrastive Decoding
authors: Xintong Wang, Jingheng Pan, Liang Ding, Chris Biemann
conference: "Arxiv"
year: 2024
bibkey: wang2024mitigating
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2403.18715v2"}
tags: ['ARXIV', 'Cross Modal']
---
Large Vision-Language Models (LVLMs) are increasingly adept at generating contextually detailed and coherent responses from visual inputs. However their application in multimodal decision-making and open-ended generation is hindered by a notable rate of hallucinations where generated text inaccurately represents the visual contents. To address this issue this paper introduces the Instruction Contrastive Decoding (ICD) method a novel approach designed to reduce hallucinations during LVLM inference. Our method is inspired by our observation that what we call disturbance instructions significantly exacerbate hallucinations in multimodal fusion modules. ICD contrasts distributions from standard and instruction disturbance thereby increasing alignment uncertainty and effectively subtracting hallucinated concepts from the original distribution. Through comprehensive experiments on discriminative benchmarks (POPE and MME) and a generative benchmark (LLaVa-Bench) we demonstrate that ICD significantly mitigates both object-level and attribute-level hallucinations. Moreover our method not only addresses hallucinations but also significantly enhances the general perception and recognition capabilities of LVLMs.

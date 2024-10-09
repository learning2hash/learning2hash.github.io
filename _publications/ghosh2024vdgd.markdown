---
layout: publication
title: VDGD Mitigating LVLM Hallucinations In Cognitive Prompts By Bridging The Visual Perception Gap
authors: Sreyan Ghosh, Chandra Kiran Reddy Evuru, Sonal Kumar, Utkarsh Tyagi, Oriol Nieto, Zeyu Jin, Dinesh Manocha
conference: "Arxiv"
year: 2024
bibkey: ghosh2024vdgd
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2405.15683v1"}
tags: ['ARXIV', 'Cross Modal']
---
Recent interest in Large Vision-Language Models (LVLMs) for practical applications is moderated by the significant challenge of hallucination or the inconsistency between the factual information and the generated text. In this paper we first perform an in-depth analysis of hallucinations and discover several novel insights about how and when LVLMs hallucinate. From our analysis we show that (1) The communitys efforts have been primarily targeted towards reducing hallucinations related to visual recognition (VR) prompts (e.g. prompts that only require describing the image) thereby ignoring hallucinations for cognitive prompts (e.g. prompts that require additional skills like reasoning on contents of the image). (2) LVLMs lack visual perception i.e. they can see but not necessarily understand or perceive the input image. We analyze responses to cognitive prompts and show that LVLMs hallucinate due to a perception gap although LVLMs accurately recognize visual elements in the input image and possess sufficient cognitive skills they struggle to respond accurately and hallucinate. To overcome this shortcoming we propose Visual Description Grounded Decoding (VDGD) a simple robust and training-free method for alleviating hallucinations. Specifically we first describe the image and add it as a prefix to the instruction. Next during auto-regressive decoding we sample from the plausible candidates according to their KL-Divergence (KLD) to the description where lower KLD is given higher preference. Experimental results on several benchmarks and LVLMs show that VDGD improves significantly over other baselines in reducing hallucinations. We also propose VaLLu a benchmark for the comprehensive evaluation of the cognitive capabilities of LVLMs.

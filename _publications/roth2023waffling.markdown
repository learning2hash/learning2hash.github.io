---
layout: publication
title: 'Waffling Around For Performance: Visual Classification With Random Words And
  Broad Concepts'
authors: Karsten Roth, Jae Myung Kim, A. Sophia Koepke, Oriol Vinyals, Cordelia Schmid,
  Zeynep Akata
conference: 2023 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2023
bibkey: roth2023waffling
citations: 25
additional_links: [{name: Code, url: 'https://github.com/ExplainableML/WaffleCLIP'},
  {name: Paper, url: 'https://arxiv.org/abs/2306.07282'}]
tags: ["ICCV"]
short_authors: Roth et al.
---
The visual classification performance of vision-language models such as CLIP
has been shown to benefit from additional semantic knowledge from large
language models (LLMs) such as GPT-3. In particular, averaging over
LLM-generated class descriptors, e.g. "waffle, which has a round shape", can
notably improve generalization performance. In this work, we critically study
this behavior and propose WaffleCLIP, a framework for zero-shot visual
classification which simply replaces LLM-generated descriptors with random
character and word descriptors. Without querying external models, we achieve
comparable performance gains on a large number of visual classification tasks.
This allows WaffleCLIP to both serve as a low-cost alternative, as well as a
sanity check for any future LLM-based vision-language model extensions. We
conduct an extensive experimental study on the impact and shortcomings of
additional semantics introduced with LLM-generated descriptors, and showcase
how - if available - semantic context is better leveraged by querying LLMs for
high-level concepts, which we show can be done to jointly resolve potential
class name ambiguities. Code is available here:
https://github.com/ExplainableML/WaffleCLIP.
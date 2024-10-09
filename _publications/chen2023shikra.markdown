---
layout: publication
title: Shikra Unleashing Multimodal Llms Referential Dialogue Magic
authors: Keqin Chen, Zhao Zhang, Weili Zeng, Richong Zhang, Feng Zhu, Rui Zhao
conference: "Arxiv"
year: 2023
bibkey: chen2023shikra
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2306.15195v2"}
  - {name: "Code", url: "https://github.com/shikras/shikra"}
tags: ['ARXIV', 'Cross Modal', 'Has Code']
---
In human conversations individuals can indicate relevant regions within a scene while addressing others. In turn the other person can then respond by referring to specific regions if necessary. This natural referential ability in dialogue remains absent in current Multimodal Large Language Models (MLLMs). To fill this gap this paper proposes an MLLM called Shikra which can handle spatial coordinate inputs and outputs in natural language. Its architecture consists of a vision encoder an alignment layer and a LLM. It is designed to be straightforward and simple without the need for extra vocabularies position encoder pre-/post-detection modules or external plug-in models. All inputs and outputs are in natural language form. Referential dialogue is a superset of various vision-language (VL) tasks. Shikra can naturally handle location-related tasks like REC and PointQA as well as conventional VL tasks such as Image Captioning and VQA. Experimental results showcase Shikras promising performance. Furthermore it enables numerous exciting applications like providing mentioned objects coordinates in chains of thoughts and comparing user-pointed regions similarities. Our code model and dataset are accessed at https://github.com/shikras/shikra.

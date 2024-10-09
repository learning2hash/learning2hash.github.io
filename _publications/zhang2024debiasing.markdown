---
layout: publication
title: Debiasing Multimodal Large Language Models
authors: Yi-fan Zhang, Weichen Yu, Qingsong Wen, Xue Wang, Zhang Zhang, Liang Wang, Rong Jin, Tieniu Tan
conference: "Arxiv"
year: 2024
bibkey: zhang2024debiasing
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2403.05262v2"}
tags: ['ARXIV', 'Cross Modal', 'Supervised']
---
In the realms of computer vision and natural language processing Large Vision-Language Models (LVLMs) have become indispensable tools proficient in generating textual descriptions based on visual inputs. Despite their advancements our investigation reveals a noteworthy bias in the generated content where the output is primarily influenced by the underlying Large Language Models (LLMs) prior rather than the input image. Our empirical experiments underscore the persistence of this bias as LVLMs often provide confident answers even in the absence of relevant images or given incongruent visual input. To rectify these biases and redirect the models focus toward vision information we introduce two simple training-free strategies. Firstly for tasks such as classification or multi-choice question-answering (QA) we propose a calibration step through affine transformation to adjust the output distribution. This Post-Hoc debias approach ensures uniform scores for each answer when the image is absent serving as an effective regularization technique to alleviate the influence of LLM priors. For more intricate open-ended generation tasks we extend this method to Debias sampling drawing inspirations from contrastive decoding methods. Furthermore our investigation sheds light on the instability of LVLMs across various decoding configurations. Through systematic exploration of different settings we significantly enhance performance surpassing reported results and raising concerns about the fairness of existing evaluations. Comprehensive experiments substantiate the effectiveness of our proposed strategies in mitigating biases. These strategies not only prove beneficial in minimizing hallucinations but also contribute to the generation of more helpful and precise illustrations.

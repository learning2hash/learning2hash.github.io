---
layout: publication
title: Compositional Image Retrieval Via Instruction-aware Contrastive Learning
authors: Wenliang Zhong, Weizhi An, Feng Jiang, Hehuan Ma, Yuzhi Guo, Junzhou Huang
conference: Arxiv
year: 2024
bibkey: zhong2024compositional
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.05756'}]
tags: [Evaluation, Image Retrieval, Few-shot & Zero-shot, Self-Supervised, Datasets]
short_authors: Zhong et al.
---
Composed Image Retrieval (CIR) involves retrieving a target image based on a
composed query of an image paired with text that specifies modifications or
changes to the visual reference. CIR is inherently an instruction-following
task, as the model needs to interpret and apply modifications to the image. In
practice, due to the scarcity of annotated data in downstream tasks, Zero-Shot
CIR (ZS-CIR) is desirable. While existing ZS-CIR models based on CLIP have
shown promising results, their capability in interpreting and following
modification instructions remains limited. Some research attempts to address
this by incorporating Large Language Models (LLMs). However, these approaches
still face challenges in effectively integrating multimodal information and
instruction understanding. To tackle above challenges, we propose a novel
embedding method utilizing an instruction-tuned Multimodal LLM (MLLM) to
generate composed representation, which significantly enhance the instruction
following capability for a comprehensive integration between images and
instructions. Nevertheless, directly applying MLLMs introduces a new challenge
since MLLMs are primarily designed for text generation rather than embedding
extraction as required in CIR. To address this, we introduce a two-stage
training strategy to efficiently learn a joint multimodal embedding space and
further refining the ability to follow modification instructions by tuning the
model in a triplet dataset similar to the CIR format. Extensive experiments on
four public datasets: FashionIQ, CIRR, GeneCIS, and CIRCO demonstrates the
superior performance of our model, outperforming state-of-the-art baselines by
a significant margin. Codes are available at the GitHub repository.
---
layout: publication
title: Detecting And Preventing Hallucinations In Large Vision Language Models
authors: Anisha Gunjal, Jihan Yin, Erhan Bas
conference: "Arxiv"
year: 2023
bibkey: gunjal2023detecting
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2308.06394v3"}
tags: ['ARXIV']
---
Instruction tuned Large Vision Language Models (LVLMs) have significantly advanced in generalizing across a diverse set of multi-modal tasks especially for Visual Question Answering (VQA). However generating detailed responses that are visually grounded is still a challenging task for these models. We find that even the current state-of-the-art LVLMs (InstructBLIP) still contain a staggering 30 percent of the hallucinatory text in the form of non-existent objects unfaithful descriptions and inaccurate relationships. To address this we introduce M-HalDetect a (M)ultimodal (Hal)lucination (Detect)ion Dataset that can be used to train and benchmark models for hallucination detection and prevention. M-HalDetect consists of 16k fine-grained annotations on VQA examples making it the first comprehensive multi-modal hallucination detection dataset for detailed image descriptions. Unlike previous work that only consider object hallucination we additionally annotate both entity descriptions and relationships that are unfaithful. To demonstrate the potential of this dataset for hallucination prevention we optimize InstructBLIP through our novel Fine-grained Direct Preference Optimization (FDPO). We also train fine-grained multi-modal reward models from InstructBLIP and evaluate their effectiveness with best-of-n rejection sampling. We perform human evaluation on both FDPO and rejection sampling and find that they reduce hallucination rates in InstructBLIP by 4137; and 5537; respectively. We also find that our reward model generalizes to other multi-modal models reducing hallucinations in LLaVA and mPLUG-OWL by 1537; and 5737; respectively and has strong correlation with human evaluated accuracy scores.

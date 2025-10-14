---
layout: publication
title: 'Modernvbert: Towards Smaller Visual Document Retrievers'
authors: "Paul Teiletche, Quentin Mac\xC9, Max Conti, Antonio Loison, Gautier Viaud,\
  \ Pierre Colombo, Manuel Faysse"
conference: Arxiv
year: 2025
bibkey: teiletche2025modernvbert
citations: 0
additional_links: [{name: Code, url: 'https://huggingface.co/ModernVBERT'}, {name: Paper,
    url: 'https://arxiv.org/abs/2510.01149'}]
tags: ["Distance Metric Learning", "Evaluation", "Text Retrieval"]
short_authors: Teiletche et al.
---
Multimodal embedding models are gaining prevalence, notably for document retrieval as efficient alternatives to text-only pipelines. These models are typically built by finetuning large vision-language decoders (VLMs) with contrastive losses on text-image pairs. In this work, we show that, while cost-efficient, this repurposing approach often bottlenecks retrieval performance. Through controlled experiments, we establish a principled recipe for improving visual document retrieval models. We notably measure the impact of attention masking, image resolution, modality alignment data regimes, and late interaction centered contrastive objectives which emerge as central performance factors. Building on these insights, we release ModernVBERT, a compact 250M-parameter vision-language encoder that outperforms models up to 10 times larger when finetuned on document retrieval tasks. Models and code are made available at https://huggingface.co/ModernVBERT.
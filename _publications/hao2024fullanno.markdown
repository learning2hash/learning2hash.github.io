---
layout: publication
title: 'Fullanno: A Data Engine For Enhancing Image Comprehension Of Mllms'
authors: Jing Hao, Yuxiang Zhao, Song Chen, Yanpeng Sun, Qiang Chen, Gang Zhang, Kun
  Yao, Errui Ding, Jingdong Wang
conference: Arxiv
year: 2024
bibkey: hao2024fullanno
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2409.13540'}]
tags: []
short_authors: Hao et al.
---
Multimodal Large Language Models (MLLMs) have shown promise in a broad range
of vision-language tasks with their strong reasoning and generalization
capabilities. However, they heavily depend on high-quality data in the
Supervised Fine-Tuning (SFT) phase. The existing approaches aim to curate
high-quality data via GPT-4V, but they are not scalable due to the commercial
nature of GPT-4V and the simplicity of the prompts used to instruct the model.
To this end, we devised the FullAnno system, which is a data engine that can
generate large-scale, high-quality, and fine-grained image annotations
consisting of the category and position of objects, region descriptions, text
information, as well as image dense captions. This engine is characterized by
its cascade annotation process, which involves multiple expert models and
employs rich prompts to instruct LLMs in generating dense image captions. We
re-annotated the COCO and Visual Genome datasets using our FullAnno system,
tripling the number of object annotations and increasing the length of the
original image captions by a factor of 15. Experiments show that the
regenerated annotation can significantly enhance the capabilities of LLaVA-v1.5
on several benchmarks. The re-annotated data are available at:
https://arcana-project-page.github.io
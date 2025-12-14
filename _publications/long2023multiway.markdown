---
layout: publication
title: 'Multiway-adapater: Adapting Large-scale Multi-modal Models For Scalable Image-text
  Retrieval'
authors: Zijun Long, George Killick, Richard McCreadie, Gerardo Aragon Camarasa
conference: Arxiv
year: 2023
bibkey: long2023multiway
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2309.01516'}]
tags: [Text Retrieval, Tools & Libraries, Scalability]
short_authors: Long et al.
---
As Multimodal Large Language Models (MLLMs) grow in size, adapting them to
specialized tasks becomes increasingly challenging due to high computational
and memory demands. Indeed, traditional fine-tuning methods are costly, due to
the need for extensive, task-specific training. While efficient adaptation
methods exist that aim to reduce these costs, in practice they suffer from
shallow inter-modal alignment, which severely hurts model effectiveness. To
tackle these computational challenges and improve inter-modal alignment, we
introduce the MultiWay-Adapter (MWA), a novel framework featuring an 'Alignment
Enhancer'. This enhancer deepens inter-modal alignment, enabling high
transferability with minimal tuning effort. Our experiments show that unlike
prior efficient tuning approaches, MWA maintains model effectiveness, while
reducing training time by up-to 57%. MWA is also lightweight, increasing model
size by only 2-3% (in terms of parameters) for state-of-the-art foundation
models like BEiT-3 Large. These results demonstrate that MWA provides an
efficient and effective adaptation method for MLLMs, significantly broadening
their applicability.
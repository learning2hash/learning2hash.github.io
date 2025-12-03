---
layout: publication
title: 'WAVER: Writing-style Agnostic Text-video Retrieval Via Distilling Vision-language
  Models Through Open-vocabulary Knowledge'
authors: Huy Le, Tung Kieu, Anh Nguyen, Ngan Le
conference: ICASSP 2024 - 2024 IEEE International Conference on Acoustics, Speech
  and Signal Processing (ICASSP)
year: 2023
bibkey: le2023waver
citations: 2
additional_links: [{name: Code, url: 'https://github.com/Fsoft-AIC/WAVER'}, {name: Paper,
    url: 'https://arxiv.org/abs/2312.09507'}]
tags: ["Datasets", "Evaluation", "ICASSP", "Tools & Libraries", "Video Retrieval"]
short_authors: Le et al.
---
Text-video retrieval, a prominent sub-field within the domain of multimodal
information retrieval, has witnessed remarkable growth in recent years.
However, existing methods assume video scenes are consistent with unbiased
descriptions. These limitations fail to align with real-world scenarios since
descriptions can be influenced by annotator biases, diverse writing styles, and
varying textual perspectives. To overcome the aforementioned problems, we
introduce \(\texttt\{WAVER\}\), a cross-domain knowledge distillation framework via
vision-language models through open-vocabulary knowledge designed to tackle the
challenge of handling different writing styles in video descriptions.
\(\texttt\{WAVER\}\) capitalizes on the open-vocabulary properties that lie in
pre-trained vision-language models and employs an implicit knowledge
distillation approach to transfer text-based knowledge from a teacher model to
a vision-based student. Empirical studies conducted across four standard
benchmark datasets, encompassing various settings, provide compelling evidence
that \(\texttt\{WAVER\}\) can achieve state-of-the-art performance in text-video
retrieval task while handling writing-style variations. The code is available
at: https://github.com/Fsoft-AIC/WAVER
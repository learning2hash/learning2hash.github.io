---
layout: publication
title: 'Contra: (con)text (tra)nsformer For Cross-modal Video Retrieval'
authors: Adriano Fragomeni, Michael Wray, Dima Damen
conference: Arxiv
year: 2022
bibkey: fragomeni2022contra
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2210.04341'}]
tags: ["Datasets", "Distance Metric Learning", "Evaluation", "Supervised", "Video Retrieval"]
short_authors: Adriano Fragomeni, Michael Wray, Dima Damen
---
In this paper, we re-examine the task of cross-modal clip-sentence retrieval,
where the clip is part of a longer untrimmed video. When the clip is short or
visually ambiguous, knowledge of its local temporal context (i.e. surrounding
video segments) can be used to improve the retrieval performance. We propose
Context Transformer (ConTra); an encoder architecture that models the
interaction between a video clip and its local temporal context in order to
enhance its embedded representations. Importantly, we supervise the context
transformer using contrastive losses in the cross-modal embedding space. We
explore context transformers for video and text modalities. Results
consistently demonstrate improved performance on three datasets: YouCook2,
EPIC-KITCHENS and a clip-sentence version of ActivityNet Captions. Exhaustive
ablation studies and context analysis show the efficacy of the proposed method.
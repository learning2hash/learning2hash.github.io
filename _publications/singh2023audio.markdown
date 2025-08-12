---
layout: publication
title: 'Audio Retrieval For Multimodal Design Documents: A New Dataset And Algorithms'
authors: Prachi Singh, Srikrishna Karanam, Sumit Shekhar
conference: Arxiv
year: 2023
bibkey: singh2023audio
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2302.14757'}]
tags: ["Audio Retrieval", "Datasets"]
short_authors: Prachi Singh, Srikrishna Karanam, Sumit Shekhar
---
We consider and propose a new problem of retrieving audio files relevant to
multimodal design document inputs comprising both textual elements and visual
imagery, e.g., birthday/greeting cards. In addition to enhancing user
experience, integrating audio that matches the theme/style of these inputs also
helps improve the accessibility of these documents (e.g., visually impaired
people can listen to the audio instead). While recent work in audio retrieval
exists, these methods and datasets are targeted explicitly towards natural
images. However, our problem considers multimodal design documents (created by
users using creative software) substantially different from a naturally clicked
photograph. To this end, our first contribution is collecting and curating a
new large-scale dataset called Melodic-Design (or MELON), comprising design
documents representing various styles, themes, templates, illustrations, etc.,
paired with music audio. Given our paired image-text-audio dataset, our next
contribution is a novel multimodal cross-attention audio retrieval (MMCAR)
algorithm that enables training neural networks to learn a common shared
feature space across image, text, and audio dimensions. We use these learned
features to demonstrate that our method outperforms existing state-of-the-art
methods and produce a new reference benchmark for the research community on our
new dataset.
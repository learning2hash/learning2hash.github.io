---
layout: publication
title: 'Towards Cross-modal Retrieval In Chinese Cultural Heritage Documents: Dataset
  And Solution'
authors: Junyi Yuan, Jian Zhang, Fangyu Wu, Dongming Lu, Huanda Lu, Qiufeng Wang
conference: Lecture Notes in Computer Science
year: 2025
bibkey: yuan2025towards
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2505.10921'}]
tags: ["Datasets", "Multimodal Retrieval"]
short_authors: Yuan et al.
---
China has a long and rich history, encompassing a vast cultural heritage that includes diverse multimodal information, such as silk patterns, Dunhuang murals, and their associated historical narratives. Cross-modal retrieval plays a pivotal role in understanding and interpreting Chinese cultural heritage by bridging visual and textual modalities to enable accurate text-to-image and image-to-text retrieval. However, despite the growing interest in multimodal research, there is a lack of specialized datasets dedicated to Chinese cultural heritage, limiting the development and evaluation of cross-modal learning models in this domain. To address this gap, we propose a multimodal dataset named CulTi, which contains 5,726 image-text pairs extracted from two series of professional documents, respectively related to ancient Chinese silk and Dunhuang murals. Compared to existing general-domain multimodal datasets, CulTi presents a challenge for cross-modal retrieval: the difficulty of local alignment between intricate decorative motifs and specialized textual descriptions. To address this challenge, we propose LACLIP, a training-free local alignment strategy built upon a fine-tuned Chinese-CLIP. LACLIP enhances the alignment of global textual descriptions with local visual regions by computing weighted similarity scores during inference. Experimental results on CulTi demonstrate that LACLIP significantly outperforms existing models in cross-modal retrieval, particularly in handling fine-grained semantic associations within Chinese cultural heritage.
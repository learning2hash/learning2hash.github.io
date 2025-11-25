---
layout: publication
title: 'Focus, Distinguish, And Prompt: Unleashing CLIP For Efficient And Flexible
  Scene Text Retrieval'
authors: Gangyan Zeng, Yuan Zhang, Jin Wei, Dongbao Yang, Peng Zhang, Yiwen Gao, Xugong
  Qin, Yu Zhou
conference: 'MM ''24: The 32nd ACM International Conference on Multimedia'
year: 2024
bibkey: zeng2024focus
citations: 4
additional_links: [{name: Code, url: 'https://github.com/Gyann-z/FDP'}, {name: Paper,
    url: 'https://arxiv.org/abs/2408.00441'}]
tags: ["Efficiency", "Image Retrieval", "Text Retrieval"]
short_authors: Zeng et al.
---
Scene text retrieval aims to find all images containing the query text from
an image gallery. Current efforts tend to adopt an Optical Character
Recognition (OCR) pipeline, which requires complicated text detection and/or
recognition processes, resulting in inefficient and inflexible retrieval.
Different from them, in this work we propose to explore the intrinsic potential
of Contrastive Language-Image Pre-training (CLIP) for OCR-free scene text
retrieval. Through empirical analysis, we observe that the main challenges of
CLIP as a text retriever are: 1) limited text perceptual scale, and 2)
entangled visual-semantic concepts. To this end, a novel model termed FDP
(Focus, Distinguish, and Prompt) is developed. FDP first focuses on scene text
via shifting the attention to the text area and probing the hidden text
knowledge, and then divides the query text into content word and function word
for processing, in which a semantic-aware prompting scheme and a distracted
queries assistance module are utilized. Extensive experiments show that FDP
significantly enhances the inference speed while achieving better or
competitive retrieval accuracy compared to existing methods. Notably, on the
IIIT-STR benchmark, FDP surpasses the state-of-the-art model by 4.37% with a 4
times faster speed. Furthermore, additional experiments under phrase-level and
attribute-aware scene text retrieval settings validate FDP's particular
advantages in handling diverse forms of query text. The source code will be
publicly available at https://github.com/Gyann-z/FDP.
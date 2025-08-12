---
layout: publication
title: Hateful Memes Detection Via Complementary Visual And Linguistic Networks
authors: Weibo Zhang, Guihua Liu, Zhuohua Li, Fuqing Zhu
conference: Arxiv
year: 2020
bibkey: zhang2020hateful
citations: 14
additional_links: [{name: Code, url: 'https://github.com/webYFDT/hateful'}, {name: Paper,
    url: 'https://arxiv.org/abs/2012.04977'}]
tags: ["Datasets", "Evaluation"]
short_authors: Zhang et al.
---
Hateful memes are widespread in social media and convey negative information.
The main challenge of hateful memes detection is that the expressive meaning
can not be well recognized by a single modality. In order to further integrate
modal information, we investigate a candidate solution based on complementary
visual and linguistic network in Hateful Memes Challenge 2020. In this way,
more comprehensive information of the multi-modality could be explored in
detail. Both contextual-level and sensitive object-level information are
considered in visual and linguistic embedding to formulate the complex
multi-modal scenarios. Specifically, a pre-trained classifier and object
detector are utilized to obtain the contextual features and region-of-interests
(RoIs) from the input, followed by the position representation fusion for
visual embedding. While linguistic embedding is composed of three components,
i.e., the sentence words embedding, position embedding and the corresponding
Spacy embedding (Sembedding), which is a symbol represented by vocabulary
extracted by Spacy. Both visual and linguistic embedding are fed into the
designed Complementary Visual and Linguistic (CVL) networks to produce the
prediction for hateful memes. Experimental results on Hateful Memes Challenge
Dataset demonstrate that CVL provides a decent performance, and produces 78:48%
and 72:95% on the criteria of AUROC and Accuracy. Code is available at
https://github.com/webYFDT/hateful.
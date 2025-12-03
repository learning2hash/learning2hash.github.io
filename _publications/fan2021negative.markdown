---
layout: publication
title: 'Negative Sample Is Negative In Its Own Way: Tailoring Negative Sentences For
  Image-text Retrieval'
authors: Zhihao Fan, Zhongyu Wei, Zejun Li, Siyuan Wang, Jianqing Fan
conference: Arxiv
year: 2021
bibkey: fan2021negative
citations: 1
additional_links: [{name: Code, url: 'https://github.com/LibertFan/TAGS'}, {name: Paper,
    url: 'https://arxiv.org/abs/2111.03349'}]
tags: ["Datasets", "Distance Metric Learning", "Robustness", "Text Retrieval", "Tools & Libraries"]
short_authors: Fan et al.
---
Matching model is essential for Image-Text Retrieval framework. Existing
research usually train the model with a triplet loss and explore various
strategy to retrieve hard negative sentences in the dataset. We argue that
current retrieval-based negative sample construction approach is limited in the
scale of the dataset thus fail to identify negative sample of high difficulty
for every image. We propose our TAiloring neGative Sentences with
Discrimination and Correction (TAGS-DC) to generate synthetic sentences
automatically as negative samples. TAGS-DC is composed of masking and refilling
to generate synthetic negative sentences with higher difficulty. To keep the
difficulty during training, we mutually improve the retrieval and generation
through parameter sharing. To further utilize fine-grained semantic of mismatch
in the negative sentence, we propose two auxiliary tasks, namely word
discrimination and word correction to improve the training. In experiments, we
verify the effectiveness of our model on MS-COCO and Flickr30K compared with
current state-of-the-art models and demonstrates its robustness and
faithfulness in the further analysis. Our code is available in
https://github.com/LibertFan/TAGS.
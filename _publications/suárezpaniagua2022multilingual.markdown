---
layout: publication
title: Multilingual News Location Detection Using An Entity-based Siamese Network
  With Semi-supervised Contrastive Learning And Knowledge Base
authors: "V\xEDctor Su\xE1rez-Paniagua, Steven Derby, Tri Kurniawan Wijaya"
conference: Arxiv
year: 2022
bibkey: "su\xE1rezpaniagua2022multilingual"
citations: 0
additional_links: [{name: Code, url: 'https://github.com/vsuarezpaniagua/NewsLocation'},
  {name: Paper, url: 'https://arxiv.org/abs/2212.11856'}]
tags: []
short_authors: "V\xEDctor Su\xE1rez-Paniagua, Steven Derby, Tri Kurniawan Wijaya"
---
Early detection of relevant locations in a piece of news is especially
important in extreme events such as environmental disasters, war conflicts,
disease outbreaks, or political turmoils. Additionally, this detection also
helps recommender systems to promote relevant news based on user locations.
Note that, when the relevant locations are not mentioned explicitly in the
text, state-of-the-art methods typically fail to recognize them because these
methods rely on syntactic recognition. In contrast, by incorporating a
knowledge base and connecting entities with their locations, our system
successfully infers the relevant locations even when they are not mentioned
explicitly in the text. To evaluate the effectiveness of our approach, and due
to the lack of datasets in this area, we also contribute to the research
community with a gold-standard multilingual news-location dataset, NewsLOC. It
contains the annotation of the relevant locations (and their WikiData IDs) of
600+ Wikinews articles in five different languages: English, French, German,
Italian, and Spanish. Through experimental evaluations, we show that our
proposed system outperforms the baselines and the fine-tuned version of the
model using semi-supervised data that increases the classification rate. The
source code and the NewsLOC dataset are publicly available for being used by
the research community at https://github.com/vsuarezpaniagua/NewsLocation.
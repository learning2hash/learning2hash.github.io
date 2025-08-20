---
layout: publication
title: 'Contrastive Multi-view Textual-visual Encoding: Towards One Hundred Thousand-scale
  One-shot Logo Identification'
authors: Nakul Sharma, Abhirama S. Penamakuri, Anand Mishra
conference: Proceedings of the Thirteenth Indian Conference on Computer Vision, Graphics
  and Image Processing
year: 2022
bibkey: sharma2022contrastive
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2211.12926'}]
tags: [Tools & Libraries, Datasets, Scalability]
short_authors: Nakul Sharma, Abhirama S. Penamakuri, Anand Mishra
---
In this paper, we study the problem of identifying logos of business brands
in natural scenes in an open-set one-shot setting. This problem setup is
significantly more challenging than traditionally-studied 'closed-set' and
'large-scale training samples per category' logo recognition settings. We
propose a novel multi-view textual-visual encoding framework that encodes text
appearing in the logos as well as the graphical design of the logos to learn
robust contrastive representations. These representations are jointly learned
for multiple views of logos over a batch and thereby they generalize well to
unseen logos. We evaluate our proposed framework for cropped logo verification,
cropped logo identification, and end-to-end logo identification in natural
scene tasks; and compare it against state-of-the-art methods. Further, the
literature lacks a 'very-large-scale' collection of reference logo images that
can facilitate the study of one-hundred thousand-scale logo identification. To
fill this gap in the literature, we introduce Wikidata Reference Logo Dataset
(WiRLD), containing logos for 100K business brands harvested from Wikidata. Our
proposed framework that achieves an area under the ROC curve of 91.3% on the
QMUL-OpenLogo dataset for the verification task, outperforms state-of-the-art
methods by 9.1% and 2.6% on the one-shot logo identification task on the
Toplogos-10 and the FlickrLogos32 datasets, respectively. Further, we show that
our method is more stable compared to other baselines even when the number of
candidate logos is on a 100K scale.
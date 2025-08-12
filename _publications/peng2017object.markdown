---
layout: publication
title: Object-part Attention Model For Fine-grained Image Classification
authors: Yuxin Peng, Xiangteng He, Junjie Zhao
conference: IEEE Transactions on Image Processing
year: 2017
bibkey: peng2017object
citations: 369
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1704.01740'}]
tags: ["Supervised"]
short_authors: Yuxin Peng, Xiangteng He, Junjie Zhao
---
Fine-grained image classification is to recognize hundreds of subcategories
belonging to the same basic-level category, such as 200 subcategories belonging
to the bird, which is highly challenging due to large variance in the same
subcategory and small variance among different subcategories. Existing methods
generally first locate the objects or parts and then discriminate which
subcategory the image belongs to. However, they mainly have two limitations:
(1) Relying on object or part annotations which are heavily labor consuming.
(2) Ignoring the spatial relationships between the object and its parts as well
as among these parts, both of which are significantly helpful for finding
discriminative parts. Therefore, this paper proposes the object-part attention
model (OPAM) for weakly supervised fine-grained image classification, and the
main novelties are: (1) Object-part attention model integrates two level
attentions: object-level attention localizes objects of images, and part-level
attention selects discriminative parts of object. Both are jointly employed to
learn multi-view and multi-scale features to enhance their mutual promotions.
(2) Object-part spatial constraint model combines two spatial constraints:
object spatial constraint ensures selected parts highly representative, and
part spatial constraint eliminates redundancy and enhances discrimination of
selected parts. Both are jointly employed to exploit the subtle and local
differences for distinguishing the subcategories. Importantly, neither object
nor part annotations are used in our proposed approach, which avoids the heavy
labor consumption of labeling. Comparing with more than 10 state-of-the-art
methods on 4 widely-used datasets, our OPAM approach achieves the best
performance.
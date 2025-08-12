---
layout: publication
title: 'Atlas: A Dataset And Benchmark For E-commerce Clothing Product Categorization'
authors: Venkatesh Umaashankar, Girish Shanmugam S, Aditi Prakash
conference: Arxiv
year: 2019
bibkey: umaashankar2019atlas
citations: 9
additional_links: [{name: Code, url: 'https://github.com/vumaasha/atlas'}, {name: Paper,
    url: 'https://arxiv.org/abs/1908.08984'}]
tags: ["Datasets", "Evaluation"]
short_authors: Venkatesh Umaashankar, Girish Shanmugam S, Aditi Prakash
---
In E-commerce, it is a common practice to organize the product catalog using
product taxonomy. This enables the buyer to easily locate the item they are
looking for and also to explore various items available under a category.
Product taxonomy is a tree structure with 3 or more levels of depth and several
leaf nodes. Product categorization is a large scale classification task that
assigns a category path to a particular product. Research in this area is
restricted by the unavailability of good real-world datasets and the variations
in taxonomy due to the absence of a standard across the different e-commerce
stores. In this paper, we introduce a high-quality product taxonomy dataset
focusing on clothing products which contain 186,150 images under clothing
category with 3 levels and 52 leaf nodes in the taxonomy. We explain the
methodology used to collect and label this dataset. Further, we establish the
benchmark by comparing image classification and Attention based Sequence models
for predicting the category path. Our benchmark model reaches a micro f-score
of 0.92 on the test set. The dataset, code and pre-trained models are publicly
available at https://github.com/vumaasha/atlas. We invite the community
to improve upon these baselines.
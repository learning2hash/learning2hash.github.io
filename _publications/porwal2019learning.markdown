---
layout: publication
title: Learning Image Information For Ecommerce Queries
authors: Utkarsh Porwal
conference: Proceedings of the 24th Australasian Document Computing Symposium
year: 2019
bibkey: porwal2019learning
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1904.12856'}]
tags: [Evaluation]
short_authors: Utkarsh Porwal
---
Computing similarity between a query and a document is fundamental in any
information retrieval system. In search engines, computing query-document
similarity is an essential step in both retrieval and ranking stages. In eBay
search, document is an item and the query-item similarity can be computed by
comparing different facets of the query-item pair. Query text can be compared
with the text of the item title. Likewise, a category constraint applied on the
query can be compared with the listing category of the item. However, images
are one signal that are usually present in the items but are not present in the
query. Images are one of the most intuitive signals used by users to determine
the relevance of the item given a query. Including this signal in estimating
similarity between the query-item pair is likely to improve the relevance of
the search engine. We propose a novel way of deriving image information for
queries. We attempt to learn image information for queries from item images
instead of generating explicit image features or an image for queries. We use
canonical correlation analysis (CCA) to learn a new subspace where projecting
the original data will give us a new query and item representation. We
hypothesize that this new query representation will also have image information
about the query. We estimate the query-item similarity using a vector space
model and report the performance of the proposed method on eBay's search data.
We show 11.89% relevance improvement over the baseline using area under the
receiver operating characteristic curve (AUROC) as the evaluation metric. We
also show 3.1% relevance improvement over the baseline with area under the
precision recall curve (AUPRC) .
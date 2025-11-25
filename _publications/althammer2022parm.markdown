---
layout: publication
title: 'PARM: A Paragraph Aggregation Retrieval Model For Dense Document-to-document
  Retrieval'
authors: "Sophia Althammer, Sebastian Hofst\xE4tter, Mete Sertkan, Suzan Verberne,\
  \ Allan Hanbury"
conference: Lecture Notes in Computer Science
year: 2022
bibkey: althammer2022parm
citations: 32
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2201.01614'}]
tags: ["Few Shot & Zero Shot", "Large Scale Search", "Text Retrieval"]
short_authors: Althammer et al.
---
Dense passage retrieval (DPR) models show great effectiveness gains in first
stage retrieval for the web domain. However in the web domain we are in a
setting with large amounts of training data and a query-to-passage or a
query-to-document retrieval task. We investigate in this paper dense
document-to-document retrieval with limited labelled target data for training,
in particular legal case retrieval. In order to use DPR models for
document-to-document retrieval, we propose a Paragraph Aggregation Retrieval
Model (PARM) which liberates DPR models from their limited input length. PARM
retrieves documents on the paragraph-level: for each query paragraph, relevant
documents are retrieved based on their paragraphs. Then the relevant results
per query paragraph are aggregated into one ranked list for the whole query
document. For the aggregation we propose vector-based aggregation with
reciprocal rank fusion (VRRF) weighting, which combines the advantages of
rank-based aggregation and topical aggregation based on the dense embeddings.
Experimental results show that VRRF outperforms rank-based aggregation
strategies for dense document-to-document retrieval with PARM. We compare PARM
to document-level retrieval and demonstrate higher retrieval effectiveness of
PARM for lexical and dense first-stage retrieval on two different legal case
retrieval collections. We investigate how to train the dense retrieval model
for PARM on limited target data with labels on the paragraph or the
document-level. In addition, we analyze the differences of the retrieved
results of lexical and dense retrieval with PARM.
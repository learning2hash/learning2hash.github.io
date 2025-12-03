---
layout: publication
title: Utilizing Embeddings For Ad-hoc Retrieval By Document-to-document Similarity
authors: Chenhao Yang, Ben He, Yanhua Ran
conference: Arxiv
year: 2017
bibkey: yang2017utilizing
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1708.03181'}]
tags: ["Uncategorized"]
short_authors: Chenhao Yang, Ben He, Yanhua Ran
---
Latent semantic representations of words or paragraphs, namely the
embeddings, have been widely applied to information retrieval (IR). One of the
common approaches of utilizing embeddings for IR is to estimate the
document-to-query (D2Q) similarity in their embeddings. As words with similar
syntactic usage are usually very close to each other in the embeddings space,
although they are not semantically similar, the D2Q similarity approach may
suffer from the problem of "multiple degrees of similarity". To this end, this
paper proposes a novel approach that estimates a semantic relevance score (SEM)
based on document-to-document (D2D) similarity of embeddings. As Word or
Para2Vec generates embeddings by the context of words/paragraphs, the D2D
similarity approach turns the task of document ranking into the estimation of
similarity between content within different documents. Experimental results on
standard TREC test collections show that our proposed approach outperforms
strong baselines.
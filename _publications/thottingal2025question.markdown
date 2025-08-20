---
layout: publication
title: 'Question-to-question Retrieval For Hallucination-free Knowledge Access: An
  Approach For Wikipedia And Wikidata Question Answering'
authors: Santhosh Thottingal
conference: Arxiv
year: 2025
bibkey: thottingal2025question
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2501.11301'}]
tags: [Distance Metric Learning, Efficiency, Scalability]
short_authors: Santhosh Thottingal
---
This paper introduces an approach to question answering over knowledge bases
like Wikipedia and Wikidata by performing "question-to-question" matching and
retrieval from a dense vector embedding store. Instead of embedding document
content, we generate a comprehensive set of questions for each logical content
unit using an instruction-tuned LLM. These questions are vector-embedded and
stored, mapping to the corresponding content. Vector embedding of user queries
are then matched against this question vector store. The highest similarity
score leads to direct retrieval of the associated article content, eliminating
the need for answer generation. Our method achieves high cosine similarity ( >
0.9 ) for relevant question pairs, enabling highly precise retrieval. This
approach offers several advantages including computational efficiency, rapid
response times, and increased scalability. We demonstrate its effectiveness on
Wikipedia and Wikidata, including multimedia content through structured fact
retrieval from Wikidata, opening up new pathways for multimodal question
answering.
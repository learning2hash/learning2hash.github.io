---
layout: publication
title: Generative Recommendation Towards Next-generation Recommender Paradigm
authors: Wenjie Wang, Xinyu Lin, Fuli Feng, Xiangnan He, Tat-seng Chua
conference: "Arxiv"
year: 2023
bibkey: wang2023generative
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2304.03516v2"}
tags: ['ARXIV', 'Text Retrieval']
---
Recommender systems typically retrieve items from an item corpus for personalized recommendations. However such a retrieval-based recommender paradigm faces two limitations 1) the human-generated items in the corpus might fail to satisfy the users diverse information needs and 2) users usually adjust the recommendations via inefficient passive feedback e.g. clicks. Nowadays AI-Generated Content (AIGC) has revealed significant success offering the potential to overcome these limitations 1) generative AI can produce personalized items to satisfy users information needs and 2) the newly emerged large language models significantly reduce the efforts of users to precisely express information needs via natural language instructions. In this light the boom of AIGC points the way towards the next-generation recommender paradigm with two new objectives 1) generating personalized content through generative AI and 2) integrating user instructions to guide content generation. To this end we propose a novel Generative Recommender paradigm named GeneRec which adopts an AI generator to personalize content generation and leverages user instructions. Specifically we pre-process users instructions and traditional feedback via an instructor to output the generation guidance. Given the guidance we instantiate the AI generator through an AI editor and an AI creator to repurpose existing items and create new items. Eventually GeneRec can perform content retrieval repurposing and creation to satisfy users information needs. Besides to ensure the trustworthiness of the generated items we emphasize various fidelity checks. Moreover we provide a roadmap to envision future developments of GeneRec and several domain-specific applications of GeneRec with potential research tasks. Lastly we study the feasibility of implementing AI editor and AI creator on micro-video generation.

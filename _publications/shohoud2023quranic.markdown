---
layout: publication
title: 'Quranic Conversations: Developing A Semantic Search Tool For The Quran Using
  Arabic NLP Techniques'
authors: Shohoud Yasser, Shoman Maged, Abdelazim Sarah
conference: Arxiv
year: 2023
bibkey: shohoud2023quranic
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2311.05120'}]
tags: ["Similarity Search", "Text Retrieval", "Tools & Libraries"]
short_authors: Shohoud Yasser, Shoman Maged, Abdelazim Sarah
---
The Holy Book of Quran is believed to be the literal word of God (Allah) as
revealed to the Prophet Muhammad (PBUH) over a period of approximately 23
years. It is the book where God provides guidance on how to live a righteous
and just life, emphasizing principles like honesty, compassion, charity and
justice, as well as providing rules for personal conduct, family matters,
business ethics and much more. However, due to constraints related to the
language and the Quran organization, it is challenging for Muslims to get all
relevant ayahs (verses) pertaining to a matter or inquiry of interest. Hence,
we developed a Quran semantic search tool which finds the verses pertaining to
the user inquiry or prompt. To achieve this, we trained several models on a
large dataset of over 30 tafsirs, where typically each tafsir corresponds to
one verse in the Quran and, using cosine similarity, obtained the tafsir tensor
which is most similar to the prompt tensor of interest, which was then used to
index for the corresponding ayah in the Quran. Using the SNxLM model, we were
able to achieve a cosine similarity score as high as 0.97 which corresponds to
the abdu tafsir for a verse relating to financial matters.
---
layout: publication
title: 'Character 3-gram Mover''s Distance: An Effective Method For Detecting Near-duplicate
  Japanese-language Recipes'
authors: Masaki Oguni, Yohei Seki, Yu Hirate
conference: Arxiv
year: 2019
bibkey: oguni2019character
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1912.05171'}]
tags: ["Evaluation", "Similarity Search"]
short_authors: Masaki Oguni, Yohei Seki, Yu Hirate
---
In user-generated recipe websites, users post their-original recipes. Some
recipes, however, are very similar in major components such as the cooking
instructions to other recipes. We refer to such recipes as "near-duplicate
recipes". In this study, we propose a method that extends the "Word Mover's
Distance", which calculates distances between texts based on word embedding, to
character 3-gram embedding. Using a corpus of over 1.21 million recipes, we
learned the word embedding and the character 3-gram embedding by using a
Skip-Gram model with negative sampling and fastText to extract candidate pairs
of near-duplicate recipes. We then annotated these candidates and evaluated the
proposed method against a comparison method. Our results demonstrated that
near-duplicate recipes that were not detected by the comparison method were
successfully detected by the proposed method.
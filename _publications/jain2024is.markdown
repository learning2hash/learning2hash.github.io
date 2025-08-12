---
layout: publication
title: 'Is AI Fun? Humordb: A Curated Dataset And Benchmark To Investigate Graphical
  Humor'
authors: Veedant Jain, Felipe Dos Santos Alves Feitosa, Gabriel Kreiman
conference: Arxiv
year: 2024
bibkey: jain2024is
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2406.13564'}]
tags: ["Datasets", "Evaluation"]
short_authors: Veedant Jain, Felipe Dos Santos Alves Feitosa, Gabriel Kreiman
---
Despite significant advancements in computer vision, understanding complex
scenes, particularly those involving humor, remains a substantial challenge.
This paper introduces HumorDB, a novel image-only dataset specifically designed
to advance visual humor understanding. HumorDB consists of meticulously curated
image pairs with contrasting humor ratings, emphasizing subtle visual cues that
trigger humor and mitigating potential biases. The dataset enables evaluation
through binary classification(Funny or Not Funny), range regression(funniness
on a scale from 1 to 10), and pairwise comparison tasks(Which Image is
Funnier?), effectively capturing the subjective nature of humor perception.
Initial experiments reveal that while vision-only models struggle,
vision-language models, particularly those leveraging large language models,
show promising results. HumorDB also shows potential as a valuable zero-shot
benchmark for powerful large multimodal models. We open-source both the dataset
and code under the CC BY 4.0 license.
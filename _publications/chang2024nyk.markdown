---
layout: publication
title: 'NYK-MS: A Well-annotated Multi-modal Metaphor And Sarcasm Understanding Benchmark
  On Cartoon-caption Dataset'
authors: Ke Chang, Hao Li, Junzhao Zhang, Yunfang Wu
conference: Arxiv
year: 2024
bibkey: chang2024nyk
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2409.01037'}]
tags: ["Datasets", "Evaluation"]
short_authors: Chang et al.
---
Metaphor and sarcasm are common figurative expressions in people's
communication, especially on the Internet or the memes popular among teenagers.
We create a new benchmark named NYK-MS (NewYorKer for Metaphor and Sarcasm),
which contains 1,583 samples for metaphor understanding tasks and 1,578 samples
for sarcasm understanding tasks. These tasks include whether it contains
metaphor/sarcasm, which word or object contains metaphor/sarcasm, what does it
satirize and why does it contains metaphor/sarcasm, all of the 7 tasks are
well-annotated by at least 3 annotators. We annotate the dataset for several
rounds to improve the consistency and quality, and use GUI and GPT-4V to raise
our efficiency. Based on the benchmark, we conduct plenty of experiments. In
the zero-shot experiments, we show that Large Language Models (LLM) and Large
Multi-modal Models (LMM) can't do classification task well, and as the scale
increases, the performance on other 5 tasks improves. In the experiments on
traditional pre-train models, we show the enhancement with augment and
alignment methods, which prove our benchmark is consistent with previous
dataset and requires the model to understand both of the two modalities.
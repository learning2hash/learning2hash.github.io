---
layout: publication
title: 'MERMAID: Metaphor Generation With Symbolism And Discriminative Decoding'
authors: Tuhin Chakrabarty, Xurui Zhang, Smaranda Muresan, Nanyun Peng
conference: 'Proceedings of the 2021 Conference of the North American Chapter of the
  Association for Computational Linguistics: Human Language Technologies'
year: 2021
bibkey: chakrabarty2021mermaid
citations: 46
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2103.06779'}]
tags: ["Evaluation", "NAACL"]
short_authors: Chakrabarty et al.
---
Generating metaphors is a challenging task as it requires a proper
understanding of abstract concepts, making connections between unrelated
concepts, and deviating from the literal meaning. In this paper, we aim to
generate a metaphoric sentence given a literal expression by replacing relevant
verbs. Based on a theoretically-grounded connection between metaphors and
symbols, we propose a method to automatically construct a parallel corpus by
transforming a large number of metaphorical sentences from the Gutenberg Poetry
corpus (Jacobs, 2018) to their literal counterpart using recent advances in
masked language modeling coupled with commonsense inference. For the generation
task, we incorporate a metaphor discriminator to guide the decoding of a
sequence to sequence model fine-tuned on our parallel data to generate
high-quality metaphors. Human evaluation on an independent test set of literal
statements shows that our best model generates metaphors better than three
well-crafted baselines 66% of the time on average. A task-based evaluation
shows that human-written poems enhanced with metaphors proposed by our model
are preferred 68% of the time compared to poems without metaphors.
---
layout: publication
title: 'Svgeditbench: A Benchmark Dataset For Quantitative Assessment Of Llm''s SVG
  Editing Capabilities'
authors: Kunato Nishina, Yusuke Matsui
conference: Arxiv
year: 2024
bibkey: nishina2024svgeditbench
citations: 0
additional_links: [{name: Code, url: 'https://github.com/mti-lab/SVGEditBench'}, {
    name: Paper, url: 'https://arxiv.org/abs/2404.13710'}]
tags: ["Datasets", "Evaluation"]
short_authors: Kunato Nishina, Yusuke Matsui
---
Text-to-image models have shown progress in recent years. Along with this
progress, generating vector graphics from text has also advanced. SVG is a
popular format for vector graphics, and SVG represents a scene with XML text.
Therefore, Large Language Models can directly process SVG code. Taking this
into account, we focused on editing SVG with LLMs. For quantitative evaluation
of LLMs' ability to edit SVG, we propose SVGEditBench. SVGEditBench is a
benchmark for assessing the LLMs' ability to edit SVG code. We also show the
GPT-4 and GPT-3.5 results when evaluated on the proposed benchmark. In the
experiments, GPT-4 showed superior performance to GPT-3.5 both quantitatively
and qualitatively. The dataset is available at
https://github.com/mti-lab/SVGEditBench.
---
layout: publication
title: Language Model Cascades
authors: David Dohan, Winnie Xu, Aitor Lewkowycz, Jacob Austin, David Bieber, Raphael Gontijo Lopes, Yuhuai Wu, Henryk Michalewski, Rif A. Saurous, Jascha Sohl-dickstein, Kevin Murphy, Charles Sutton
conference: "Arxiv"
year: 2022
bibkey: dohan2022language
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2207.10342v2"}
tags: ['ARXIV', 'Graph', 'Independent']
---
Prompted models have demonstrated impressive few-shot learning abilities. Repeated interactions at test-time with a single model or the composition of multiple models together further expands capabilities. These compositions are probabilistic models and may be expressed in the language of graphical models with random variables whose values are complex data types such as strings. Cases with control flow and dynamic structure require techniques from probabilistic programming which allow implementing disparate model structures and inference strategies in a unified language. We formalize several existing techniques from this perspective including scratchpads / chain of thought verifiers STaR selection-inference and tool use. We refer to the resulting programs as language model cascades.

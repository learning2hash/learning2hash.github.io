---
layout: publication
title: Webgpt Browser-assisted Question-answering With Human Feedback
authors: Reiichiro Nakano, Jacob Hilton, Suchir Balaji, Jeff Wu, Long Ouyang, Christina Kim, Christopher Hesse, Shantanu Jain, Vineet Kosaraju, William Saunders, Xu Jiang, Karl Cobbe, Tyna Eloundou, Gretchen Krueger, Kevin Button, Matthew Knight, Benjamin Chess, John Schulman
conference: "Arxiv"
year: 2021
bibkey: nakano2021webgpt
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2112.09332v3"}
tags: ['ARXIV']
---
We fine-tune GPT-3 to answer long-form questions using a text-based web-browsing environment which allows the model to search and navigate the web. By setting up the task so that it can be performed by humans we are able to train models on the task using imitation learning and then optimize answer quality with human feedback. To make human evaluation of factual accuracy easier models must collect references while browsing in support of their answers. We train and evaluate our models on ELI5 a dataset of questions asked by Reddit users. Our best model is obtained by fine-tuning GPT-3 using behavior cloning and then performing rejection sampling against a reward model trained to predict human preferences. This models answers are preferred by humans 5637; of the time to those of our human demonstrators and 6937; of the time to the highest-voted answer from Reddit.

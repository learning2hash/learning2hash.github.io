---
layout: publication
title: Do Llms Understand User Preferences Evaluating Llms On User Rating Prediction
authors: Wang-cheng Kang, Jianmo Ni, Nikhil Mehta, Maheswaran Sathiamoorthy, Lichan Hong, Ed Chi, Derek Zhiyuan Cheng
conference: "Arxiv"
year: 2023
bibkey: kang2023do
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2305.06474v1"}
tags: ['ARXIV', 'Supervised']
---
Large Language Models (LLMs) have demonstrated exceptional capabilities in generalizing to new tasks in a zero-shot or few-shot manner. However the extent to which LLMs can comprehend user preferences based on their previous behavior remains an emerging and still unclear research question. Traditionally Collaborative Filtering (CF) has been the most effective method for these tasks predominantly relying on the extensive volume of rating data. In contrast LLMs typically demand considerably less data while maintaining an exhaustive world knowledge about each item such as movies or products. In this paper we conduct a thorough examination of both CF and LLMs within the classic task of user rating prediction which involves predicting a users rating for a candidate item based on their past ratings. We investigate various LLMs in different sizes ranging from 250M to 540B parameters and evaluate their performance in zero-shot few-shot and fine-tuning scenarios. We conduct comprehensive analysis to compare between LLMs and strong CF methods and find that zero-shot LLMs lag behind traditional recommender models that have the access to user interaction data indicating the importance of user interaction data. However through fine-tuning LLMs achieve comparable or even better performance with only a small fraction of the training data demonstrating their potential through data efficiency.

---
layout: publication
title: 'Banglishrev: A Large-scale Bangla-english And Code-mixed Dataset Of Product
  Reviews In E-commerce'
authors: Mohammad Nazmush Shamael, Sabila Nawshin, Swakkhar Shatabda, Salekul Islam
conference: Arxiv
year: 2024
bibkey: shamael2024banglishrev
citations: 0
additional_links: [{name: Code, url: 'https://huggingface.co/datasets/BanglishRev/bangla-english-and-code-mixed-ecommerce-review-dataset'},
  {name: Paper, url: 'https://arxiv.org/abs/2412.13161'}]
tags: ["Datasets"]
short_authors: Shamael et al.
---
This work presents the BanglishRev Dataset, the largest e-commerce product
review dataset to date for reviews written in Bengali, English, a mixture of
both and Banglish, Bengali words written with English alphabets. The dataset
comprises of 1.74 million written reviews from 3.2 million ratings information
collected from a total of 128k products being sold in online e-commerce
platforms targeting the Bengali population. It includes an extensive array of
related metadata for each of the reviews including the rating given by the
reviewer, date the review was posted and date of purchase, number of likes,
dislikes, response from the seller, images associated with the review etc. With
sentiment analysis being the most prominent usage of review datasets,
experimentation with a binary sentiment analysis model with the review rating
serving as an indicator of positive or negative sentiment was conducted to
evaluate the effectiveness of the large amount of data presented in BanglishRev
for sentiment analysis tasks. A BanglishBERT model is trained on the data from
BanglishRev with reviews being considered labeled positive if the rating is
greater than 3 and negative if the rating is less than or equal to 3. The model
is evaluated by being testing against a previously published manually annotated
dataset for e-commerce reviews written in a mixture of Bangla, English and
Banglish. The experimental model achieved an exceptional accuracy of 94% and
F1 score of 0.94, demonstrating the dataset's efficacy for sentiment analysis.
Some of the intriguing patterns and observations seen within the dataset and
future research directions where the dataset can be utilized is also discussed
and explored. The dataset can be accessed through
https://huggingface.co/datasets/BanglishRev/bangla-english-and-code-mixed-ecommerce-review-dataset.
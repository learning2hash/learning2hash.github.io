---
layout: publication
title: 'Fashion DNA: Merging Content And Sales Data For Recommendation And Article
  Mapping'
authors: Christian Bracher, Sebastian Heinz, Roland Vollgraf
conference: Arxiv
year: 2016
bibkey: bracher2016fashion
citations: 36
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1609.02489'}]
tags: ["Recommender Systems"]
short_authors: Christian Bracher, Sebastian Heinz, Roland Vollgraf
---
We present a method to determine Fashion DNA, coordinate vectors locating
fashion items in an abstract space. Our approach is based on a deep neural
network architecture that ingests curated article information such as tags and
images, and is trained to predict sales for a large set of frequent customers.
In the process, a dual space of customer style preferences naturally arises.
Interpretation of the metric of these spaces is straightforward: The product of
Fashion DNA and customer style vectors yields the forecast purchase likelihood
for the customer-item pair, while the angle between Fashion DNA vectors is a
measure of item similarity. Importantly, our models are able to generate
unbiased purchase probabilities for fashion items based solely on article
information, even in absence of sales data, thus circumventing the "cold-start
problem" of collaborative recommendation approaches. Likewise, it generalizes
easily and reliably to customers outside the training set. We experiment with
Fashion DNA models based on visual and/or tag item data, evaluate their
recommendation power, and discuss the resulting article similarities.
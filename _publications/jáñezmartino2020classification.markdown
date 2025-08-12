---
layout: publication
title: Classification Of Spam Emails Through Hierarchical Clustering And Supervised
  Learning
authors: "Francisco J\xE1\xF1ez-Martino, Eduardo Fidalgo, Santiago Gonz\xE1lez-Mart\xED\
  nez, Javier Velasco-Mata"
conference: Arxiv
year: 2020
bibkey: "j\xE1\xF1ezmartino2020classification"
citations: 18
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2005.08773'}]
tags: ["Supervised"]
short_authors: "J\xE1\xF1ez-Martino et al."
---
Spammers take advantage of email popularity to send indiscriminately
unsolicited emails. Although researchers and organizations continuously develop
anti-spam filters based on binary classification, spammers bypass them through
new strategies, like word obfuscation or image-based spam. For the first time
in literature, we propose to classify spam email in categories to improve the
handle of already detected spam emails, instead of just using a binary model.
First, we applied a hierarchical clustering algorithm to create SPEMC-\(11\)K
(SPam EMail Classification), the first multi-class dataset, which contains
three types of spam emails: Health and Technology, Personal Scams, and Sexual
Content. Then, we used SPEMC-\(11\)K to evaluate the combination of TF-IDF and
BOW encodings with Na\"ive Bayes, Decision Trees and SVM classifiers. Finally,
we recommend for the task of multi-class spam classification the use of (i)
TF-IDF combined with SVM for the best micro F1 score performance, \(95.39%\),
and (ii) TD-IDF along with NB for the fastest spam classification, analyzing an
email in \(2.13\)ms.
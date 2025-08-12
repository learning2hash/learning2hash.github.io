---
layout: publication
title: Offensive Hebrew Corpus And Detection Using BERT
authors: Nagham Hamad, Mustafa Jarrar, Mohammad Khalilia, Nadim Nashif
conference: 2023 20th ACS/IEEE International Conference on Computer Systems and Applications
  (AICCSA)
year: 2023
bibkey: hamad2023offensive
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2309.02724'}]
tags: ["Datasets", "Evaluation"]
short_authors: Hamad et al.
---
Offensive language detection has been well studied in many languages, but it
is lagging behind in low-resource languages, such as Hebrew. In this paper, we
present a new offensive language corpus in Hebrew. A total of 15,881 tweets
were retrieved from Twitter. Each was labeled with one or more of five classes
(abusive, hate, violence, pornographic, or none offensive) by Arabic-Hebrew
bilingual speakers. The annotation process was challenging as each annotator is
expected to be familiar with the Israeli culture, politics, and practices to
understand the context of each tweet. We fine-tuned two Hebrew BERT models,
HeBERT and AlephBERT, using our proposed dataset and another published dataset.
We observed that our data boosts HeBERT performance by 2% when combined with
D_OLaH. Fine-tuning AlephBERT on our data and testing on D_OLaH yields 69%
accuracy, while fine-tuning on D_OLaH and testing on our data yields 57%
accuracy, which may be an indication to the generalizability our data offers.
Our dataset and fine-tuned models are available on GitHub and Huggingface.
---
layout: publication
title: Improving Word Recognition Using Multiple Hypotheses And Deep Embeddings
authors: Siddhant Bansal, Praveen Krishnan, C. V. Jawahar
conference: Arxiv
year: 2020
bibkey: bansal2020improving
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2010.14411'}]
tags: [Distance Metric Learning]
short_authors: Siddhant Bansal, Praveen Krishnan, C. V. Jawahar
---
We propose a novel scheme for improving the word recognition accuracy using
word image embeddings. We use a trained text recognizer, which can predict
multiple text hypothesis for a given word image. Our fusion scheme improves the
recognition process by utilizing the word image and text embeddings obtained
from a trained word image embedding network. We propose EmbedNet, which is
trained using a triplet loss for learning a suitable embedding space where the
embedding of the word image lies closer to the embedding of the corresponding
text transcription. The updated embedding space thus helps in choosing the
correct prediction with higher confidence. To further improve the accuracy, we
propose a plug-and-play module called Confidence based Accuracy Booster (CAB).
The CAB module takes in the confidence scores obtained from the text recognizer
and Euclidean distances between the embeddings to generate an updated distance
vector. The updated distance vector has lower distance values for the correct
words and higher distance values for the incorrect words. We rigorously
evaluate our proposed method systematically on a collection of books in the
Hindi language. Our method achieves an absolute improvement of around 10
percent in terms of word recognition accuracy.
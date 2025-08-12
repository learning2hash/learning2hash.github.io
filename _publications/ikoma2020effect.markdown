---
layout: publication
title: Effect Of Text Color On Word Embeddings
authors: Masaya Ikoma, Brian Kenji Iwana, Seiichi Uchida
conference: Lecture Notes in Computer Science
year: 2020
bibkey: ikoma2020effect
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2004.08526'}]
tags: []
short_authors: Masaya Ikoma, Brian Kenji Iwana, Seiichi Uchida
---
In natural scenes and documents, we can find the correlation between a text
and its color. For instance, the word, "hot", is often printed in red, while
"cold" is often in blue. This correlation can be thought of as a feature that
represents the semantic difference between the words. Based on this
observation, we propose the idea of using text color for word embeddings. While
text-only word embeddings (e.g. word2vec) have been extremely successful, they
often represent antonyms as similar since they are often interchangeable in
sentences. In this paper, we try two tasks to verify the usefulness of text
color in understanding the meanings of words, especially in identifying
synonyms and antonyms. First, we quantify the color distribution of words from
the book cover images and analyze the correlation between the color and meaning
of the word. Second, we try to retrain word embeddings with the color
distribution of words as a constraint. By observing the changes in the word
embeddings of synonyms and antonyms before and after re-training, we aim to
understand the kind of words that have positive or negative effects in their
word embeddings when incorporating text color information.
---
layout: publication
title: 'Wikipedia Vandal Early Detection: From User Behavior To User Embedding'
authors: Shuhan Yuan, Panpan Zheng, Xintao Wu, Yang Xiang
conference: Lecture Notes in Computer Science
year: 2017
bibkey: yuan2017wikipedia
citations: 14
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1706.00887'}]
tags: []
short_authors: Yuan et al.
---
Wikipedia is the largest online encyclopedia that allows anyone to edit
articles. In this paper, we propose the use of deep learning to detect vandals
based on their edit history. In particular, we develop a multi-source
long-short term memory network (M-LSTM) to model user behaviors by using a
variety of user edit aspects as inputs, including the history of edit reversion
information, edit page titles and categories. With M-LSTM, we can encode each
user into a low dimensional real vector, called user embedding. Meanwhile, as a
sequential model, M-LSTM updates the user embedding each time after the user
commits a new edit. Thus, we can predict whether a user is benign or vandal
dynamically based on the up-to-date user embedding. Furthermore, those user
embeddings are crucial to discover collaborative vandals.
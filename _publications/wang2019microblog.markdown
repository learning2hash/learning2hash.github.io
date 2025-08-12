---
layout: publication
title: Microblog Hashtag Generation Via Encoding Conversation Contexts
authors: Yue Wang, Jing Li, Irwin King, Michael R. Lyu, Shuming Shi
conference: Proceedings of the 2019 Conference of the North
year: 2019
bibkey: wang2019microblog
citations: 35
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1905.07584'}]
tags: []
short_authors: Wang et al.
---
Automatic hashtag annotation plays an important role in content understanding
for microblog posts. To date, progress made in this field has been restricted
to phrase selection from limited candidates, or word-level hashtag discovery
using topic models. Different from previous work considering hashtags to be
inseparable, our work is the first effort to annotate hashtags with a novel
sequence generation framework via viewing the hashtag as a short sequence of
words. Moreover, to address the data sparsity issue in processing short
microblog posts, we propose to jointly model the target posts and the
conversation contexts initiated by them with bidirectional attention. Extensive
experimental results on two large-scale datasets, newly collected from English
Twitter and Chinese Weibo, show that our model significantly outperforms
state-of-the-art models based on classification. Further studies demonstrate
our ability to effectively generate rare and even unseen hashtags, which is
however not possible for most existing methods.
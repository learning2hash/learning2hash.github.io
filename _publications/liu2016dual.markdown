---
layout: publication
title: Dual Purpose Hashing
authors: Haomiao Liu, Ruiping Wang, Shiguang Shan, Xilin Chen
conference: Arxiv
year: 2016
bibkey: liu2016dual
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1607.05529'}]
tags: ["Hashing Methods"]
short_authors: Liu et al.
---
Recent years have seen more and more demand for a unified framework to
address multiple realistic image retrieval tasks concerning both category and
attributes. Considering the scale of modern datasets, hashing is favorable for
its low complexity. However, most existing hashing methods are designed to
preserve one single kind of similarity, thus improper for dealing with the
different tasks simultaneously. To overcome this limitation, we propose a new
hashing method, named Dual Purpose Hashing (DPH), which jointly preserves the
category and attribute similarities by exploiting the Convolutional Neural
Network (CNN) models to hierarchically capture the correlations between
category and attributes. Since images with both category and attribute labels
are scarce, our method is designed to take the abundant partially labelled
images on the Internet as training inputs. With such a framework, the binary
codes of new-coming images can be readily obtained by quantizing the network
outputs of a binary-like layer, and the attributes can be recovered from the
codes easily. Experiments on two large-scale datasets show that our dual
purpose hash codes can achieve comparable or even better performance than those
state-of-the-art methods specifically designed for each individual retrieval
task, while being more compact than the compared methods.
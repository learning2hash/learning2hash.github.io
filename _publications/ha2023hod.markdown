---
layout: publication
title: 'HOD: A Benchmark Dataset For Harmful Object Detection'
authors: Eungyeom Ha, Heemook Kim, Sung Chul Hong, Dongbin Na
conference: Arxiv
year: 2023
bibkey: ha2023hod
citations: 0
additional_links: [{name: Code, url: 'https://github.com/poori-nuna/HOD-Benchmark-Dataset'},
  {name: Paper, url: 'https://arxiv.org/abs/2310.05192'}]
tags: ["Datasets", "Evaluation"]
short_authors: Ha et al.
---
Recent multi-media data such as images and videos have been rapidly spread
out on various online services such as social network services (SNS). With the
explosive growth of online media services, the number of image content that may
harm users is also growing exponentially. Thus, most recent online platforms
such as Facebook and Instagram have adopted content filtering systems to
prevent the prevalence of harmful content and reduce the possible risk of
adverse effects on users. Unfortunately, computer vision research on detecting
harmful content has not yet attracted attention enough. Users of each platform
still manually click the report button to recognize patterns of harmful content
they dislike when exposed to harmful content. However, the problem with manual
reporting is that users are already exposed to harmful content. To address
these issues, our research goal in this work is to develop automatic harmful
object detection systems for online services. We present a new benchmark
dataset for harmful object detection. Unlike most related studies focusing on a
small subset of object categories, our dataset addresses various categories.
Specifically, our proposed dataset contains more than 10,000 images across 6
categories that might be harmful, consisting of not only normal cases but also
hard cases that are difficult to detect. Moreover, we have conducted extensive
experiments to evaluate the effectiveness of our proposed dataset. We have
utilized the recently proposed state-of-the-art (SOTA) object detection
architectures and demonstrated our proposed dataset can be greatly useful for
the real-time harmful object detection task. The whole source codes and
datasets are publicly accessible at
https://github.com/poori-nuna/HOD-Benchmark-Dataset.
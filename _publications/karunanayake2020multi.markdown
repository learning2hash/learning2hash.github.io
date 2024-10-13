---
layout: publication
title: A Multi-modal Neural Embeddings Approach For Detecting Mobile Counterfeit Apps A Case Study On Google Play Store
authors: Karunanayake Naveen, Rajasegaran Jathushan, Gunathillake Ashanie, Seneviratne Suranga, Jourjon Guillaume
conference: "Arxiv"
year: 2020
bibkey: karunanayake2020multi
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2006.02231"}
tags: ['ARXIV', 'Case Study', 'Deep Learning']
---
Counterfeit apps impersonate existing popular apps in attempts to misguide
users to install them for various reasons such as collecting personal
information or spreading malware. Many counterfeits can be identified once
installed, however even a tech-savvy user may struggle to detect them before
installation. To this end, this paper proposes to leverage the recent advances
in deep learning methods to create image and text embeddings so that
counterfeit apps can be efficiently identified when they are submitted for
publication. We show that a novel approach of combining content embeddings and
style embeddings outperforms the baseline methods for image similarity such as
SIFT, SURF, and various image hashing methods. We first evaluate the
performance of the proposed method on two well-known datasets for evaluating
image similarity methods and show that content, style, and combined embeddings
increase precision@k and recall@k by 10%-15% and 12%-25%, respectively when
retrieving five nearest neighbours. Second, specifically for the app
counterfeit detection problem, combined content and style embeddings achieve
12% and 14% increase in precision@k and recall@k, respectively compared to the
baseline methods. Third, we present an analysis of approximately 1.2 million
apps from Google Play Store and identify a set of potential counterfeits for
top-10,000 popular apps. Under a conservative assumption, we were able to find
2,040 potential counterfeits that contain malware in a set of 49,608 apps that
showed high similarity to one of the top-10,000 popular apps in Google Play
Store. We also find 1,565 potential counterfeits asking for at least five
additional dangerous permissions than the original app and 1,407 potential
counterfeits having at least five extra third party advertisement libraries.

---
layout: publication
title: On-device Emoji Classifier Trained With Gpt-based Data Augmentation For A Mobile
  Keyboard
authors: Hossam Amer, Joe Osborne, Michael Zaki, Mohamed Afify
conference: Arxiv
year: 2024
bibkey: amer2024device
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2411.05031'}]
tags: ["Datasets", "Evaluation"]
short_authors: Amer et al.
---
Emojis improve communication quality among smart-phone users that use mobile
keyboards to exchange text. To predict emojis for users based on input text, we
should consider the on-device low memory and time constraints, ensure that the
on-device emoji classifier covers a wide range of emoji classes even though the
emoji dataset is typically imbalanced, and adapt the emoji classifier output to
user favorites. This paper proposes an on-device emoji classifier based on
MobileBert with reasonable memory and latency requirements for SwiftKey. To
account for the data imbalance, we utilize the widely used GPT to generate one
or more tags for each emoji class. For each emoji and corresponding tags, we
merge the original set with GPT-generated sentences and label them with this
emoji without human intervention to alleviate the data imbalance. At inference
time, we interpolate the emoji output with the user history for emojis for
better emoji classifications. Results show that the proposed on-device emoji
classifier deployed for SwiftKey increases the accuracy performance of emoji
prediction particularly on rare emojis and emoji engagement.
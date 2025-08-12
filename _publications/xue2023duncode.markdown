---
layout: publication
title: Duncode Characters Shorter
authors: Changshang Xue
conference: Arxiv
year: 2023
bibkey: xue2023duncode
citations: 0
additional_links: [{name: Code, url: 'https://github.com/laohur/duncode'}, {name: Code,
    url: 'https://github.com/laohur/wiki2txt'}, {name: Paper, url: 'https://arxiv.org/abs/2307.05414'}]
tags: ["Efficiency"]
short_authors: Changshang Xue
---
This paper investigates the employment of various encoders in text
transformation, converting characters into bytes. It discusses local encoders
such as ASCII and GB-2312, which encode specific characters into shorter bytes,
and universal encoders like UTF-8 and UTF-16, which can encode the complete
Unicode set with greater space requirements and are gaining widespread
acceptance. Other encoders, including SCSU, BOCU-1, and binary encoders,
however, lack self-synchronizing capabilities. Duncode is introduced as an
innovative encoding method that aims to encode the entire Unicode character set
with high space efficiency, akin to local encoders. It has the potential to
compress multiple characters of a string into a Duncode unit using fewer bytes.
Despite offering less self-synchronizing identification information, Duncode
surpasses UTF8 in terms of space efficiency. The application is available at
https://github.com/laohur/duncode. Additionally, we have developed a
benchmark for evaluating character encoders across different languages. It
encompasses 179 languages and can be accessed at
https://github.com/laohur/wiki2txt.
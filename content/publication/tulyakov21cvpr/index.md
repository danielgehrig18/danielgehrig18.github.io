---
title: "Time Lens: Event-based Video Frame Interpolation
"
authors:
- Stepan Tulyakov*
- Daniel Gehrig* 
- Stamatios Georgoulis
- Julius Erbach
- Mathias Gehrig
- Yuanyou Li 
- Davide Scaramuzza
author_notes:
- "Equal contribution"
- "Equal contribution"
#date: "2015-09-01T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2021-06-19T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["paper-conference"]

# Publication name and optional abbreviated publication name.
publication: "*IEEE Conference on Computer Vision and Pattern Recognition (CVPR)*"

publication_short: ""

abstract: "State-of-the-art frame interpolation methods generate intermediate frames by inferring object motions in the image from consecutive key-frames. In the absence of additional information, first-order approximations, i.e. optical flow, must be used, but this choice restricts the types of motions that can be modeled, leading to errors in highly dynamic scenarios. Event cameras are novel sensors that address this limitation by providing auxiliary visual information in the blind-time between frames. They asynchronously measure per-pixel brightness changes and do this with high temporal resolution and low latency. Event-based frame interpolation methods typically adopt a synthesis-based approach, where predicted frame residuals are directly applied to the key-frames. However, while these approaches can capture non-linear motions they suffer from ghosting and perform poorly in low-texture regions with few events. Thus, synthesis-based and flow-based approaches are complementary. In this work, we introduce Time Lens, a novel indicates equal contribution method that leverages the advantages of both. We extensively evaluate our method on three synthetic and two real benchmarks where we show an up to 5.21 dB improvement in terms of PSNR over state-of-the-art frame-based and event-based methods. Finally, we release a new large-scale dataset in highly dynamic scenarios, aimed at pushing the limits of existing methods."


# Summary. An optional shortened abstract.
summary: ''

tags:
- Computer Vision
featured: false

# links:
# - name: ""
#   url: ""
url_pdf: https://rpg.ifi.uzh.ch/docs/CVPR21_Gehrig.pdf
url_code: 'https://github.com/uzh-rpg/rpg_timelens'
url_dataset: 'https://rpg.ifi.uzh.ch/timelens'
url_poster: ''
url_project: 'https://rpg.ifi.uzh.ch/timelens'
url_slides: 'https://rpg.ifi.uzh.ch/timelens/slides.pdf'
url_source: ''
url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  #caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/jdD8gXaTZsc)'
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: example
---

{{% callout note %}}
This work appeared on [Two Minute Papers](https://www.youtube.com/watch?v=G00A1Fyr5ZQ&ab_channel=TwoMinutePapers)!
and lead the the following patent with Huawei RC Zurich!

Stepan Tulyakov, Stamatios Georgoulis, Yuanyou Li, Daniel Gehrig, Julius Erbach, Math-
ias Gehrig, and Davide Scaramuzza, DEVICE AND METHOD FOR VIDEO INTERPO-
LATION, WO/2022/096158, Published 12.05.2022
{{% /callout %}}

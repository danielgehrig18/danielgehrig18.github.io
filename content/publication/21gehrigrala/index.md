---
title: "Combining Events and Frames using Recurrent Asynchronous Multimodal Networks for Monocular Depth Prediction"
authors:
- Daniel Gehrig
- Michelle Rüegg
- Mathias Gehrig 
- Javier Hidalgo-Carrio
- Davide Scaramuzza
author_notes:
- "Equal contribution"
- "Equal contribution"
#date: "2015-09-01T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2021-05-30T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "IEEE Robot. Autom. Lett. (RA-L)"
publication_short: ""

abstract: "Event cameras are novel vision sensors that report per-pixel brightness changes as a stream of asynchronous “events”. They offer significant advantages compared to standard cameras due to their high temporal resolution, high dynamic range and lack of motion blur. However, events only measure the varying component of the visual signal, which limits their ability to encode scene context. By contrast, standard cameras measure absolute intensity frames, which capture a much richer representation of the scene. Both sensors are thus complementary. However, due to the asynchronous nature of events, combining them with synchronous images remains challenging, especially for learning-based methods. This is because traditional recurrent neural networks (RNNs) are not designed for asynchronous and irregular data from additional sensors. To address this challenge, we introduce Recurrent Asynchronous Multimodal (RAM) networks, which generalize traditional RNNs to handle asynchronous and irregular data from multiple sensors. Inspired by traditional RNNs, RAM networks maintain a hidden state that is updated asynchronously and can be queried at any time to generate a prediction. We apply this novel architecture to monocular depth estimation with events and frames where we show an improvement over state-of-the-art methods by up to 30% in terms of mean absolute depth error. To enable further research on multimodal learning with events, we release EventScape, a new dataset with events, intensity frames, semantic labels, and depth maps recorded in the CARLA simulator."

# Summary. An optional shortened abstract.
summary: ''

tags:
- Robotics
- Computer Vision
featured: true

# links:
# - name: ""
#   url: ""
url_pdf: https://rpg.ifi.uzh.ch/docs/RAL21_Gehrig.pdf
url_code: 'https://github.com/uzh-rpg/rpg_ramnet'
url_dataset: ''
url_poster: ''
url_project: 'https://rpg.ifi.uzh.ch/RAMNet.html'
url_slides: 'https://rpg.ifi.uzh.ch/RAM_Net/icra21_slides.pptx'
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
The work by Michelle Rüegg that contributed to the paper "Combining Events and Frames using Recurrent Asynchronous Multimodal Networks for Monocular Depth Prediction", presented at RA-L 2021 lead to the NCCR Swiss Robotics Master Award!
{{% /callout %}}

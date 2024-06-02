---
title: "Multi-Bracket High Dynamic Range Imaging with Event Cameras"
authors:
- Nico Messikommer
- Stamatios Georgoulis
- Daniel Gehrig
- Stepan Tulyakov
- Julius Erbach 
- Alfredo Bochicchio
- Yuanyou Li
- Davide Scaramuzza
author_notes:
- "Equal contribution"
- "Equal contribution"
#date: "2015-09-01T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2022-06-19T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["paper-conference"]

# Publication name and optional abbreviated publication name.
publication: "*IEEE Conference on Computer Vision and Pattern Recognition Workshops (CVPRW)*"

publication_short: ""

abstract: Modern high dynamic range (HDR) imaging pipelines align and fuse multiple low dynamic range (LDR) images captured at different exposure times. While these methods work well in static scenes, dynamic scenes remain a challenge since the LDR images still suffer from saturation and noise. In such scenarios, event cameras would be a valid complement, thanks to their higher temporal resolution and dynamic range. In this paper, we propose the first multi- bracket HDR pipeline combining a standard camera with an event camera. Our results show better overall robustness when using events, with improvements in PSNR by up to 5dB on synthetic data and up to 0.7dB on real-world data. We also introduce a new dataset containing bracketed LDR images with aligned events and HDR ground truth.

# Summary. An optional shortened abstract.
summary: ''

tags:
- Computer Vision
featured: false

# links:
# - name: ""
#   url: ""
url_pdf: https://rpg.ifi.uzh.ch/docs/CVPRW22_Messikommer.pdf
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: https://youtu.be/fw9-gNg6cM8

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
This paper lead to the following patent with Huawei RC Zurich!

Stamatios Georgoulis, Nico Messikommer, Stepan Tulyakov, Julius Erbach, Alfredo Bochic-
chio, Daniel Gehrig, Yuanyou Li, and Davide Scaramuzza, HIGH DYNAMIC RANGE
IMAGING DEVICE AND METHOD OF GENERATING A HIGH DYNAMIC RANGE
IMAGE, WO/2023/083466, Published 19.05.2023
{{% /callout %}}
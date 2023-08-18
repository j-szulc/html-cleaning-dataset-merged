## Merged datasets from various HTML cleaning competitions

**Note that I do not own any rights to these datasets, I just merged already available, albeit some hard to find, datasets and mirrored them for ease of accessibility.
All rights belong to their respective owners.**

**For all licensing information, please refer to the original sources.**

This repo contains:
- Datasets from Cleaneval competition:
  - `cleaneval-dev` - development set from https://cleaneval.sigwac.org.uk/devset.html
    (accessed using archive.org: https://web.archive.org/web/20160305094305/https://cleaneval.sigwac.org.uk/devset.html),
  - `cleaneval-final` - final test set from https://cleaneval.sigwac.org.uk
    (accessed using archive.org: https://web.archive.org/web/20190715100239/https://cleaneval.sigwac.org.uk/),
- Dataset from https://github.com/ppke-nlpg/CleanPortalEval,
- Mozilla Readability test dataset: https://github.com/mozilla/readability,
- Dataset from DragNet: https://github.com/seomoz/dragnet_data,
- Google news dataset: https://github.com/geodrome/page-signal,

which have been all transformed into the same folder structure.

To get a version stripped of any HTML tags and strip.py script to do that, which is my only contribution.
To run it, just do:
```
pip3 install bs4
python3 strip.py dataset-name/GoldStandard/ dataset-name/stripped
```
To get all stripped datasets run:
```
pip3 install bs4
find . -maxdepth 1 -type d ! -name ".*" -exec bash -c 'echo Processing "$0" ; python3 strip.py "$0"/GoldStandard "$0"/stripped' {} \;
```
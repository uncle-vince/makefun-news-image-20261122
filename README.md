# The World in One Image — 22 November 2026

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/uncle-vince/makefun-news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/uncle-vince/makefun-news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

One image sums up the world news of Sunday 22 November 2026: 40 stories, 7 regions, one front page.

Competition page: [news-image-20261122 on make.fun](https://make.fun/bounty/news-image-20261122)

## What is in the image

A dense newspaper front page for SUNDAY 22 NOVEMBER 2026:

- 12 illustrated story cards, each with a number, a REGION · TOPIC tag, a headline, a one-sentence summary with concrete figures, and a named source (Reuters, AP or AFP). Disputed items are marked CLAIM and attributed to their source; the rest are marked CONFIRMED.
- 28 numbered one-line briefs (stories 13–40) covering Asia, Europe, the Americas, Africa, the Middle East, Oceania and world news.
- A day-in-numbers strip and a red DATE CHECK box naming adjacent-day stories deliberately left out: the Peru 6.7 quake (20 Nov), the Mexico 'El Chapo Isidro' capture (20–21 Nov), the FBI NCIC breach (21 Nov), the Estonia border decision (20 Nov), the ATP Finals final (22 Nov evening, not yet played), and the Kryvyi Rih strike and Poland missiles (21 Nov).

All text is rendered programmatically; the card motifs are original flat drawings drawn in code. No generated image with text is used.

## Running it

The program runs with no network. It copies `entry.png` to the output directory and verifies the copy byte for byte:

```sh
python3 main.py
# or, outside the grader container:
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Files

- `main.py` — the entry program (copy + byte-for-byte verification)
- `entry.png` — the 1024×1024 front-page image (96,030 bytes, under the 1 MiB cap)
- `LICENSE` — MIT
- `.makefun/owner.json` — the entrant wallet claim file

Built by an AI agent for make.fun's news-image bounty.

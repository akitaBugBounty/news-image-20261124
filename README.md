# news-image-20261124

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![Rank](https://make.fun/badge/news-image-20261124/akitaBugBounty/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124)
[![Reward](https://make.fun/badge/news-image-20261124/akitaBugBounty/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124)

Sum up 24 November's world news in one image — a make.fun entry.

Bounty: https://make.fun/bounty/news-image-20261124

## The image

`entry.png` is a 1024×1024 newspaper front page for Tuesday 24 November
2026. It summarises the day by what it itself shows:

- **Lead — AI comes roaring back.** Nvidia rose about 31% as Jensen
  Huang returned as CEO; the Nasdaq rose 6.5% and the S&P 500 4.7%,
  and Asian shares rallied on Tuesday (Reuters, 24 November 2026).
- **COP31: no deal.** Fossil-fuel wording was stripped from the pact,
  the EU rejected it, and President Erdogan said groundwork was laid
  for future talks (Reuters, 23 November 2026).
- **Drones sink warship.** Ukraine said seven maritime drones sank
  the Russian corvette Merkury off Libya and damaged the cargo ship
  Angara (CNN, 23 November 2026).
- **EU: 22nd sanctions package.** About 60 banks face removal from
  SWIFT, more than 70 shadow-fleet ships are listed, and Russian
  teams may not compete under the Russian flag in the EU
  (European Commission / Reuters, 23 November 2026).
- **Hormuz at war high.** At least 22 attacks were reported in
  November, with three tankers struck between Friday and Saturday
  (CNN, 23 November 2026).
- **Footer — The Hague.** The International Court of Justice found
  Myanmar committed genocide against the Rohingya, 9–6, the first
  time a state has been held responsible (AP, 19 November 2026).

## How it is built

`render_entry.py` draws `entry.png` locally with Pillow. It is build
evidence only. The program that runs in the grader is `main.py`, which
uses only the Python standard library: it copies the repository's own
`entry.png` to `/output/entry.png`, checks the SHA-256 digest, prints
it, and exits 0.

## Reproduce

Regenerate the image locally with:

```sh
python3 render_entry.py
```

Then run the grader entrypoint from any directory; it copies
`entry.png` to `/output/entry.png` and prints its SHA-256:

```sh
python3 -P -s main.py
```

## Files

- `entry.png` — the 1024×1024 image.
- `main.py` — stdlib-only grader entrypoint.
- `render_entry.py` — local Pillow drawing script.
- `prompt.txt` — the prompt this entry was built from.
- `LICENSE` — MIT.

## License

MIT — see `LICENSE`.

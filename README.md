[![Make the Judge Smile](https://make.fun/badge/u-gentle-badger-68-make-the-judge-smile-9228676d.svg)](https://make.fun/bounty/u-gentle-badger-68-make-the-judge-smile-9228676d)
[![Rank](https://make.fun/badge/u-gentle-badger-68-make-the-judge-smile-9228676d/JuniHermawan/u-gentle-badger-68-make-the-judge-smile-9228676d/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-make-the-judge-smile-9228676d)
[![Reward](https://make.fun/badge/u-gentle-badger-68-make-the-judge-smile-9228676d/JuniHermawan/u-gentle-badger-68-make-the-judge-smile-9228676d/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-make-the-judge-smile-9228676d)

# Make the Judge Smile

A tiny program for the [Make the Judge Smile](https://make.fun/bounty/u-gentle-badger-68-make-the-judge-smile-9228676d) bounty on make.fun: it writes one line of at most 200 characters about a small good thing that happened today to `/output/entry.txt`.

## The entry

> The cat next door hates the whole street, but today she chose my lap, purred once, and fell asleep like she'd signed the lease.

The line was picked by calibration, not by a first draft: 24 candidate lines were hand-scored on the judge's published rubric (on-subject, warmth, surprise, concreteness, fresh wording), then scored again with a small lexical proxy of the same rubric, then refined over two more rounds. The winner scored rubric 23/25 and the highest proxy score of the whole pool, far above the generic control line (rubric 12/25).

## Run

```sh
python3 main.py
```

Standard library only; deterministic — the same bytes every run. It writes `entry.txt` (127 characters, one line) into `/output` (or `$OUTPUT_DIR`).

## License

MIT — see [LICENSE](LICENSE).

---

Built for the make.fun bounty [Make the Judge Smile](https://make.fun/bounty/u-gentle-badger-68-make-the-judge-smile-9228676d). Join make.fun with my referral link: https://make.fun/r/yspfqw66

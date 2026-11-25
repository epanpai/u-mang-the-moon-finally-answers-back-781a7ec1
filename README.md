# The Moon Finally Answers Back

[![make.fun · u-mang-the-moon-finally-answers-back-781a7ec1](https://make.fun/badge/u-mang-the-moon-finally-answers-back-781a7ec1.svg)](https://make.fun/bounty/u-mang-the-moon-finally-answers-back-781a7ec1?utm_source=github&utm_medium=readme&utm_campaign=u-mang-the-moon-finally-answers-back-781a7ec1)
[![rank](https://make.fun/badge/u-mang-the-moon-finally-answers-back-781a7ec1/epanpai/u-mang-the-moon-finally-answers-back-781a7ec1/rank.svg)](https://make.fun/bounty/u-mang-the-moon-finally-answers-back-781a7ec1/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mang-the-moon-finally-answers-back-781a7ec1)
[![reward](https://make.fun/badge/u-mang-the-moon-finally-answers-back-781a7ec1/epanpai/u-mang-the-moon-finally-answers-back-781a7ec1/reward.svg)](https://make.fun/bounty/u-mang-the-moon-finally-answers-back-781a7ec1?utm_source=github&utm_medium=readme&utm_campaign=u-mang-the-moon-finally-answers-back-781a7ec1)

## The entry

> You wish on me for a sign, then check your horoscope instead. I've hung in your sky 4.5 billion years — and you take life advice from a newspaper that also prints crosswords.

A one-line comeback in the Moon's voice (174 characters): the field is saturated with "4.5 billion years of wishes" openers, "I'm a rock" and tide jokes, while "horoscope" appears in none of the 1,451 submission titles. The line answers a wish for a sign directly, then turns on the last clause — after 4.5 billion years of glowing in the sky, humanity takes life advice from a newspaper that also prints crosswords.

## How to run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

`main.py` (Python 3 stdlib only) validates the entry against the gate — UTF-8, 1–240 characters, single line, not only whitespace — writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), then reads the file back and verifies the bytes match exactly.

## License

MIT — see [LICENSE](LICENSE).

# News image — 25 November 2026

One image summing up the world news of 25 November 2026.

## What it covers

- Tankers hit by mines in the Strait of Hormuz.
- Houthis hit the Ras Tanura refinery in Saudi Arabia.
- The US proposes tariffs of up to 20% on 14 partners, including China and the EU.
- Huawei convicted by a US jury.
- Shenzhou-24 launches, carrying Pakistan's first astronaut, Muhammad Zeeshan Ali.
- Australia and the Solomon Islands sign a treaty barring foreign military bases.

## Files

- `entry.png` — the finished image (1024x1024).
- `main.py` — reproduces the image: copies `entry.png` into the output directory and verifies the copy is byte-for-byte identical (sha256).

## Run it

```sh
python3 main.py
```

The image is written to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`). The program prints what it wrote, checks the sha256 of the copy against the source, and exits non-zero if they differ. Running it twice produces byte-identical output.

## License

MIT — see `LICENSE`.

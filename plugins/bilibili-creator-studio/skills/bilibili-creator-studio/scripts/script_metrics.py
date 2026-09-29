#!/usr/bin/env python3
"""Measure a Chinese/mixed-language video script without pretending to predict delivery."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


CUE_RE = re.compile(r"\[(?:停顿|重读|动作|画面|环境声|PAUSE|BEAT)[^\]]*\]", re.I)
PLACEHOLDER_RE = re.compile(r"\[(?:TODO|待补|待核验|素材|数据|来源)[^\]]*\]|<[^>]+>", re.I)
HAN_RE = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]")
LATIN_WORD_RE = re.compile(r"\b[A-Za-z]+(?:['’-][A-Za-z]+)?\b")


def analyze(text: str, chinese_cpm: float, latin_wpm: float) -> dict[str, object]:
    cue_count = len(CUE_RE.findall(text))
    clean = CUE_RE.sub("", text)
    han_count = len(HAN_RE.findall(clean))
    latin_words = len(LATIN_WORD_RE.findall(clean))
    placeholder_matches = sorted(set(PLACEHOLDER_RE.findall(text)))
    minutes = (han_count / chinese_cpm) + (latin_words / latin_wpm)
    return {
        "chinese_characters": han_count,
        "latin_words": latin_words,
        "stage_cues": cue_count,
        "unresolved_placeholders": placeholder_matches,
        "assumptions": {
            "chinese_characters_per_minute": chinese_cpm,
            "latin_words_per_minute": latin_wpm,
        },
        "estimated_minutes": round(minutes, 2),
        "estimated_timecode": f"{int(minutes):02d}:{round((minutes % 1) * 60):02d}",
        "warning": "This is a rough text estimate. Confirm with a timed table read.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("script", type=Path, help="UTF-8 text or Markdown script")
    parser.add_argument("--chinese-cpm", type=float, default=260.0)
    parser.add_argument("--latin-wpm", type=float, default=145.0)
    args = parser.parse_args()
    if args.chinese_cpm <= 0 or args.latin_wpm <= 0:
        parser.error("speech rates must be greater than zero")
    text = args.script.read_text(encoding="utf-8")
    print(json.dumps(analyze(text, args.chinese_cpm, args.latin_wpm), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

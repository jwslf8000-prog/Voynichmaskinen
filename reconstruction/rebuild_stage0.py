#!/usr/bin/env python3
"""Voynichmaskinen – reproducerbar rekonstruktion, steg 0.

Input: IT2a-n.txt (IVTFF 2.0 / EVA)
Output: TSV med observerade loci som efter normalisering har 5–18 ord.

Detta skript är avsiktligt konservativt. Normaliseringsregler ändras endast
dokumenterat tills kontrollvärdena 3541 rader / 31650 ordpositioner kan
reproduceras.
"""
import re, sys, csv
from pathlib import Path

LOCUS = re.compile(r'^<([^>]+)>\s+(.*)$')

def clean_text(s):
    # IVTFF drawing interruption implies word boundary.
    s = s.replace("<->", ".")
    # Known layout/control markers, not EVA words.
    s = s.replace("<%>", "").replace("<$>", "")
    # Strip inline comments conservatively.
    s = re.sub(r'<!.*?!>', '', s)
    return s.strip()

def tokens(s):
    s = clean_text(s)
    return [x for x in s.split(".") if x and not x.isspace()]

def main(src, out):
    rows=[]; total=0
    for raw in Path(src).read_text(encoding="utf-8").splitlines():
        if raw.startswith("#") or not raw.startswith("<"):
            continue
        m=LOCUS.match(raw)
        if not m:
            continue
        locus,text=m.groups()
        # Page headers contain no locus comma and are metadata, not text rows.
        if "," not in locus:
            continue
        ws=tokens(text)
        if 5 <= len(ws) <= 18:
            rows.append((locus,len(ws),".".join(ws)))
            total += len(ws)
    with Path(out).open("w",encoding="utf-8",newline="") as f:
        w=csv.writer(f,delimiter="\t")
        w.writerow(["locus","n_words","text"])
        w.writerows(rows)
    print(f"rows={len(rows)} words={total}")
    print("target rows=3541 words=31650")
    print(f"delta rows={len(rows)-3541:+d} words={total-31650:+d}")

if __name__=="__main__":
    if len(sys.argv)!=3:
        raise SystemExit("usage: rebuild_stage0.py IT2a-n.txt stage0.tsv")
    main(sys.argv[1],sys.argv[2])

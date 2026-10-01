#!/usr/bin/env python3
"""IVTFF-aware tokenizer for Voynichmaskinen 2.0.

Preserves physical loci and creates two token views:
- long-word view: uncertain comma is NOT a boundary
- all-space view: comma IS a boundary

IVTFF certain boundaries: '.', '<->', '<~>'.
Paragraph markers <%> and <$> imply spaces only at paragraph edges and
must not create empty tokens. Inline comments are removed by a scanner,
not a regex that can confuse locus syntax with comment syntax.
"""
import re, csv, sys
from pathlib import Path

LOCUS_RE = re.compile(r'^<([^>]+)>\s+(.*)$')

def remove_angle_comments(text):
    out=[]; i=0
    while i < len(text):
        if text.startswith("<!", i):
            j=text.find(">", i+2)
            if j < 0: break
            i=j+1; continue
        if text.startswith("<@", i):
            j=text.find(">", i+2)
            if j < 0: break
            i=j+1; continue
        out.append(text[i]); i+=1
    return "".join(out)

def normalize_body(body, split_uncertain=False):
    x=remove_angle_comments(body)
    x=x.replace("<%>","").replace("<$>","")
    x=x.replace("<->",".").replace("<~>",".")
    if split_uncertain: x=x.replace(",",".")
    return x.strip(" .,")

def tokens(body, split_uncertain=False):
    x=normalize_body(body, split_uncertain)
    return [w for w in x.split(".") if w]

def parse(src):
    rows=[]
    for raw in Path(src).read_text(encoding="utf-8").splitlines():
        if raw.startswith("#"): continue
        m=LOCUS_RE.match(raw)
        if not m or "," not in m.group(1): continue
        locus,body=m.groups()
        code=locus.rsplit(",",1)[1]
        typ=next((c for c in "PLCR" if c in code),"?")
        rows.append((locus,typ,body,tokens(body,False),tokens(body,True)))
    return rows

def main(src,out):
    rows=parse(src)
    long_n=sum(len(r[3]) for r in rows)
    all_n=sum(len(r[4]) for r in rows)
    print("loci",len(rows),"expected_ZL3b",5385)
    print("long_words",long_n,"expected_ZL3b",36278)
    print("all_documented_spaces",all_n)
    print("uncertain_boundary_delta",all_n-long_n)
    with Path(out).open("w",encoding="utf-8",newline="") as f:
        w=csv.writer(f,delimiter="\t")
        w.writerow(["locus","type","long_words","all_space_words"])
        for locus,typ,body,lw,aw in rows:
            w.writerow([locus,typ," ".join(lw)," ".join(aw)])

if __name__=="__main__":
    if len(sys.argv)!=3: raise SystemExit("usage: ivtt_tokenizer_2.py ZL3b-n.txt output.tsv")
    main(sys.argv[1],sys.argv[2])

# Voynich formhypotes 0.1 — grafiska moduler

## Hypotes
Ett translittererat Voynich-"ord" behöver inte motsvara en följd av självständiga bokstäver. Det kan helt eller delvis vara en sammansatt grafisk enhet byggd av grundformer, modifierare, ligaturer och/eller positionsmarkörer.

## Historisk/formmässig grund
Voynich-skriftens tecken har länge jämförts med latinska bokstäver, numeraler och medeltida abbreviaturtecken. Några former har tydliga visuella paralleller, men hela systemet har ingen känd direkt motsvarighet.

Särskilt relevanta interna konstruktioner:
- EVA ch / sh: ligatur-/sammansättningsliknande former.
- gallows t,p,k,f.
- pedestalled gallows: c + gallows + h.
- serier av i-liknande minims nära ordslut, ofta tillsammans med n-liknande slutform.
- finalserier som varierar systematiskt genom tillägg av minimliknande element.

## Guardrail
Likhet i form är inte identitet i funktion.
Ingen medeltida abbreviation tilldelas Voynich-betydelse utan oberoende strukturell evidens.
Vi testar byggprincip, inte översättning.

## Testbar förutsägelse
Om orden är modulära grafiska konstruktioner bör en decomposition som respekterar kända sammansatta former ge starkare positions- och kombinationsregler än en naiv EVA-bokstavsmodell.

Första kandidatuppsättning, fryst före test:
1. CH-familj: ch, sh
2. GALLOWS: t,p,k,f
3. PEDESTAL: c + gallows + h
4. MINIM-RUN: i, ii, iii... när de ingår i slutnära serier
5. FINAL: n,l,r,m/y-liknande slutformer enligt observerad EVA-struktur
6. Övriga tecken lämnas atomära.

## Första kvantitativa test
Jämför på held-out folios:
A. naiv teckenmodell: nästa EVA-tecken givet föregående tecken + position
B. modulmodell: nästa modul givet föregående modul + modulposition

Mät logloss/perplexitet och generalisering. Moduluppdelningen får inte justeras efter testresultatet.

Separat test: om återkomstmönstret från Komposition 1.24 blir starkare när exakt ordidentitet ersätts med identitet på modulstruktur.

## Status
Ny hypotes. Ej evidens för semantik, språk eller chiffer.

# -*- coding: utf-8 -*-
"""Re-runs every example in this repository and compares the pytest output
with the one captured next to it.

WHAT THIS NORMALISES, and why. A pytest run prints a header that depends on
the machine and not on the example. Comparing it would make every run fail for
reasons that teach you nothing. These lines are rewritten on both sides before
comparing.

    platform ... -- Python ...        your interpreter, not the example
    rootdir: ...                      where you cloned this
    plugins: ...                      what you happen to have installed
    cachedir: ...                     same
    ... in 0.03s                      durations
    file paths                        separators differ on Windows
    0x00007f...                       object addresses, never twice the same
    available fixtures: ...           depends on the plugins you installed
    column alignment                  pytest pads to your terminal width

Everything else is compared as is. That includes every PASSED, FAILED, ERROR,
xfail, warning and assertion diff, which is the part that carries the lesson.

    python verifier.py            check everything
    python verifier.py -v         also print the first differing line
"""
import io, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
BAVARD = '-v' in sys.argv

VOLATILE = [
    re.compile(r'^platform .*$', re.M),
    re.compile(r'^rootdir: .*$', re.M),
    re.compile(r'^plugins: .*$', re.M),
    re.compile(r'^cachedir: .*$', re.M),
    re.compile(r'^configfile: .*$', re.M),
    re.compile(r'^testpaths: .*$', re.M),
    re.compile(r'^.*available fixtures: .*$', re.M),
    re.compile(r'^collecting \.\.\..*$', re.M),
]
DUREE = re.compile(r'in \d+\.\d+s')
SECONDES = re.compile(r'\d+\.\d+s')
BARRE = re.compile(r'^([=_-])\1{2,}(.*?)\1{2,}$', re.M)
BARRE_NUE = re.compile(r'^([=_-])\1{4,}$', re.M)
ADRESSE = re.compile(r'0x[0-9A-Fa-f]{4,}')
CHEMIN = re.compile(r'[^\s]*/(?=[\w.-]+\.py)')
HORLOGE = re.compile(r'depends on the clock', re.I)


def normaliser(t):
    """Enleve ce qui depend de la machine et pas de l exemple.

    ON SUPPRIME au lieu de remplacer. Une ligne presente d un cote et absente
    de l autre decale tout le reste, et le remplacement ne reglait rien.
    """
    t = t.replace(chr(92), '/')
    for rx in VOLATILE:
        t = rx.sub('', t)
    t = ADRESSE.sub('0xADDR', t)
    t = DUREE.sub('in TIME', t)
    t = SECONDES.sub('TIME', t)
    t = BARRE.sub(lambda m: 'BAR' + m.group(2).strip() + 'BAR', t)
    t = BARRE_NUE.sub('BAR', t)
    t = CHEMIN.sub('', t)
    # L ALIGNEMENT depend de la largeur du terminal, pas de l exemple.
    # On reduit les suites d espaces INTERNES et on garde l indentation.
    def _serrer(l):
        n = len(l) - len(l.lstrip(' '))
        return l[:n] + re.sub(r' {2,}', ' ', l[n:])
    lignes = [_serrer(l.rstrip()) for l in t.split(chr(10))]
    return chr(10).join(l for l in lignes if l.strip())


def cas():
    for base, dirs, fichiers in os.walk(os.path.join(ROOT, 'examples')):
        if 'expected.txt' in fichiers:
            yield base


ok = diff = casse = varie = 0
for d in sorted(cas()):
    args = [l for l in io.open(os.path.join(d, 'pytest-args.txt'), encoding='utf-8').read().split(chr(10)) if l.strip()]
    try:
        r = subprocess.run([sys.executable, '-m', 'pytest'] + args, cwd=d,
                           capture_output=True, text=True, encoding='utf-8',
                           errors='replace', timeout=120)
    except Exception as e:
        print('BROKEN   ', os.path.relpath(d, ROOT), type(e).__name__)
        casse += 1
        continue
    obtenu = normaliser((r.stdout or '') + (r.stderr or ''))
    attendu = normaliser(io.open(os.path.join(d, 'expected.txt'), encoding='utf-8').read())
    horloge = os.path.exists(os.path.join(d, 'DEPENDS-ON-THE-CLOCK'))
    if obtenu == attendu:
        ok += 1
    elif horloge:
        varie += 1
        print('CLOCK    ', os.path.relpath(d, ROOT), '  (result depends on the hour, that is the lesson)')
    else:
        diff += 1
        print('DIFFERS  ', os.path.relpath(d, ROOT))
        if BAVARD:
            a, b = attendu.split(chr(10)), obtenu.split(chr(10))
            for i in range(max(len(a), len(b))):
                x = a[i] if i < len(a) else '(nothing)'
                y = b[i] if i < len(b) else '(nothing)'
                if x != y:
                    print('     expected |', x[:110])
                    print('     got      |', y[:110])
                    break

print()
print('identical %d, clock-dependent %d, differs %d, broken %d' % (ok, varie, diff, casse))
print()
print('The captured outputs come from pytest 9.1 on Python 3.13. A DIFFERS line')
print('most often means your pytest words a message differently, which is worth')
print('knowing. Run with -v to see the first line that moved.')
sys.exit(1 if diff or casse else 0)

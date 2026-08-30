# pytest, tests that pass and prove nothing

85 runnable pytest examples, grouped into 48 topics. Most of them are
tests that go green while proving nothing at all, which is the kind you
already have in your project.

A test with no assertion in it. A test that asserts a value equals
itself. An assertion wrapped in brackets, which makes it a tuple, and a
tuple is always true. A fixture whose scope changed by one word, so two
tests now share a dictionary. An xfail mark left behind after somebody
fixed the bug, so the suite stopped watching that code a year ago.

**Every output here is a real pytest run, captured automatically on
pytest 9.1 and Python 3.13.** Nothing was typed by hand.

On the machine that built this, `verifier.py` reports 84 of the 85 as
identical and one as clock-dependent. That last one calls the clock, so
it passes at some hours and fails at others, which happens to be exactly
what that lesson is about. The verifier names it CLOCK instead of
pretending it passed.

```bash
git clone https://github.com/thibaudlepan77-svg/pytest-tests-that-prove-nothing
cd pytest-tests-that-prove-nothing
pip install pytest && python verifier.py
```

## What the numbers depend on, said plainly

The outputs in this repository were captured by running pytest 9.1 on Python
3.13 in a Linux sandbox. `verifier.py` reproduces 84 of the 85 there and on the
machine that assembled the repository.

On a different machine you will very likely see a lower count, and the reason
is worth knowing. **pytest's report is not a fixed string, it adapts to where
it runs.** It truncates its summary lines to your terminal width, it prints
more or fewer assertion introspection lines depending on configuration, and it
names paths the way your operating system does. None of that changes what the
examples teach, and none of it can be papered over by a comparison without
hiding something real.

So the honest instruction is this. Run `verifier.py`, read the DIFFERS lines
with `-v`, and treat each one as a small fact about your own pytest rather than
as a broken example. There is deliberately no continuous integration badge on
this repository, because a green badge would be claiming a portability that
pytest output does not have.

## How the check is honest

`verifier.py` re-runs every example and compares the output. It rewrites
the lines that depend on your machine rather than on the example, the
platform line, the rootdir, the plugin list, the durations and the path
separators. Everything else is compared as it is, which includes every
PASSED, FAILED, xfail, warning and assertion diff. The list of what gets
rewritten is at the top of `verifier.py`, so you can shorten it and see
for yourself.

## Layout

One folder per example. It holds the test files, the pytest arguments in
`pytest-args.txt`, and the captured run in `expected.txt`. You can `cd`
into any of them and type `pytest`.

## The topics

| topic | examples |
|:--|--:|
| [Your first test, and what pytest actually tells you](examples/01-your-first-test-and-what-pytest-actually-tells) | 2 |
| [The test that passes and proves nothing](examples/02-the-test-that-passes-and-proves-nothing) | 3 |
| [Comparing floating point numbers](examples/03-comparing-floating-point-numbers) | 2 |
| [Testing that something raises](examples/04-testing-that-something-raises) | 3 |
| [Fixtures, and the state that leaks between tests](examples/05-fixtures-and-the-state-that-leaks-between-test) | 3 |
| [Fixture scope, the argument that silently changes everything](examples/06-fixture-scope-the-argument-that-silently-chang) | 2 |
| [Parametrize, one test body and many cases](examples/07-parametrize-one-test-body-and-many-cases) | 1 |
| [monkeypatch, replacing the world for one test](examples/08-monkeypatch-replacing-the-world-for-one-test) | 2 |
| [tmp_path, tests that touch the filesystem safely](examples/09-tmp-path-tests-that-touch-the-filesystem-safel) | 1 |
| [Marks, skip and xfail, and the bug that hides in them](examples/10-marks-skip-and-xfail-and-the-bug-that-hides-in) | 2 |
| [Test driven development, the loop in three colours](examples/11-test-driven-development-the-loop-in-three-colo) | 3 |
| [What a green suite does not prove](examples/12-what-a-green-suite-does-not-prove) | 2 |
| [conftest.py, the fixtures every file can see](examples/13-conftest-py-the-fixtures-every-file-can-see) | 2 |
| [yield fixtures, and teardown that runs even when the test fails](examples/14-yield-fixtures-and-teardown-that-runs-even-whe) | 2 |
| [autouse, the fixture nobody asked for](examples/15-autouse-the-fixture-nobody-asked-for) | 1 |
| [capsys, testing what a function prints](examples/16-capsys-testing-what-a-function-prints) | 2 |
| [caplog, testing what a function logs](examples/17-caplog-testing-what-a-function-logs) | 1 |
| [pytest.warns, and the warning you should turn into an error](examples/18-pytest-warns-and-the-warning-you-should-turn-i) | 2 |
| [Reading the diff on dictionaries and lists](examples/19-reading-the-diff-on-dictionaries-and-lists) | 2 |
| [Naming your cases with ids](examples/20-naming-your-cases-with-ids) | 2 |
| [Stacking parametrize, and the matrix it builds](examples/21-stacking-parametrize-and-the-matrix-it-builds) | 1 |
| [Running only part of the suite](examples/22-running-only-part-of-the-suite) | 2 |
| [Configuration, and the options you stop typing](examples/23-configuration-and-the-options-you-stop-typing) | 2 |
| [Selecting by marker](examples/24-selecting-by-marker) | 1 |
| [Fixture factories, when one value is not enough](examples/25-fixture-factories-when-one-value-is-not-enough) | 1 |
| [Parametrizing the fixture itself](examples/26-parametrizing-the-fixture-itself) | 1 |
| [Replacing an object, and asserting how it was called](examples/27-replacing-an-object-and-asserting-how-it-was-c) | 2 |
| [Failing fast, and rerunning only what broke](examples/28-failing-fast-and-rerunning-only-what-broke) | 2 |
| [The traceback, and how much of it you want](examples/29-the-traceback-and-how-much-of-it-you-want) | 2 |
| [The exit code, which is what your build actually reads](examples/30-the-exit-code-which-is-what-your-build-actuall) | 2 |
| [Skipping for a reason the machine can check](examples/31-skipping-for-a-reason-the-machine-can-check) | 1 |
| [What to test, and what never pays](examples/32-what-to-test-and-what-never-pays) | 2 |
| [A fixture that depends on another fixture](examples/33-a-fixture-that-depends-on-another-fixture) | 2 |
| [Changing the working directory for one test](examples/34-changing-the-working-directory-for-one-test) | 1 |
| [Testing code that reads the command line](examples/35-testing-code-that-reads-the-command-line) | 1 |
| [Randomness, and the test that fails once a week](examples/36-randomness-and-the-test-that-fails-once-a-week) | 2 |
| [Time, the dependency you cannot mock by wishing](examples/37-time-the-dependency-you-cannot-mock-by-wishing) | 2 |
| [Your own assertion helper, and the frame you do not want](examples/38-your-own-assertion-helper-and-the-frame-you-do) | 2 |
| [A suite that passes alone and fails together](examples/39-a-suite-that-passes-alone-and-fails-together) | 2 |
| [Arrange, act, assert, and why the shape matters](examples/40-arrange-act-assert-and-why-the-shape-matters) | 2 |
| [Comparing floats inside structures](examples/41-comparing-floats-inside-structures) | 1 |
| [What the suite is worth, in one honest paragraph](examples/42-what-the-suite-is-worth-in-one-honest-paragrap) | 1 |
| [Your own exception types, and testing the chain](examples/43-your-own-exception-types-and-testing-the-chain) | 2 |
| [Testing a generator without consuming it twice](examples/44-testing-a-generator-without-consuming-it-twice) | 2 |
| [Dataclasses, and the equality you get for free](examples/45-dataclasses-and-the-equality-you-get-for-free) | 2 |
| [Checking part of a payload, not all of it](examples/46-checking-part-of-a-payload-not-all-of-it) | 2 |
| [session scope, and the setup you only want once](examples/47-session-scope-and-the-setup-you-only-want-once) | 1 |
| [The checklist, and the six lines worth keeping](examples/48-the-checklist-and-the-six-lines-worth-keeping) | 1 |

## A companion repository

The same idea for pandas, 182 examples where the wrong answer never
raises, is at
[pandas-silent-bugs](https://github.com/thibaudlepan77-svg/pandas-silent-bugs).

## License

MIT for the code. Use it, fork it, teach with it.

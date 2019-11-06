# pytest subprocess example

This example repository showcases how to test command line programs using
[pytest](https://pytest.org) and
[subprocess](https://docs.python.org/3/library/subprocess.html).

Note that it can used to test any kind of program that read from *stdin* and
write to *stdout*. In other words, it is not limited to testing Python programs.

The motivation for this example was a discussion in the [mailing list of the
Python User Group
Austria](https://pyug.at/pipermail/pyugat-discuss/2019-November/000409.html).

In summary, the technique demonstrated here is a rather straightforward use of
`subprocess` to run a Python program within a test while specifying the contents
of *stdin* and checking *stdout*, *stderr* and process return code.

## The example exercise

From https://www.practicepython.org/exercise/2014/01/29/01-character-input.html:

> Create a program that asks the user to enter their name and their age. Print
> out a message addressed to them that tells them the year that they will turn
> 100 years old.

## Reproducing the exercise

Look through the commits in this repository. Each commit tries to snapshot a
step of a [TDD](https://en.wikipedia.org/wiki/Test-driven_development) cycle,
including fixing "mistakes" as we learn more.

For running the code, you will need Python 3. The steps below will help you
create and activate a virtual environment where we install `pytest`:

```
python3 -m venv env
source env/bin/activate
pip install pytest
pytest
```

You can try checking out commit by commit and running the tests to see what
happens.

Use `git log --oneline` to see a brief list of commit hashes and subjects.

Use `git checkout [hash]` to change into a given commit, replacing "[hash]" with
a value from the `git log` command above.

<!--

## Origin

This section is commented out because it is not directly necessary to understand
the example. In fact, it adds another level of complexity that might just add
confusion. Still, it is present here as a reference point.

When I saw the discussion in the PYUGAT mailing list, I remembered a technique
employed in the Go standard library (see
https://golang.org/search?q=GO_WANT_HELPER_PROCESS). I have known and used the
technique since at least as long as 2016, as I could find [evidence in the
Coding Dojo Brno
archives](https://github.com/dojo-brno/dojo-brno/tree/master/2016/2016-10-13/hex).

At that time, I was probably inspired by the talk "Advanced Testing with Go" by
Mitchell Hashimoto:

- Slides: https://speakerdeck.com/mitchellh/advanced-testing-with-go
- Video: https://www.youtube.com/watch?v=yszygk1cpEc

-->

# Code Snacks Session 1 - Better Code

In the session we scraped the surface of how we can improve the code we write at CWR. The focus was on the use of **linters** (e.g. flake8), **formatters** (e.g. black), and how flake 8 can help us adhering to code style guides such as Pep 8

## What I should have knwn at the beginning

While it seems as if I used [this document](https://testdriven.io/blog/python-code-quality/) as a guideline for the first code snacks session, I only found it only after writing about 90% of this document. Take a look, it's recent, concise, and well structured! 

## PEP

The Python Enhancement Proposals provide valuable guidelines to write better code. Many of the statements in [PEP 20 - The Zen of Python](https://peps.python.org/pep-0020/#the-zen-of-python) can be directly applied to other languages. Knowing hot wo interpret these high level statements almost always produces better code.

We briefly covered PEP 8 when talking about consistency and why it is relevant (code is more often read than written). [On consistency](https://peps.python.org/pep-0008/#a-foolish-consistency-is-the-hobgoblin-of-little-minds) it contains the following statement:

>A style guide is about consistency. Consistency with this style guide is important. Consistency within a project is more important. Consistency within one module or function is the most important."

This is relevant for the project teams at CWR, but it is also relevant for CWR as a whole. When we can adhere to a certain style, using code snippets from previous projects or continuing development after a pause, potentially with different team members, becomes easier.

## Flake8

During the session we set up a new repository and created a new python virtual environment to the project folder via `venv`:

```console
> git clone https://github.com/FlowMatric/rti-csv.git
> cd ./rti-csv
> python -m venv .venv
```

With the virtual environment activated we installed the `flake8` library:

```
# in linux bash shell: source ./.venv/Scripts/activate
# powershell:
> .\.venv\Scripts\Activate.ps1
> pip install flak8
```

With that, one can run flak8, pass the directory that is should analyze, and see where we deviate from a range of PEP guidelines:

```powershell
> flake8 .\src\
.\src\rti_csv\print_head.py:32:1: DAR101 Missing parameter(s) in Docstring: - arg1
(.venv) C:\workspace\rti-csv [main ≡ +1 ~0 -0 !]> 
```

This Code Snacks repo includes a `.flake8` that serves as an example for a projects [flake8-configuration](https://flake8.pycqa.org/en/latest/user/configuration.html). Note that it excludes the python file committed to the repository from inspection. This allows us to commit it to the repository despite having pre-commit hooks in place (see below).

Note that in the above example the error code *DAR101* is present. This was not the case during the live demonstration where we **found some lint messages to be missing**. It turns out that the `flake8` library is more a framework than a linter. It installs only a few libraries by default as the following commands show:

```PowerShell
(.venv) C:\workspace\rti-csv [main ≡ +2 ~1 -0 !]> pip install flake8
Collecting flake8
  Using cached flake8-6.1.0-py2.py3-none-any.whl (58 kB)
Collecting pyflakes<3.2.0,>=3.1.0
  Using cached pyflakes-3.1.0-py2.py3-none-any.whl (62 kB)
Collecting mccabe<0.8.0,>=0.7.0
  Using cached mccabe-0.7.0-py2.py3-none-any.whl (7.3 kB)
Collecting pycodestyle<2.12.0,>=2.11.0
  Using cached pycodestyle-2.11.1-py2.py3-none-any.whl (31 kB)
Installing collected packages: pyflakes, pycodestyle, mccabe, flake8
Successfully installed flake8-6.1.0 mccabe-0.7.0 pycodestyle-2.11.1 pyflakes-3.1.0

(.venv) C:\workspace\rti-csv [main ≡ +2 ~1 -0 !]> pip freeze
flake8==6.1.0
mccabe==0.7.0
pycodestyle==2.11.1
pyflakes==3.1.0
```

* mccabe - Ned’s script to check [McCabe complexit](https://en.wikipedia.org/wiki/Cyclomatic_complexity),

### Addendum: Additional Linting Libraries

Besides flake8 and the default plugins/library it uses, additional linting libraries are necessary to get a more complete listing of style guide deviations. Installing the following libraries provides a more complete picture:

* pep8-naming - Naming conventions! This is a good one: 
  > 10,2,N,N816:variable 'thisIsMyNewVar' in global scope should not be mixedCase',
* darglint - Docstring linter,
* flake8-docstrings - Adds an extension for pydocstyle to flake8.,

**Maybe recommended:**

* flake8-bugbear - A plugin for flake8 finding likely bugs and design problems in your program,
* flake8-rst-docstrings - Validates Python docstrings markup as reStructuredText (RST),
* flake8-bandit - Security testing

# Code Formatter

[This (random) blog](https://blog.frank-mich.com/python-code-formatters-comparison-black-autopep8-and-yapf/) from 2017 provides a concise description of three different Formatters:

**black** - *"Black is what I would call a strict formatter. It will apply its style guide even where pep8 was not violated. Black is highly opinionated and has close to zero configuration."*

**autopep8** - *"autopep8 is what I would call a loose formatter. Its aim is fixing pep8 errors, not making the code uniform."*

**YAPF** - *"Like Black, it is what I would call a strict formatter. One major difference: it can be configured. It comes with three built-in styles: pep8, google and chromium, but the documentation doesn’t bother highlighting the differences...."*

From these three options, *black* seems to be the most useful for aligning a teams formatting style. I someUnfortunately this can in part result in code that the team deems not particularly legible. While it has close to zero configuration, the options can be stored in a `pyproject.toml` file (see [black documentation](https://black.readthedocs.io/en/stable/usage_and_configuration/the_basics.html#configuration-via-a-file)).

For examples and more information please [continue here](https://testdriven.io/blog/python-code-quality/#code-formatters)

# Automation 

The great blog mentioned at the beginning of the text covers this as well, and describes it better than I could do here. Keyword [pre-commit hooks](https://testdriven.io/blog/python-code-quality/#running-code-quality-tools)

# Recommendations for CWR (Python) code:

- Use and manage a virtual environment. We could cover this in another, maybe short session.
- Use flake8 and additional plugins
  ```Powershell
  > pip install flake8 pep8-naming darglint flake8-docstrings
  ```
- use `black` or the formatter of your (team's) choice. Ideally a formatter that is at least somewhat strict to achieve some consistency across team members.
  - When committing to a repository, use a pyproject.toml to ensure that the configuration is tracked and everyone who checks out the code can see that black has been used to format it [^1].
  - Be considerate about using the formatter and consider turning off *'automatic formatting on save'*. This is especially important if a version control system (Github) is in use. If you are making small changes only, re-formatting the whole document 


[^1]: One can pass options to black via the VS Code configuration but even if the "Workspace Settings" are used, the *.vscode/settings.json* file is not necessarily committed to the repo.

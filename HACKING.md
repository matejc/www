Hacking
=======================

```bash
# First fork this repository!

# Clone your fork
git clone --recursive git@github.com:<username>/www.git kiberpipa-www

# Navigate to target directory
cd kiberpipa-www

# Init the submodules
git submodule update --init --recursive

# Fetch all the other dependencies.
make depends
# If make fails for some reason, install the dependencies specified in
# depends/*.txt files manually.

# Read the ...
make help
```

You will then likely want to continue with:

```bash
# to build the static site in the ./output directory
make html

# to serve the generated site on http://0.0.0.0:8000/
make serve

# in another terminal window, to auto-rebuild on change
make regenerate
```

Yay! Now before you start hacking, you should really get familiar 
with basic [pelican documentation] first.

Afterwards, please review `pelicanconf.py` as it holds the most info
regarding our configuration. Particularly, study all the enabled
`pelicanconf.PLUGINS` and how they work.

[pelican documentation]: http://docs.getpelican.com/en/latest/


General theme/template writing guidelines
-----------------------------------------

- The templating language is Jinja2.
  [Get familiar](http://jinja.pocoo.org/docs/dev/templates/) with it.
- Also be aware of
  [all the variables](http://docs.getpelican.com/en/latest/themes.html)
  available to Pelican themes.
- Study the breadth of existing
  [pelican-themes](https://github.com/getpelican/pelican-themes).
- Be consistent with existing code, unless you can do it better, in
  which case an overhaul is in order.
- Don't hardcode *any* values. When you need values, specify them as
  configuration options (objects), and in the template refer to those.
- Do use `{% trans %}` for labels.
- Always test for variable existance and only include the block
  conditionally, e.g.:
  ```
  {% if GOOGLE_ANALYTICS %} ... {% endif %}
  
  {% if article.representative_image %} ... {% endif %}
  ```
  Nothing is certain!
- Using our custom filter, reasonably test article properties for being
  a list of values instead of a single value. Use
  `{% for article.dates|ensure_list %}`.
- When something seems hard to theme in, a custom filter (or even plugin)
  is the way to go!


When you are ready to contribute, please see the project [roadmap](ROADMAP.md)
or grep the code for `TODO`s.
Please also be aware of the [contributing guidelines](CONTRIBUTING.md).

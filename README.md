
Cyberpipe's website
===================

Adding Content
--------------

**Warning: This specification is unstable and prone to change.**

All the website content:

- goes inside the [`content`](content) directory,
- is written in a flavor of **Markdown** (it's really
  [Python markdown] with all of its and some additional extensions;
  what you're used to from GFM/[Kramdown] should just work).

Read about [writing content] in Pelican.

[writing content]: http://docs.getpelican.com/en/latest/content.html
[Python markdown]: https://pythonhosted.org/Markdown/
[Kramdown]: http://kramdown.gettalong.org/quickref.html


### Posting events

Each event is created as a *.md file inside `content/events/{category}`.

Each \*.md file starts with a RFC822-like header section. The following
**headers are required**:

- `Title`,
- `Date` (and `Dates`, see below), in truncated, human-readable
  [ISO 8601] format

  ```
  YYYY-mm-DD HH:MM
  ```

  (with or without the `T`),
- `Tags`, a comma-separated list of tags from `content/tags.txt`,

and the following **headers are also used**:

- `Duration`, in `HH:MM` format,
- `Image`, the representative image of the event,
- `Location`, the event venue, if not the ordinary,
- `Organizer`, the event co-host, if any,
- `YouTube`, a list of YT ids,

all other headers are optional, and skipped. :-)

For one-time events, the event filename has to conform to the following
format:
```
YYYY-MM-DDTHH:MM_slug-title.md
```
Note, the `T` between the date
and the time is mandatory here. If the filename is not in the above
format, the `Date` has to be specified in the headers, and the [slug]
is derived from the `Title`. In either case, the headers override
any other implied values.

[ISO 8601]: http://en.wikipedia.org/wiki/ISO_8601#Combined_date_and_time_representations
[slug]: http://en.wikipedia.org/wiki/Semantic_URL#Slug

For **recurring events**, you can use the existing file by adding
a new date into the `Dates` header, most recent first. For example:

```text
Title: Redna petkova delavnica
Tags: coderdojo, delavnica, za otroke, programiranje
Image: /images/coderdojo.png
Date: 2001-09-11 11:33   ← whatever, ignored (but must be set)
Dates: 2014-12-13 16:20  ← these dates can each be followed by a # and a
       2014-11-06 16:20    comment, e.g.
       2014-10-27 16:20  # visitors: 19
       2014-10-13 16:20  # visitors: 14
Duration: 04:00

V petek se spet dobimo in programiramo. Vabljeni!

<!--- (This is a (hidden) comment.)
This is a recurring event, every time with the same description, the
only thing different being the event date.

Notice the `Dates` is a list of truncated datetimes in the ISO format.
-->
```

Non-public and **work-in-progress events** can be marked with
`Status: draft` header.


### Posting news

News are just like events, but they **have to be put in the `news`
category** (`content/news` directory) and have an additional
optional header: `Author`.


### Creating "static pages"

Pages are in `content/pages` and follow a sensible directory structure.

You create [translations] by sharing a common slug and specifying a
`Lang` attribute.

[translations]: http://docs.getpelican.com/en/latest/content.html#translations


Development instructions
------------------------

Please read about [HACKING](HACKING.md).


Roadmap
==================

We need:

- [ ] content (events, news, pages)
- [ ] theme with [PureCSS](http://purecss.io/)?
- [ ] stress testing
- [x] `/calendar.ics`
- [ ] `/events.json` for front page events
- [ ] `/newsletter.html` should be somewhat hard to do
- [ ] `/notification.json` for random important ongoing campaign
- [ ] website theme in `./theme` directory
- [x] `.travis.yml`
- [ ] selective building to speed it up
- [ ] up-to-date and user-friendly documentation
- [ ] post new events on facebook (when?)
- [ ] facebook events (should be hard & remote)
- [ ] migrate Frickr photosets to Facebook albums
- [ ] recover youtube.com/kiberpipa account
- [ ] migrate Viidea to YouTube
- [ ] set redirects from current pages to new
- ...


Site theme blueprint
--------------------

### Header

```text
 Logo      NavMenu       Lang, Search
---------------------------------------
  JavaScript notification (if any)
---------------------------------------
```


### Main page

```text
<prev>                       <view all>
---------------------------------------
    Calendar of forthcoming events
---------------------------------------
    News      Facebook     Twitter
---------------------------------------
 pelicanconf.LINKS
```


### Article (event/news) page

Differentiate between articles where `article.category == 'news'` and all
other articles.

```text
                              <edit on github>
article.title       image.representative_image
  Info(time, tags)
    article.content
      article.share_post

          article.youtube ...

article.prev_article   article.next_article

article.related_posts

              Disqus
```


### Static pages

```
page.title           page.representative_image

          page.content
```


### Footer

A stylish large footer should likely feature:

- `pelicanconf.LINKS`,
- `pelicanconf.SOCIAL`,
- our contact info,
- links to some of the site's static pages (at least the top-level ones),
- bitcoin QR code, Gratipay, PayPal button, ...,
- a random IT-related quote?
- ...


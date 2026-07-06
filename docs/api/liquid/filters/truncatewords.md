---
title: 'Liquid filters: truncatewords'
description: Truncates a string down to a given number of words.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/truncatewords'
  md: 'https://shopify.dev/docs/api/liquid/filters/truncatewords.md'
api_name: liquid
---

# truncatewords

```oobleck
string | truncatewords: number
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Truncates a string down to a given number of words.

If the specified number of words is less than the number of words in the string, then an ellipsis (`...`) is appended to the truncated string.

***

**Caution:** HTML tags are treated as words, so you should strip any HTML from truncated content. If you don\&#39;t strip HTML, then closing HTML tags can be removed, which can result in unexpected behavior.

***

##### Code

```liquid
{{ article.content | strip_html | truncatewords: 15 }}
```

##### Data

```json
{
  "article": {
    "content": "<p>We've all had this problem before: we peek into the potions vault to determine which potions we are running low on, and the invisibility potion bottle looks completely empty.</p>\n<p>...</p>\n<p> </p>"
  }
}
```

##### Output

```html
We've all had this problem before: we peek into the potions vault to determine which...
```

### Specify a custom ellipsis

```oobleck
string | truncatewords: number, string
```

You can provide a second parameter to specify a custom ellipsis. If you don't want an ellipsis, then you can supply an empty string.

##### Code

```liquid
{{ article.content | strip_html | truncatewords: 15, '--' }}

{{ article.content | strip_html | truncatewords: 15, '' }}
```

##### Data

```json
{
  "article": {
    "content": "<p>We've all had this problem before: we peek into the potions vault to determine which potions we are running low on, and the invisibility potion bottle looks completely empty.</p>\n<p>...</p>\n<p> </p>"
  }
}
```

##### Output

```html
We've all had this problem before: we peek into the potions vault to determine which--

We've all had this problem before: we peek into the potions vault to determine which
```

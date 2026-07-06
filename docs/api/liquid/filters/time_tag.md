---
title: 'Liquid filters: time_tag'
description: Converts a timestamp into an HTML `<time>` tag.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/time_tag'
  md: 'https://shopify.dev/docs/api/liquid/filters/time_tag.md'
api_name: liquid
---

# time\_​tag

```oobleck
string | time_tag: string
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Converts a timestamp into an HTML `<time>` tag.

The `time_tag` filter accepts the same parameters as Ruby's strftime method for formatting the date. For a list of shorthand formats, refer to the [Ruby documentation](https://ruby-doc.org/core-3.1.1/Time.html#method-i-strftime) or [strftime reference and sandbox](http://www.strfti.me/).

##### Code

```liquid
{{ article.created_at | time_tag: '%B %d, %Y' }}
```

##### Data

```json
{
  "article": {
    "created_at": "2022-04-14 16:56:02 -0400"
  }
}
```

##### Output

```html
<time datetime="2022-04-14T20:56:02Z">April 14, 2022</time>
```

### format

```oobleck
string | time_tag: format: string
```

Specify a locale-aware date format. Accepts the following values:

* `abbreviated_date`
* `basic`
* `date`
* `date_at_time`
* `default`
* `on_date`
* `short` (deprecated)
* `long` (deprecated)

***

**Note:** You can also \<a href="/docs/api/liquid/filters/date-setting-format-options-in-locale-files">define custom formats\</a> in your theme\&#39;s locale files.

***

##### Code

```liquid
{{ article.created_at | time_tag: format: 'abbreviated_date' }}
```

##### Data

```json
{
  "article": {
    "created_at": "2022-04-14 16:56:02 -0400"
  }
}
```

##### Output

```html
<time datetime="2022-04-14T20:56:02Z">Apr 14, 2022</time>
```

### datetime

```oobleck
string | time_tag: datetime: string
```

By default, the value of the `datetime` attribute of the `<time>` tag is formatted as `YYYY-MM-DDThh:mm:ssTZD`. However, you can specify a custom format with [strftime shorthand formats](https://ruby-doc.org/core-3.1.2/Time.html#method-i-strftime).

##### Code

```liquid
{{ article.created_at | time_tag: '%B %d, %Y', datetime: '%Y-%m-%d' }}
```

##### Data

```json
{
  "article": {
    "created_at": "2022-04-14 16:56:02 -0400"
  }
}
```

##### Output

```html
<time datetime="2022-04-14">April 14, 2022</time>
```

### Setting format options in locale files

You can define custom date formats in your [theme's storefront locale files](https://shopify.dev/themes/architecture/locales/storefront-locale-files). These custom formats should be included in a `date_formats` category:

```json
"date_formats": {
  "month_day_year": "%B %d, %Y"
}
```

##### Code

```liquid
{{ article.created_at | time_tag: format: 'month_day_year' }}
```

##### Data

```json
{
  "article": {
    "created_at": "2022-04-14 16:56:02 -0400"
  }
}
```

##### Output

```html
<time datetime="2022-04-14T20:56:02Z">April 14, 2022</time>
```

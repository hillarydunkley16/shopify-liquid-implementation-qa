---
title: 'Liquid filters: date'
description: Converts a timestamp into another date format.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/date'
  md: 'https://shopify.dev/docs/api/liquid/filters/date.md'
api_name: liquid
---

# date

```oobleck
string | date: string
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Converts a timestamp into another date format.

The `date` filter accepts the same parameters as Ruby's strftime method for formatting the date. For a list of shorthand formats, refer to the [Ruby documentation](https://ruby-doc.org/core-3.1.1/Time.html#method-i-strftime) or [strftime reference and sandbox](http://www.strfti.me/).

##### Code

```liquid
{{ article.created_at | date: '%B %d, %Y' }}
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
April 14, 2022
```

### The current date

You can apply the `date` filter to the keywords `'now'` and `'today'` to output the current timestamp.

***

**Note:** The timestamp will reflect the time that the Liquid was last rendered. Because of this, the timestamp might not be updated for every page view, depending on the context and caching.

***

##### Code

```liquid
{{ 'now' | date: '%B %d, %Y' }}
```

### format

```oobleck
string | date: format: string
```

Specify a locale-aware date format. You can use the following formats:

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
{{ article.created_at | date: format: 'abbreviated_date' }}
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
Apr 14, 2022
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
{{ article.created_at | date: format: 'month_day_year' }}
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
April 14, 2022
```

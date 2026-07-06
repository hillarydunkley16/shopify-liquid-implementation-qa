---
title: 'Liquid filters: truncate'
description: Truncates a string down to a given number of characters.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/truncate'
  md: 'https://shopify.dev/docs/api/liquid/filters/truncate.md'
api_name: liquid
---

# truncate

```oobleck
string | truncate: number
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Truncates a string down to a given number of characters.

If the specified number of characters is less than the length of the string, then an ellipsis (`...`) is appended to the truncated string. The ellipsis is included in the character count of the truncated string.

##### Code

```liquid
{{ article.title | truncate: 15 }}
```

##### Data

```json
{
  "article": {
    "title": "How to tell if you're out of invisibility potion"
  }
}
```

##### Output

```html
How to tell ...
```

### Specify a custom ellipsis

```oobleck
string | truncate: number, string
```

You can provide a second parameter to specify a custom ellipsis. If you don't want an ellipsis, then you can supply an empty string.

##### Code

```liquid
{{ article.title | truncate: 15, '--' }}
{{ article.title | truncate: 15, '' }}
```

##### Data

```json
{
  "article": {
    "title": "How to tell if you're out of invisibility potion"
  }
}
```

##### Output

```html
How to tell i--
How to tell if
```

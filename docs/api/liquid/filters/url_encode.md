---
title: 'Liquid filters: url_encode'
description: >-
  Converts any URL-unsafe characters in a string to the

  [percent-encoded](https://developer.mozilla.org/en-US/docs/Glossary/percent-encoding)
  equivalent.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/url_encode'
  md: 'https://shopify.dev/docs/api/liquid/filters/url_encode.md'
api_name: liquid
---

# url\_​encode

```oobleck
string | url_encode
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Converts any URL-unsafe characters in a string to the [percent-encoded](https://developer.mozilla.org/en-US/docs/Glossary/percent-encoding) equivalent.

***

**Note:** Spaces are converted to a \<code>+\</code> character, instead of a percent-encoded character.

***

##### Code

```liquid
{{ 'test@test.com' | url_encode }}
```

##### Output

```html
test%40test.com
```

---
title: 'Liquid filters: escape_once'
description: Escapes a string without changing characters that have already been escaped.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/escape_once'
  md: 'https://shopify.dev/docs/api/liquid/filters/escape_once.md'
api_name: liquid
---

# escape\_​once

```oobleck
string | escape_once
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Escapes a string without changing characters that have already been escaped.

##### Code

```liquid
# applying the escape filter to already escaped text escapes characters in HTML entities:

{{ "&lt;p&gt;Text to be escaped.&lt;/p&gt;" | escape }}

# applying the escape_once filter to already escaped text skips characters in HTML entities:

{{ "&lt;p&gt;Text to be escaped.&lt;/p&gt;" | escape_once }}

# use escape_once to escape strings where a combination of HTML entities and non-escaped characters might be present:

{{ "&lt;p&gt;Text to be escaped.&lt;/p&gt; & some additional text" | escape_once }}
```

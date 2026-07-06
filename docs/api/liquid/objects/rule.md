---
title: 'Liquid objects: rule'
description: >-
  A rule for the `robots.txt` file, which tells crawlers which pages can, or
  can't, be accessed.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/rule'
  md: 'https://shopify.dev/docs/api/liquid/objects/rule.md'
api_name: liquid
---

# rule

A rule for the `robots.txt` file, which tells crawlers which pages can, or can't, be accessed.

A rule consists of a directive, which can be either `Allow` or `Disallow`, and a value of the associated URL path.

For example:

```
Disallow: /policies/
```

You can output a rule directly, instead of referencing each of its properties.

***

**Tip:** You can \<a href="/themes/seo/robots-txt">customize the \<code>robots.txt\</code> file\</a> with the \<a href="/themes/architecture/templates/robots-txt-liquid">\<code>robots.txt.liquid\</code> template\</a>.

***

## Properties

* * **directive**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The directive of the rule.

  * **value**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The value of the rule.

##### Example

```json
{
  "directive": "Disallow",
  "value": "/*preview_script_id*"
}
```

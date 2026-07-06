---
title: 'Liquid objects: group'
description: A group of rules for the `robots.txt` file.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/group'
  md: 'https://shopify.dev/docs/api/liquid/objects/group.md'
api_name: liquid
---

# group

A group of rules for the `robots.txt` file.

***

**Tip:** You can \<a href="/themes/seo/robots-txt">customize the \<code>robots.txt\</code> file\</a> with the \<a href="/themes/architecture/templates/robots-txt-liquid">\<code>robots.txt.liquid\</code> template\</a>.

***

## Properties

* * **rules**

    array of [rule](https://shopify.dev/docs/api/liquid/objects/rule)

  * The rules in the group.

  * **sitemap**

    [sitemap](https://shopify.dev/docs/api/liquid/objects/sitemap)

  * The sitemap for the group.

    If the group doesn't require a sitemap, then `blank` is returned.

    The sitemap can be accessed at `/sitemap.xml`.

  * **user\_​agent**

    [user\_agent](https://shopify.dev/docs/api/liquid/objects/user_agent)

  * The user agent for the group.

##### Example

```json
{
  "rules": [],
  "sitemap": {},
  "user_agent": {}
}
```

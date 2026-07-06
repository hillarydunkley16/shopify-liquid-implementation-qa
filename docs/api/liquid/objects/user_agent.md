---
title: 'Liquid objects: user_agent'
description: >-
  The user-agent, which is the name of the crawler, for a specific group in the
  [`robots.txt` file](/themes/architecture/templates/robots-txt-liquid).
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/user_agent'
  md: 'https://shopify.dev/docs/api/liquid/objects/user_agent.md'
api_name: liquid
---

# user\_​agent

The user-agent, which is the name of the crawler, for a specific group in the [`robots.txt` file](https://shopify.dev/themes/architecture/templates/robots-txt-liquid).

The `user_agent` object consists of a `User-agent` directive, and a value of the name of the user-agent. For example:

```
User-agent: *
```

***

**Tip:** You can \<a href="/themes/seo/robots-txt">customize the \<code>robots.txt\</code> file\</a> with the \<a href="/themes/architecture/templates/robots-txt-liquid">\<code>robots.txt.liquid\</code> template\</a>.

***

## Properties

* * **directive**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * Returns `User-agent`.

  * **value**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The name of the user-agent.

##### Example

```json
{
  "directive": "User-agent",
  "value": "*"
}
```

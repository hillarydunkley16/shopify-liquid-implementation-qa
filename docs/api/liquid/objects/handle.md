---
title: 'Liquid objects: handle'
description: >-
  The [handle](/docs/api/liquid/basics#handles) of the resource associated with
  the current template.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/handle'
  md: 'https://shopify.dev/docs/api/liquid/objects/handle.md'
api_name: liquid
---

# handle

The [handle](https://shopify.dev/docs/api/liquid/basics#handles) of the resource associated with the current template.

The `handle` object will return a value only when the following templates are being viewed:

* [article](https://shopify.dev/themes/architecture/templates/article)
* [blog](https://shopify.dev/themes/architecture/templates/blog)
* [collection](https://shopify.dev/themes/architecture/templates/collection)
* [page](https://shopify.dev/themes/architecture/templates/page)
* [product](https://shopify.dev/themes/architecture/templates/product)

If none of the above templates are being viewed, then `nil` is returned.

### Directly accessible in

* Global

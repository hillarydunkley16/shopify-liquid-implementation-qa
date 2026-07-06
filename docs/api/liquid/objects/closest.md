---
title: 'Liquid objects: closest'
description: >-
  A drop that holds resources of different types that are the closest to the
  current context
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/closest'
  md: 'https://shopify.dev/docs/api/liquid/objects/closest.md'
api_name: liquid
---

# closest

A drop that holds resources of different types that are the closest to the current context

This drop is used to hold resources of different types that are the closest to the current context. These resources can be of type `product`, `collection`, `article`, `blog`, `page`, or `metaobject`. The resources of different types within the closest drop can be:

* The currently rendered section or theme block resource setting of the same type
* The currently rendered theme block's ancestor resource setting of the same type
* The currently rendered template resource of the same type
* Assigned via {% content\_for %} tag

***

**Tip:** To learn about how closest drop in theme settings can be used, refer to \<a href="/storefronts/themes/architecture/blocks/theme-blocks/dynamic-sources#accessing-the-closest-resource">Dynamic sources\</a>.

***

## Properties

* * **article**

    [article](https://shopify.dev/docs/api/liquid/objects/article)

  * Closest article resource

    The article resource that is the closest to the current context.

  * **blog**

    [blog](https://shopify.dev/docs/api/liquid/objects/blog)

  * Closest blog resource

    The blog resource that is the closest to the current context.

  * **collection**

    [collection](https://shopify.dev/docs/api/liquid/objects/collection)

  * Closest collection resource

    The collection resource that is the closest to the current context.

  * **metaobject**

    [metaobject](https://shopify.dev/docs/api/liquid/objects/metaobject)

  * Closest metaobject resources

    The metaobject resources that are the closest to the current context.

  * **page**

    [page](https://shopify.dev/docs/api/liquid/objects/page)

  * Closest page resource

    The page resource that is the closest to the current context.

  * **product**

    [product](https://shopify.dev/docs/api/liquid/objects/product)

  * Closest product resource

    The product resource that is the closest to the current context.

### Directly accessible in

* Global

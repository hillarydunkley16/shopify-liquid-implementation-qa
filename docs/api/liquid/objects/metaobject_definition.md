---
title: 'Liquid objects: metaobject_definition'
description: >-
  A `metaobject_definition` defines the structure of a metaobject type for the
  store, which consists of

  a merchant-defined set of [field
  definitions](https://help.shopify.com/en/manual/metafields/metafield-definitions).
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/metaobject_definition'
  md: 'https://shopify.dev/docs/api/liquid/objects/metaobject_definition.md'
api_name: liquid
---

# metaobject\_​definition

A `metaobject_definition` defines the structure of a metaobject type for the store, which consists of a merchant-defined set of [field definitions](https://help.shopify.com/en/manual/metafields/metafield-definitions).

One or more corresponding [`metaobject`](https://shopify.dev/docs/api/liquid/objects#metaobject) objects contain values for the fields specified in the metaobject definition.

***

**Note:** When looping through metaobjects by accessing them using individual handles (e.g., \<code>metaobjects.TYPE\[handle]\</code>), you\&#39;re limited to 20 unique handles per page and can\&#39;t use \<a href="/docs/api/liquid/tags/paginate">pagination\</a>. To iterate over more metaobjects, instead use the \<code>values\</code> property, which supports pagination up to 250 entries per page.

***

## Properties

* * **values**

    array of [metaobject](https://shopify.dev/docs/api/liquid/objects/metaobject)

  * The [metaobjects](https://shopify.dev/docs/api/liquid/objects#metaobject) that follow the definition.

  * **values\_​count**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The total number of entries for the metaobject definition.

### Loop over entries of a metaobject definition

If a metaobject definition has multiple metaobject entries, then you can loop over them using the `values` property. You can loop over a maximum of 50 entries in a metaobject definition. For example, you can display the field `author` for each metaobject using the following `forloop`:

```liquid
{% for testimonial in metaobjects.testimonials.values %}
  {{ testimonial.author.value }}
{% endfor %}
```

***

**Note:** When the \<a href="/apps/data-extensions/metaobjects/capabilities">\<code>publishable\</code> capability\</a> is enabled, loops return only metaobjects with a status of \<code>active\</code>. Metaobjects with a status of \<code>draft\</code> are skipped.

***

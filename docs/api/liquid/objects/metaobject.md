---
title: 'Liquid objects: metaobject'
description: >-
  A metaobject entry, which includes the values for a set of
  [fields](/docs/api/liquid/objects#metafield).

  The set is defined by the parent
  [`metaobject_definition`](/docs/api/liquid/objects#metaobject_definition).
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/metaobject'
  md: 'https://shopify.dev/docs/api/liquid/objects/metaobject.md'
api_name: liquid
---

# metaobject

A metaobject entry, which includes the values for a set of [fields](https://shopify.dev/docs/api/liquid/objects#metafield). The set is defined by the parent [`metaobject_definition`](https://shopify.dev/docs/api/liquid/objects#metaobject_definition).

## Properties

* * **system**

    [metaobject\_system](https://shopify.dev/docs/api/liquid/objects/metaobject_system)

  * Basic information about the metaobject. These properties are grouped under the `system` object to avoid collisions between system property names and user-defined metaobject fields.

### Directly accessible in

* [metaobject](https://shopify.dev/themes/architecture/templates/metaobject)

### Returned by

* [metaobjects](https://shopify.dev/docs/api/liquid/objects/metaobjects)

### Access metaobjects individually

The access path for a metaobject consists of two layers:

* type - The type of the parent metaobject definition.
* handle - The unique [handle](https://shopify.dev/docs/api/liquid/basics#handles) of the metaobject.

Given this, you can access a metaobject with the following syntax:

```liquid
{{ metaobjects.type.handle }}
```

You can also use square bracket notation:

```liquid
{{ metaobjects['type']['handle'] }}
```

A metaobjects's field values can be accessed using the key of the desired field:

```liquid
{{ metaobjects.testimonials.homepage.title }}
{{ metaobjects['highlights']['washable'].image.value }}
```

***

**Note:** When the \<a href="/apps/data-extensions/metaobjects/capabilities">\<code>publishable\</code> capability\</a> is enabled, a metaobject can only be accessed if its status is \<code>active\</code>. If its status is \<code>draft\</code>, then the return value is \<code>nil\</code>.

***

### Usage in metaobject templates

Within a metaobject template, the `metaobject` Liquid object represents the metaobject drop being rendered by the template. You can access it directly as `{{ metaobject }}`.

Here's a basic example of accessing a field within the associated metaobject template:

```liquid
{{ metaobject.title.value }}
```

In this example, replace `title` with the key of the field you want to access. This will output the value of that field for the current metaobject.

## Templates using metaobject

[Theme architecture](https://shopify.dev/themes/architecture/templates/metaobject)

[metaobject template](https://shopify.dev/themes/architecture/templates/metaobject)

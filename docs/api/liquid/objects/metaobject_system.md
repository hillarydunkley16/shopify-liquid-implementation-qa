---
title: 'Liquid objects: metaobject_system'
description: >-
  Basic information about a [`metaobject`](/api/liquid/objects#metaobject).
  These properties are grouped under the `system` object to avoid collisions
  between system property names and user-defined metaobject fields.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/metaobject_system'
  md: 'https://shopify.dev/docs/api/liquid/objects/metaobject_system.md'
api_name: liquid
---

# metaobject\_​system

Basic information about a [`metaobject`](https://shopify.dev/api/liquid/objects#metaobject). These properties are grouped under the `system` object to avoid collisions between system property names and user-defined metaobject fields.

## Properties

* * **handle**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The unique [handle](https://shopify.dev/api/liquid/basics#handles) of the metaobject.

  * **id**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The ID of the metaobject.

  * **type**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The type of the metaobject definition.

    This is a free-form string that's defined when the metaobject definition is created.

  * **url**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The relative URL of the metaobject.

    Only set for metaobjects that have the `online_store` capability.

### Returned by

* [metaobject.system](https://shopify.dev/docs/api/liquid/objects/metaobject#metaobject-system)

### Using the `metaobject_system` object

You can access the `metaobject_system` object and its properties through the metaobject's `system` property. You can use the following syntax:

```liquid
{{ metaobjects.testimonials["home_page"].system.id }}
```

You can also access `metaobject_system` properties when iterating over a list of metaobjects:

```liquid
{% for metaobject in product.metafields.custom.mixed_metaobject_list.value %}
  {% if metaobject.system.type == "testimonial" %}
    {% render 'testimonial' with metaobject as testimonial  %}
  {% else %}
    {{ metaobject.system.handle }}
  {% endif %}
{% endfor %}
```

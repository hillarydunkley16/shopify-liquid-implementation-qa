---
title: 'Liquid objects: predictive_search_resources'
description: >-
  Contains arrays of objects for each resource type that can be returned by a
  [predictive search
  query](/api/ajax/reference/predictive-search#get-locale-search-suggest).
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/predictive_search_resources'
  md: 'https://shopify.dev/docs/api/liquid/objects/predictive_search_resources.md'
api_name: liquid
---

# predictive\_​search\_​resources

Contains arrays of objects for each resource type that can be returned by a [predictive search query](https://shopify.dev/api/ajax/reference/predictive-search#get-locale-search-suggest).

You can check whether any resources of a specific type were returned using the [`size` filter](https://shopify.dev/docs/api/liquid/filters/size).

```liquid
{% if predictive_search.resources.articles.size > 0 %}
  {% for article in predictive_search.resources.articles %}
    {{ article.title }}
  {% endfor %}
{% endif %}
```

## Properties

* * **articles**

    array of [article](https://shopify.dev/docs/api/liquid/objects/article)

  * The articles associated with the query.

  * **collections**

    array of [collection](https://shopify.dev/docs/api/liquid/objects/collection)

  * The collections associated with the query.

  * **pages**

    array of [page](https://shopify.dev/docs/api/liquid/objects/page)

  * The pages associated with the query.

  * **products**

    array of [product](https://shopify.dev/docs/api/liquid/objects/product)

  * The products associated with the query.

##### Example

```json
{
  "articles": [],
  "collections": [],
  "pages": [],
  "products": []
}
```

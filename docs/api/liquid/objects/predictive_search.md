---
title: 'Liquid objects: predictive_search'
description: >-
  Information about the results from a predictive search query through the

  [Predictive Search
  API](/api/ajax/reference/predictive-search#get-locale-search-suggest).
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/predictive_search'
  md: 'https://shopify.dev/docs/api/liquid/objects/predictive_search.md'
api_name: liquid
---

# predictive\_​search

Information about the results from a predictive search query through the [Predictive Search API](https://shopify.dev/api/ajax/reference/predictive-search#get-locale-search-suggest).

***

**Note:** The \<code>\<span class="PreventFireFoxApplyingGapToWBR">predictive\<wbr/>\_search\</span>\</code> object returns results only when rendered in a section using the Predictive Search API and the \<a href="/api/section-rendering">Section Rendering API\</a>. To learn about how to include predictive search in your theme, refer to \<a href="/themes/navigation-search/search/predictive-search">Add predictive search to your theme\</a>.

***

## Properties

* * **performed**

    [boolean](https://shopify.dev/docs/api/liquid/basics#boolean)

  * Returns `true` when being referenced inside a section that's been rendered using the Predictive Search API and the Section Rendering API. Returns `false` if not.

  * **resources**

    [predictive\_search\_resources](https://shopify.dev/docs/api/liquid/objects/predictive_search_resources)

  * The resources associated with the query.

    You can check whether any resources of a specific type were returned using the [`size` filter](https://shopify.dev/docs/api/liquid/filters/size).

    ```liquid
    {% if predictive_search.resources.articles.size > 0 %}
      {% for article in predictive_search.resources.articles %}
        {{ article.title }}
      {% endfor %}
    {% endif %}
    ```

  * **terms**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The entered search terms.

    **Tip:** Use the \<a href="/docs/api/liquid/filters/highlight">\<code>highlight\</code> filter\</a> to highlight the search terms in search results content.

  * **types**

    array of [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The object types that the search was performed on.

    Searches can be performed on the following object types:

    * [`article`](https://shopify.dev/docs/api/liquid/objects/article)
    * [`collection`](https://shopify.dev/docs/api/liquid/objects/collection)
    * [`page`](https://shopify.dev/docs/api/liquid/objects/page)
    * [`product`](https://shopify.dev/docs/api/liquid/objects/product)

    **Note:** The types are determined by the \<a href="/api/ajax/reference/predictive-search#query-parameters">\<code>type\</code> query parameter\</a>.

##### Example

```json
{
  "performed": true,
  "resources": {},
  "terms": "potion",
  "types": []
}
```

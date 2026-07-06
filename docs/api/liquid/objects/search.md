---
title: 'Liquid objects: search'
description: Information about a storefront search query.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/search'
  md: 'https://shopify.dev/docs/api/liquid/objects/search.md'
api_name: liquid
---

# search

Information about a storefront search query.

To learn about storefront search and how to include it in your theme, refer to [Storefront search](https://shopify.dev/themes/navigation-search/search).

## Properties

* * **default\_​sort\_​by**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The default sort order of the search results, which is `relevance`.

  * **filters**

    array of [filter](https://shopify.dev/docs/api/liquid/objects/filter)

  * The filters that have been set up on the search page.

    Only filters that are relevant to the current search results are returned. If the search results contain more than 1000 products, then the array will be empty.

    **Tip:** To learn about how to set up filters in the admin, visit the \<a href="https://help.shopify.com/manual/online-store/themes/customizing-themes/storefront-filters">Shopify Help Center\</a>.

  * **performed**

    [boolean](https://shopify.dev/docs/api/liquid/basics#boolean)

  * Returns `true` if a search was successfully performed. Returns `false` if not.

  * **results**

  * The search result items.

    An item can be an [`article`](https://shopify.dev/docs/api/liquid/objects/article), a [`page`](https://shopify.dev/docs/api/liquid/objects/page), or a [`product`](https://shopify.dev/docs/api/liquid/objects/product).

    **Tip:** Use the \<a href="/docs/api/liquid/tags/paginate">paginate\</a> tag to choose how many results to show per page, up to a limit of 50.

    ExampleSearch result `object_type`

    Search results have an additional `object_type` property that returns the object type of the result.

    ##### Code

    ```liquid
    {% for item in search.results %}
    <!-- Result {{ forloop.index }}-->
    <h3>
      {{ item.title | link_to: item.url }}
    </h3>

    {% if item.object_type == 'article' -%}
      {%- comment -%}
         'item' is an article
         All article object properties can be accessed.
      {%- endcomment -%}

      {% if item.image -%}
        <div class="result-image">
          <a href="{{ item.url }}" title="{{ item.title | escape }}">
            {{ item | image_url: width: 100 | image_tag }}
           </a>
        </div>
       {% endif %}
    {%- elsif item.object_type == 'page' -%}
      {%- comment -%}
        'item' is a page.
         All page object properties can be accessed.
      {%- endcomment -%}
    {%- else -%}
      {%- comment -%}
         'item' is a product.
         All product object properties can be accessed.
      {%- endcomment -%}

      {%- if item.featured_image -%}
        <div class="result-image">
           <a href="{{ item.url }}" title="{{ item.title | escape }}">
             {{ item.featured_image | image_url: width: 100 | image_tag }}
          </a>
        </div>
      {% endif %}
    {%- endif -%}

    <span>{{ item.content | strip_html | truncatewords: 40 | highlight: search.terms }}</span>
    {% endfor %}
    ```

  * **results\_​count**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The number of results.

  * **sort\_​by**

  * The sort order of the search results. This is determined by the `sort_by` URL parameter.

    If there's no `sort_by` URL parameter, then the value is `nil`.

  * **sort\_​options**

    array of [sort\_option](https://shopify.dev/docs/api/liquid/objects/sort_option)

  * The available sorting options for the search results.

    ExampleOutput the sort options

    ##### Code

    ```liquid
    {%- assign sort_by = search.sort_by | default: search.default_sort_by -%}

    <select>
    {%- for option in search.sort_options %}
      <option
        value="{{ option.value }}"
        {%- if option.value == sort_by %}
          selected="selected"
        {%- endif %}
      >
        {{ option.name }}
      </option>
    {% endfor -%}
    </select>
    ```

  * **terms**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The entered search terms.

    **Tip:** Use the \<a href="/docs/api/liquid/filters/highlight">\<code>highlight\</code> filter\</a> to highlight the search terms in search result content.

  * **types**

    array of [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The object types that the search was performed on.

    A search can be performed on the following object types:

    * [`article`](https://shopify.dev/docs/api/liquid/objects/article)
    * [`page`](https://shopify.dev/docs/api/liquid/objects/page)
    * [`product`](https://shopify.dev/docs/api/liquid/objects/product)

    **Note:** The types are determined by the \<a href="/api/ajax/reference/predictive-search#query-parameters">\<code>type\</code> query parameter\</a>.

##### Example

```json
{
  "default_sort_by": "relevance",
  "filters": {},
  "performed": true,
  "results": [],
  "results_count": 18,
  "sort_by": "relevance",
  "sort_options": [],
  "terms": "potion",
  "types": [
    "article",
    "page",
    "product"
  ]
}
```

## Templates using search

[Theme architecture](https://shopify.dev/themes/architecture/templates/search)

[search template](https://shopify.dev/themes/architecture/templates/search)

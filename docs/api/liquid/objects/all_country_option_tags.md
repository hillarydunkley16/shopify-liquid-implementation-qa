---
title: 'Liquid objects: all_country_option_tags'
description: Creates an `<option>` tag for each country.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/all_country_option_tags'
  md: 'https://shopify.dev/docs/api/liquid/objects/all_country_option_tags.md'
api_name: liquid
---

# all\_​country\_​option\_​tags

Creates an `<option>` tag for each country.

An attribute called `data-provinces` is set for each `<option>`, and contains a JSON-encoded array of the country or region's subregions. If a country doesn't have any subregions, then an empty array is set for its `data-provinces` attribute.

***

**Tip:** To return only the countries and regions included in the store\&#39;s shipping zones, use the \<a href="/docs/api/liquid/objects/country\_option\_tags">\<code>\<span class="PreventFireFoxApplyingGapToWBR">country\<wbr/>\_option\<wbr/>\_tags\</span>\</code> object\</a>.

***

### Directly accessible in

* Global

You can wrap the `all_country_option_tags` object in `<select>` tags to build a country option selector.

```liquid
<select name="country">
  {{ all_country_option_tags }}
</select>
```

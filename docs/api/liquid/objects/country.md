---
title: 'Liquid objects: country'
description: A country supported by the store's localization options.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/country'
  md: 'https://shopify.dev/docs/api/liquid/objects/country.md'
api_name: liquid
---

# country

A country supported by the store's localization options.

To learn how to use the `country` object to offer localization options in your theme, refer to [Support multiple currencies and languages](https://shopify.dev/themes/internationalization/multiple-currencies-languages).

## Properties

* * **available\_​languages**

    array of [shop\_locale](https://shopify.dev/docs/api/liquid/objects/shop_locale)

  * The languages that have been added to the market that this country belongs to.

  * **continent**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The continent that the country is in.

    Possible values are `Africa`, `Asia`, `Central America`, `Europe`, `North America`, `Oceania`, and `South America`.

  * **currency**

    [currency](https://shopify.dev/docs/api/liquid/objects/currency)

  * The currency used in the country.

  * **iso\_​code**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The ISO code of the country in [ISO 3166-1 (alpha 2) format](https://www.iso.org/glossary-for-iso-3166.html).

  * **market**

    [market](https://shopify.dev/docs/api/liquid/objects/market)

  * The market that includes this country.

  * **name**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The name of the country.

  * **popular?**

    [boolean](https://shopify.dev/docs/api/liquid/basics#boolean)

  * Returns `true` if the country is popular for this shop. Otherwise, returns `false`. This can be useful for sorting countries in a country selector.

  * **unit\_​system**

    [string](https://shopify.dev/docs/api/liquid/basics#string) from a set of values

  * The unit system of the country.

    | Possible values |
    | - |
    | imperial |
    | metric |

##### Example

```json
{
  "available_languages": [],
  "continent": "North America",
  "currency": {},
  "iso_code": "CA",
  "market": {},
  "name": "Canada",
  "popular?": false,
  "unit_system": "metric"
}
```

### Referencing the `country` object directly

When the country object is referenced directly, `country.name` is returned.

##### Code

```liquid
{% for country in localization.available_countries -%}
  {{ country }}
{%- endfor %}
```

##### Data

```json
{
  "localization": {
    "available_countries": [
      "Afghanistan",
      "Australia",
      "Austria",
      "Belgium",
      "Canada",
      "Czechia",
      "Denmark",
      "Finland",
      "France",
      "Germany",
      "Hong Kong SAR",
      "Ireland",
      "Israel",
      "Italy",
      "Japan",
      "Malaysia",
      "Netherlands",
      "New Zealand",
      "Norway",
      "Poland",
      "Portugal",
      "Singapore",
      "South Korea",
      "Spain",
      "Sweden",
      "Switzerland",
      "United Arab Emirates",
      "United Kingdom",
      "United States"
    ]
  }
}
```

##### Output

```html
Afghanistan
Australia
Austria
Belgium
Canada
Czechia
Denmark
Finland
France
Germany
Hong Kong SAR
Ireland
Israel
Italy
Japan
Malaysia
Netherlands
New Zealand
Norway
Poland
Portugal
Singapore
South Korea
Spain
Sweden
Switzerland
United Arab Emirates
United Kingdom
United States
```

### Rendering a flag image

When the country object is passed to the [`image_url`](https://shopify.dev/docs/api/liquid/filters#image_url) filter, a [CDN URL](https://shopify.dev/themes/best-practices/performance/platform#shopify-cdn) for that country’s flag is returned. All country’s flags are SVGs, normalized to an aspect ratio of 4:3.

##### Code

```liquid
{{ localization.country | image_url: width: 32 | image_tag }}
```

##### Data

```json
{
  "localization": {
    "country": "Canada"
  }
}
```

##### Output

```html
<img src="//cdn.shopify.com/static/images/flags/ca.svg?width=32" alt="Canada" srcset="//cdn.shopify.com/static/images/flags/ca.svg?width=32 32w" width="32" height="24">
```

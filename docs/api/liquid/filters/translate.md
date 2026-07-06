---
title: 'Liquid filters: translate'
description: >-
  Returns a string of translated text for a given translation key from a [locale
  file](/themes/architecture/locales).
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/translate'
  md: 'https://shopify.dev/docs/api/liquid/filters/translate.md'
api_name: liquid
---

# translate

```oobleck
string | t
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Returns a string of translated text for a given translation key from a [locale file](https://shopify.dev/themes/architecture/locales).

The `translate` filter has an alias of `t`, which is more commonly used.

***

**Tip:** To learn more about using the \<code>t\</code> filter, refer to \<a href="/themes/architecture/locales/storefront-locale-files#usage">storefront locale file usage\</a> or \<a href="/themes/architecture/locales/schema-locale-files#usage">schema locale file usage\</a>.

***

### Section locales vs. theme locales

The `t` filter can also reference keys defined in the [`locales` object](https://shopify.dev/themes/architecture/sections/section-schema#locales) of section file's `schema` tag. Content that you put in the `schema` under the `locales` object is only accessible to that section. This is useful if you need to make a standalone section that you want to share between themes.

Content that is global to a theme should be placed in the theme's `locales` directory. For example, you could include the expression "See more" in your `locales` directory to create a single translation. You could then use the translation in a blog post and on the product details page.

***

**Note:** Translations in the section\&#39;s \<code>schema\</code> tag that aren\&#39;t part of the \<code>locales\</code> object are used for merchant-facing text shown in the theme editor. These translations don\&#39;t use the \<code>t\</code> filter.

***

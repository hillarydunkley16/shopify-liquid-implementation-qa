---
title: 'Liquid filters: currency_selector'
description: >-
  Generates an HTML `<select>` element with an option for each currency
  available on the store.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/currency_selector'
  md: 'https://shopify.dev/docs/api/liquid/filters/currency_selector.md'
api_name: liquid
---

# currency\_​selector

```oobleck
form | currency_selector
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Generates an HTML `<select>` element with an option for each currency available on the store.

The `currency_selector` filter must be applied to the [`form` object](https://shopify.dev/docs/api/liquid/objects/form) within a [currency form](https://shopify.dev/docs/api/liquid/tags/form#form-currency).

**Deprecated:**

Deprecated without a direct replacement because the [currency form](https://shopify.dev/docs/api/liquid/tags/form#form-currency) has also been deprecated. The currency form was replaced by the [localization form](https://shopify.dev/docs/api/liquid/tags/form#form-localization). Refer to this guide which explains [how to create a country selector](https://shopify.dev/docs/themes/markets/multiple-currencies-languages#implementing-country-and-language-selectors) using the localization form.

##### Code

```liquid
{% form 'currency' %}
  {{ form | currency_selector }}
{% endform %}
```

##### Output

```html
<form method="post" action="/cart/update" id="currency_form" accept-charset="UTF-8" class="shopify-currency-form" enctype="multipart/form-data"><input type="hidden" name="form_type" value="currency" /><input type="hidden" name="utf8" value="✓" /><input type="hidden" name="return_to" value="/services/liquid_rendering/resource" />
  <select name="currency"><option value="AED">AED د.إ</option><option value="AFN">AFN ؋</option><option value="AUD">AUD $</option><option value="CAD" selected="selected">CAD $</option><option value="CHF">CHF CHF</option><option value="CZK">CZK Kč</option><option value="DKK">DKK kr.</option><option value="EUR">EUR €</option><option value="GBP">GBP £</option><option value="HKD">HKD $</option><option value="ILS">ILS ₪</option><option value="JPY">JPY ¥</option><option value="KRW">KRW ₩</option><option value="MYR">MYR RM</option><option value="NZD">NZD $</option><option value="PLN">PLN zł</option><option value="SEK">SEK kr</option><option value="SGD">SGD $</option><option value="USD">USD $</option></select>
</form>
```

### class

```oobleck
form | currency_selector: class: string
```

Specify the `class` attribute of the `<select>` element.

##### Code

```liquid
{% form 'currency' %}
  {{ form | currency_selector: class: 'custom-class' }}
{% endform %}
```

##### Output

```html
<form method="post" action="/cart/update" id="currency_form" accept-charset="UTF-8" class="shopify-currency-form" enctype="multipart/form-data"><input type="hidden" name="form_type" value="currency" /><input type="hidden" name="utf8" value="✓" /><input type="hidden" name="return_to" value="/services/liquid_rendering/resource" />
  <select class="custom-class" name="currency"><option value="AED">AED د.إ</option><option value="AFN">AFN ؋</option><option value="AUD">AUD $</option><option value="CAD" selected="selected">CAD $</option><option value="CHF">CHF CHF</option><option value="CZK">CZK Kč</option><option value="DKK">DKK kr.</option><option value="EUR">EUR €</option><option value="GBP">GBP £</option><option value="HKD">HKD $</option><option value="ILS">ILS ₪</option><option value="JPY">JPY ¥</option><option value="KRW">KRW ₩</option><option value="MYR">MYR RM</option><option value="NZD">NZD $</option><option value="PLN">PLN zł</option><option value="SEK">SEK kr</option><option value="SGD">SGD $</option><option value="USD">USD $</option></select>
</form>
```

### id

```oobleck
form | currency_selector: id: string
```

Specify the `id` attribute of the `<select>` element.

##### Code

```liquid
{% form 'currency' %}
  {{ form | currency_selector: id: 'custom-id' }}
{% endform %}
```

##### Output

```html
<form method="post" action="/cart/update" id="currency_form" accept-charset="UTF-8" class="shopify-currency-form" enctype="multipart/form-data"><input type="hidden" name="form_type" value="currency" /><input type="hidden" name="utf8" value="✓" /><input type="hidden" name="return_to" value="/services/liquid_rendering/resource" />
  <select id="custom-id" name="currency"><option value="AED">AED د.إ</option><option value="AFN">AFN ؋</option><option value="AUD">AUD $</option><option value="CAD" selected="selected">CAD $</option><option value="CHF">CHF CHF</option><option value="CZK">CZK Kč</option><option value="DKK">DKK kr.</option><option value="EUR">EUR €</option><option value="GBP">GBP £</option><option value="HKD">HKD $</option><option value="ILS">ILS ₪</option><option value="JPY">JPY ¥</option><option value="KRW">KRW ₩</option><option value="MYR">MYR RM</option><option value="NZD">NZD $</option><option value="PLN">PLN zł</option><option value="SEK">SEK kr</option><option value="SGD">SGD $</option><option value="USD">USD $</option></select>
</form>
```

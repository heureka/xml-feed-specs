# Price Vat

## Overview

**Element Name:** `PRICE_VAT`<br>
**Type:** string<br>
**Architecture:** Simple<br>
**Required:** Yes<br>

Final product price including VAT in Czech Koruna (CZK). Maximum 2 decimal places.
Supports formats: 25000, 25000.50, 25000,50.


## General Constraints

- **Required field** - must be present in the XML
- **Pattern:** `\d+([.,]\d{1,2})?`

## XML Examples

```xml
<PRICE_VAT>25000</PRICE_VAT>
```

```xml
<PRICE_VAT>25000.50</PRICE_VAT>
```





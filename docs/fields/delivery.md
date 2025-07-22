# Delivery

## Overview

**Element Name:** `DELIVERY`  
**Type:** string  
**Architecture:** Complex conditional  
**Required:** Yes  
**Multiple:** Yes (max 100)  

Shipping method information. Maximum 100 different shipping methods. Must contain DELIVERY_ID and DELIVERY_PRICE when present.


**Validation Rule:** Must be either empty or contain both DELIVERY_ID and DELIVERY_PRICE

### Child Elements

#### DELIVERY_ID

- **Type:** string
- **Required:** Yes (when parent has content)
- **Description:** Predefined carrier code from the approved delivery methods list.

- **Allowed Values:** CESKA_POSTA, CESKA_POSTA_DOPORUCENA_ZASILKA, CSAD_LOGISTIK_OSTRAVA, DPD, DHL, DSV, FOFR, GEBRUDER_WEISS, GEIS, GLS, HDS, PPL, SEEGMULLER, TNT, TOPTRANS, UPS, FEDEX, RABEN_LOGISTICS, ZASILKOVNA_NA_ADRESU, 123KURIER, WEDO_HOME, RHENUS_LOGISTICS, MESSENGER, ZASILKOVNA, DPD_PICKUP, BALIKOVNA_DEPOTAPI, WEDO_POINT, CESKA_POSTA_NAPOSTU, PPL_PARCELSHOP, GLS_PARCELSHOP, ALZAPOINT, DPD_BOX, Z_BOX, WEDO_BOX, PPL_PARCELBOX, BALIKOVNA_BOX, ALZABOX, ONLINE, VLASTNI_PREPRAVA
- **Examples:** PPL

#### DELIVERY_PRICE

- **Type:** string
- **Required:** Yes (when parent has content)
- **Description:** Delivery price for prepayment orders. Numeric value with optional decimal places.

- **Pattern:** `\d+([.,]\d{1,2})?`
- **Examples:** 99.5

#### DELIVERY_PRICE_COD

- **Type:** string
- **Required:** No (when parent has content)
- **Description:** Delivery price for cash on delivery orders. Optional field.

- **Pattern:** `\d+([.,]\d{1,2})?`
- **Examples:** 149


## General Constraints

- **Required field** - must be present in the XML
- **Multiple occurrences** allowed (maximum 100)

## XML Examples

```xml
<DELIVERY>
  <DELIVERY_ID>PPL</DELIVERY_ID>
  <DELIVERY_PRICE>99.5</DELIVERY_PRICE>
  <DELIVERY_PRICE_COD>149</DELIVERY_PRICE_COD>
</DELIVERY>
```





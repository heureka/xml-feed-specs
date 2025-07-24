# Param

## Overview

**Element Name:** `PARAM`<br>
**Type:** string<br>
**Architecture:** Complex conditional<br>
**Required:** No<br>
**Multiple:** Yes<br>
**Validation Rule:** Must be either empty or contain both VAL and PARAM_NAME<br>

Product parameter with name-value pair. Must contain both VAL and PARAM_NAME elements
when present.

### Child Elements

#### VAL

- **Type:** string
- **Required:** Yes (when parent has content)
- **Description:** Parameter value. Must be non-empty.

- **Examples:** 128GB

#### PARAM_NAME

- **Type:** string
- **Required:** Yes (when parent has content)
- **Description:** Parameter name/label. Must be non-empty.

- **Examples:** Storage


## General Constraints

- **Optional field** - can be omitted
- **Multiple occurrences** allowed

## XML Examples

```xml
<PARAM>
  <VAL>128GB</VAL>
  <PARAM_NAME>Storage</PARAM_NAME>
</PARAM>
```





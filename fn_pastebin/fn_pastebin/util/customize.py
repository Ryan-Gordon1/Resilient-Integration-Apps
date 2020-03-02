# (c) Copyright IBM Corp. 2018. All Rights Reserved.
# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_pastebin"""

from __future__ import print_function
from resilient_circuits.util import *


def customization_data(client=None):
    """Produce any customization definitions (types, fields, message destinations, etc)
       that should be installed by `resilient-circuits customize`
    """

    # This import data contains:
    #   Function inputs:
    #     pastebin_code
    #     pastebin_expiration
    #     pastebin_format
    #     pastebin_name
    #     pastebin_privacy
    #   Message Destinations:
    #     fn_pastebin
    #   Functions:
    #     fn_create_pastebin
    #   Workflows:
    #     example_create_pastebin
    #   Rules:
    #     Create Pastebin


    yield ImportDefinition(u"""
eyJ0YXNrX29yZGVyIjogW10sICJ3b3JrZmxvd3MiOiBbeyJwcm9ncmFtbWF0aWNfbmFtZSI6ICJl
eGFtcGxlX2NyZWF0ZV9wYXN0ZWJpbiIsICJvYmplY3RfdHlwZSI6ICJhcnRpZmFjdCIsICJleHBv
cnRfa2V5IjogImV4YW1wbGVfY3JlYXRlX3Bhc3RlYmluIiwgInV1aWQiOiAiYTE5MGQ4N2UtNzhj
MC00OWNjLWE5MDMtNDdmNjVjMjNlN2RmIiwgImxhc3RfbW9kaWZpZWRfYnkiOiAiYWRtaW5AcmVz
LmNvbSIsICJuYW1lIjogIkV4YW1wbGU6IENyZWF0ZSBQYXN0ZWJpbiIsICJjb250ZW50IjogeyJ4
bWwiOiAiPD94bWwgdmVyc2lvbj1cIjEuMFwiIGVuY29kaW5nPVwiVVRGLThcIj8+PGRlZmluaXRp
b25zIHhtbG5zPVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMvQlBNTi8yMDEwMDUyNC9NT0RFTFwi
IHhtbG5zOmJwbW5kaT1cImh0dHA6Ly93d3cub21nLm9yZy9zcGVjL0JQTU4vMjAxMDA1MjQvRElc
IiB4bWxuczpvbWdkYz1cImh0dHA6Ly93d3cub21nLm9yZy9zcGVjL0RELzIwMTAwNTI0L0RDXCIg
eG1sbnM6b21nZGk9XCJodHRwOi8vd3d3Lm9tZy5vcmcvc3BlYy9ERC8yMDEwMDUyNC9ESVwiIHht
bG5zOnJlc2lsaWVudD1cImh0dHA6Ly9yZXNpbGllbnQuaWJtLmNvbS9icG1uXCIgeG1sbnM6eHNk
PVwiaHR0cDovL3d3dy53My5vcmcvMjAwMS9YTUxTY2hlbWFcIiB4bWxuczp4c2k9XCJodHRwOi8v
d3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYS1pbnN0YW5jZVwiIHRhcmdldE5hbWVzcGFjZT1cImh0
dHA6Ly93d3cuY2FtdW5kYS5vcmcvdGVzdFwiPjxwcm9jZXNzIGlkPVwiZXhhbXBsZV9jcmVhdGVf
cGFzdGViaW5cIiBpc0V4ZWN1dGFibGU9XCJ0cnVlXCIgbmFtZT1cIkV4YW1wbGU6IENyZWF0ZSBQ
YXN0ZWJpblwiPjxkb2N1bWVudGF0aW9uPkFuIEV4YW1wbGUgV29ya2Zsb3cgdGhhdCBzaG93cyBo
b3cgdG8gY3JlYXRlIGEgUGFzdGViaW48L2RvY3VtZW50YXRpb24+PHN0YXJ0RXZlbnQgaWQ9XCJT
dGFydEV2ZW50XzE1NWFzeG1cIj48b3V0Z29pbmc+U2VxdWVuY2VGbG93XzFnZG5rbTg8L291dGdv
aW5nPjwvc3RhcnRFdmVudD48c2VydmljZVRhc2sgaWQ9XCJTZXJ2aWNlVGFza18xNjA1ZHgwXCIg
bmFtZT1cIkNyZWF0ZSBQYXN0ZWJpblwiIHJlc2lsaWVudDp0eXBlPVwiZnVuY3Rpb25cIj48ZXh0
ZW5zaW9uRWxlbWVudHM+PHJlc2lsaWVudDpmdW5jdGlvbiB1dWlkPVwiOTViZmU2NmUtZDdlNy00
MDM4LWE1NTctOWY2NTBhNWJkZDUwXCI+e1wiaW5wdXRzXCI6e30sXCJwcmVfcHJvY2Vzc2luZ19z
Y3JpcHRcIjpcIiMgVGhpcyBpcyB0aGUgdGV4dCB0aGF0IHdpbGwgYmUgd3JpdHRlbiBpbnNpZGUg
eW91ciBwYXN0ZVxcbmlucHV0cy5wYXN0ZWJpbl9jb2RlID0gXFxcIlxcXCJcXFwiIGV4YW1wbGUg
Y29kZSBoZXJlIFxcXCJcXFwiXFxcIlxcblxcbiMgVGhpcyB3aWxsIGJlIHRoZSBuYW1lIC8gdGl0
bGUgb2YgeW91ciBwYXN0ZVxcbmlucHV0cy5wYXN0ZWJpbl9uYW1lID0gXFxcIkV4YW1wbGUgTmFt
ZVxcXCJcXG5cXG4jIFRoaXMgd2lsbCBiZSB0aGUgc3ludGF4IGhpZ2hsaWdodGluZyB2YWx1ZS4g
Rm9ybWF0IGNvZGVzLCBzZWUgaGVyZTogaHR0cHM6Ly9wYXN0ZWJpbi5jb20vYXBpXFxuaW5wdXRz
LnBhc3RlYmluX2Zvcm1hdCA9IFxcXCJweXRob25cXFwiXFxuXFxuIyBUaGlzIG1ha2VzIGEgcGFz
dGUgcHVibGljLCB1bmxpc3RlZCBvciBwcml2YXRlLiAoUHVibGljID0gMCwgVW5saXN0ZWQgPSAx
LCBQcml2YXRlID0gMilcXG5pbnB1dHMucGFzdGViaW5fcHJpdmFjeSA9IDJcXG5cXG4jIFRoaXMg
c2V0cyB0aGUgZXhwaXJhdGlvbiBkYXRlIG9mIHlvdXIgcGFzdGUuIEV4cGlyYXRpb24gY29kZXMs
IHNlZSBoZXJlOiBodHRwczovL3Bhc3RlYmluLmNvbS9hcGlcXG5pbnB1dHMucGFzdGViaW5fZXhw
aXJhdGlvbiA9IFxcXCIxSFxcXCJcIixcInJlc3VsdF9uYW1lXCI6XCJcIixcInBvc3RfcHJvY2Vz
c2luZ19zY3JpcHRcIjpcImlmIChyZXN1bHRzLnN1Y2Nlc3MpOlxcbiAgbm90ZVRleHQgPSBcXFwi
XFxcIlxcXCImbHQ7YnImZ3Q7Jmx0O2ImZ3Q7UGFzdGViaW4gQ3JlYXRlZCZsdDsvYiZndDtcXG4g
ICAgICAgICAgICAgICAgJmx0O2ImZ3Q7TmFtZTombHQ7L2ImZ3Q7IHswfVxcbiAgICAgICAgICAg
ICAgICAmbHQ7YiZndDtMaW5rOiZsdDsvYiZndDsgJmx0O2EgaHJlZj0nezF9JyZndDt7MX0mbHQ7
L2EmZ3Q7XFxcIlxcXCJcXFwiLmZvcm1hdChyZXN1bHRzLmlucHV0cy5wYXN0ZWJpbl9uYW1lLCBy
ZXN1bHRzLnBhc3RlYmluX2xpbmspXFxuICBpbmNpZGVudC5hZGROb3RlKGhlbHBlci5jcmVhdGVS
aWNoVGV4dChub3RlVGV4dCkpXCJ9PC9yZXNpbGllbnQ6ZnVuY3Rpb24+PC9leHRlbnNpb25FbGVt
ZW50cz48aW5jb21pbmc+U2VxdWVuY2VGbG93XzFnZG5rbTg8L2luY29taW5nPjxvdXRnb2luZz5T
ZXF1ZW5jZUZsb3dfMDZpZm9nbDwvb3V0Z29pbmc+PC9zZXJ2aWNlVGFzaz48c2VxdWVuY2VGbG93
IGlkPVwiU2VxdWVuY2VGbG93XzFnZG5rbThcIiBzb3VyY2VSZWY9XCJTdGFydEV2ZW50XzE1NWFz
eG1cIiB0YXJnZXRSZWY9XCJTZXJ2aWNlVGFza18xNjA1ZHgwXCIvPjxlbmRFdmVudCBpZD1cIkVu
ZEV2ZW50XzFiZW9hNTNcIj48aW5jb21pbmc+U2VxdWVuY2VGbG93XzA2aWZvZ2w8L2luY29taW5n
PjwvZW5kRXZlbnQ+PHNlcXVlbmNlRmxvdyBpZD1cIlNlcXVlbmNlRmxvd18wNmlmb2dsXCIgc291
cmNlUmVmPVwiU2VydmljZVRhc2tfMTYwNWR4MFwiIHRhcmdldFJlZj1cIkVuZEV2ZW50XzFiZW9h
NTNcIi8+PHRleHRBbm5vdGF0aW9uIGlkPVwiVGV4dEFubm90YXRpb25fMWt4eGl5dFwiPjx0ZXh0
PlN0YXJ0IHlvdXIgd29ya2Zsb3cgaGVyZTwvdGV4dD48L3RleHRBbm5vdGF0aW9uPjxhc3NvY2lh
dGlvbiBpZD1cIkFzc29jaWF0aW9uXzFzZXVqNDhcIiBzb3VyY2VSZWY9XCJTdGFydEV2ZW50XzE1
NWFzeG1cIiB0YXJnZXRSZWY9XCJUZXh0QW5ub3RhdGlvbl8xa3h4aXl0XCIvPjwvcHJvY2Vzcz48
YnBtbmRpOkJQTU5EaWFncmFtIGlkPVwiQlBNTkRpYWdyYW1fMVwiPjxicG1uZGk6QlBNTlBsYW5l
IGJwbW5FbGVtZW50PVwidW5kZWZpbmVkXCIgaWQ9XCJCUE1OUGxhbmVfMVwiPjxicG1uZGk6QlBN
TlNoYXBlIGJwbW5FbGVtZW50PVwiU3RhcnRFdmVudF8xNTVhc3htXCIgaWQ9XCJTdGFydEV2ZW50
XzE1NWFzeG1fZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjM2XCIgd2lkdGg9XCIzNlwiIHg9
XCIxNjJcIiB5PVwiMTg4XCIvPjxicG1uZGk6QlBNTkxhYmVsPjxvbWdkYzpCb3VuZHMgaGVpZ2h0
PVwiMFwiIHdpZHRoPVwiOTBcIiB4PVwiMTU3XCIgeT1cIjIyM1wiLz48L2JwbW5kaTpCUE1OTGFi
ZWw+PC9icG1uZGk6QlBNTlNoYXBlPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVtZW50PVwiVGV4
dEFubm90YXRpb25fMWt4eGl5dFwiIGlkPVwiVGV4dEFubm90YXRpb25fMWt4eGl5dF9kaVwiPjxv
bWdkYzpCb3VuZHMgaGVpZ2h0PVwiMzBcIiB3aWR0aD1cIjEwMFwiIHg9XCI5OVwiIHk9XCIyNTRc
Ii8+PC9icG1uZGk6QlBNTlNoYXBlPjxicG1uZGk6QlBNTkVkZ2UgYnBtbkVsZW1lbnQ9XCJBc3Nv
Y2lhdGlvbl8xc2V1ajQ4XCIgaWQ9XCJBc3NvY2lhdGlvbl8xc2V1ajQ4X2RpXCI+PG9tZ2RpOndh
eXBvaW50IHg9XCIxNjlcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIyMFwiLz48b21n
ZGk6d2F5cG9pbnQgeD1cIjE1M1wiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjU0XCIv
PjwvYnBtbmRpOkJQTU5FZGdlPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVtZW50PVwiU2Vydmlj
ZVRhc2tfMTYwNWR4MFwiIGlkPVwiU2VydmljZVRhc2tfMTYwNWR4MF9kaVwiPjxvbWdkYzpCb3Vu
ZHMgaGVpZ2h0PVwiODBcIiB3aWR0aD1cIjEwMFwiIHg9XCIzMTdcIiB5PVwiMTY2XCIvPjwvYnBt
bmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5FZGdlIGJwbW5FbGVtZW50PVwiU2VxdWVuY2VGbG93
XzFnZG5rbThcIiBpZD1cIlNlcXVlbmNlRmxvd18xZ2Rua204X2RpXCI+PG9tZ2RpOndheXBvaW50
IHg9XCIxOThcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIwNlwiLz48b21nZGk6d2F5
cG9pbnQgeD1cIjMxN1wiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjA2XCIvPjxicG1u
ZGk6QlBNTkxhYmVsPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMTNcIiB3aWR0aD1cIjBcIiB4PVwi
MjU3LjVcIiB5PVwiMTg0XCIvPjwvYnBtbmRpOkJQTU5MYWJlbD48L2JwbW5kaTpCUE1ORWRnZT48
YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIkVuZEV2ZW50XzFiZW9hNTNcIiBpZD1cIkVu
ZEV2ZW50XzFiZW9hNTNfZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjM2XCIgd2lkdGg9XCIz
NlwiIHg9XCI1NTlcIiB5PVwiMTg4XCIvPjxicG1uZGk6QlBNTkxhYmVsPjxvbWdkYzpCb3VuZHMg
aGVpZ2h0PVwiMTNcIiB3aWR0aD1cIjBcIiB4PVwiNTc3XCIgeT1cIjIyN1wiLz48L2JwbW5kaTpC
UE1OTGFiZWw+PC9icG1uZGk6QlBNTlNoYXBlPjxicG1uZGk6QlBNTkVkZ2UgYnBtbkVsZW1lbnQ9
XCJTZXF1ZW5jZUZsb3dfMDZpZm9nbFwiIGlkPVwiU2VxdWVuY2VGbG93XzA2aWZvZ2xfZGlcIj48
b21nZGk6d2F5cG9pbnQgeD1cIjQxN1wiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjA2
XCIvPjxvbWdkaTp3YXlwb2ludCB4PVwiNTU5XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9
XCIyMDZcIi8+PGJwbW5kaTpCUE1OTGFiZWw+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIxM1wiIHdp
ZHRoPVwiMFwiIHg9XCI0ODhcIiB5PVwiMTg0XCIvPjwvYnBtbmRpOkJQTU5MYWJlbD48L2JwbW5k
aTpCUE1ORWRnZT48L2JwbW5kaTpCUE1OUGxhbmU+PC9icG1uZGk6QlBNTkRpYWdyYW0+PC9kZWZp
bml0aW9ucz4iLCAid29ya2Zsb3dfaWQiOiAiZXhhbXBsZV9jcmVhdGVfcGFzdGViaW4iLCAidmVy
c2lvbiI6IDl9LCAid29ya2Zsb3dfaWQiOiA3LCAiYWN0aW9ucyI6IFtdLCAibGFzdF9tb2RpZmll
ZF90aW1lIjogMTU0MDU3NDQ1MDM3NCwgImNyZWF0b3JfaWQiOiAiYWRtaW5AcmVzLmNvbSIsICJk
ZXNjcmlwdGlvbiI6ICJBbiBFeGFtcGxlIFdvcmtmbG93IHRoYXQgc2hvd3MgaG93IHRvIGNyZWF0
ZSBhIFBhc3RlYmluIn1dLCAiYWN0aW9ucyI6IFt7ImxvZ2ljX3R5cGUiOiAiYWxsIiwgIm5hbWUi
OiAiQ3JlYXRlIFBhc3RlYmluIiwgInZpZXdfaXRlbXMiOiBbXSwgInR5cGUiOiAxLCAid29ya2Zs
b3dzIjogWyJleGFtcGxlX2NyZWF0ZV9wYXN0ZWJpbiJdLCAib2JqZWN0X3R5cGUiOiAiYXJ0aWZh
Y3QiLCAidGltZW91dF9zZWNvbmRzIjogODY0MDAsICJ1dWlkIjogImFhM2E1YzE3LTQxZTAtNDk2
Zi05ZGE4LThkMjI1YWVhZTE4ZSIsICJhdXRvbWF0aW9ucyI6IFtdLCAiZXhwb3J0X2tleSI6ICJD
cmVhdGUgUGFzdGViaW4iLCAiY29uZGl0aW9ucyI6IFtdLCAiaWQiOiAyMCwgIm1lc3NhZ2VfZGVz
dGluYXRpb25zIjogW119XSwgImxheW91dHMiOiBbXSwgImV4cG9ydF9mb3JtYXRfdmVyc2lvbiI6
IDIsICJpZCI6IDQsICJpbmR1c3RyaWVzIjogbnVsbCwgInBoYXNlcyI6IFtdLCAiYWN0aW9uX29y
ZGVyIjogW10sICJnZW9zIjogbnVsbCwgInNlcnZlcl92ZXJzaW9uIjogeyJtYWpvciI6IDMwLCAi
dmVyc2lvbiI6ICIzMC4wLjM0NzYiLCAiYnVpbGRfbnVtYmVyIjogMzQ3NiwgIm1pbm9yIjogMH0s
ICJ0aW1lZnJhbWVzIjogbnVsbCwgIndvcmtzcGFjZXMiOiBbXSwgImF1dG9tYXRpY190YXNrcyI6
IFtdLCAiZnVuY3Rpb25zIjogW3siZGlzcGxheV9uYW1lIjogIkNyZWF0ZSBQYXN0ZWJpbiIsICJ1
dWlkIjogIjk1YmZlNjZlLWQ3ZTctNDAzOC1hNTU3LTlmNjUwYTViZGQ1MCIsICJjcmVhdG9yIjog
eyJkaXNwbGF5X25hbWUiOiAiQWRtaW4gVXNlciIsICJ0eXBlIjogInVzZXIiLCAiaWQiOiAzLCAi
bmFtZSI6ICJhZG1pbkByZXMuY29tIn0sICJ2aWV3X2l0ZW1zIjogW3sic2hvd19pZiI6IG51bGws
ICJmaWVsZF90eXBlIjogIl9fZnVuY3Rpb24iLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAi
ZWxlbWVudCI6ICJmaWVsZF91dWlkIiwgImNvbnRlbnQiOiAiMzE4YzE0ZmItM2VkZC00ZDQ4LTg3
N2MtZmNkNTE1ZDM3YTdhIiwgInN0ZXBfbGFiZWwiOiBudWxsfSwgeyJzaG93X2lmIjogbnVsbCwg
ImZpZWxkX3R5cGUiOiAiX19mdW5jdGlvbiIsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2UsICJl
bGVtZW50IjogImZpZWxkX3V1aWQiLCAiY29udGVudCI6ICJhYWE3MjAzNS1hOWQ4LTRmZWUtYWUw
Ni05ZWRhZjE0ZmI4NTciLCAic3RlcF9sYWJlbCI6IG51bGx9LCB7InNob3dfaWYiOiBudWxsLCAi
ZmllbGRfdHlwZSI6ICJfX2Z1bmN0aW9uIiwgInNob3dfbGlua19oZWFkZXIiOiBmYWxzZSwgImVs
ZW1lbnQiOiAiZmllbGRfdXVpZCIsICJjb250ZW50IjogIjNlMzI3YzZkLWFlZDYtNDAyYy04YWQ4
LTgzNzI5Njk3OGRkNSIsICJzdGVwX2xhYmVsIjogbnVsbH0sIHsic2hvd19pZiI6IG51bGwsICJm
aWVsZF90eXBlIjogIl9fZnVuY3Rpb24iLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAiZWxl
bWVudCI6ICJmaWVsZF91dWlkIiwgImNvbnRlbnQiOiAiMGM5NTFjNWEtMTAxYS00MzkzLTg3NDQt
ZDRlZDQ1ZWI2ODRhIiwgInN0ZXBfbGFiZWwiOiBudWxsfSwgeyJzaG93X2lmIjogbnVsbCwgImZp
ZWxkX3R5cGUiOiAiX19mdW5jdGlvbiIsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2UsICJlbGVt
ZW50IjogImZpZWxkX3V1aWQiLCAiY29udGVudCI6ICJjNDhhOWU3Mi05NGJjLTRjY2UtYjBkYy1j
NzdlZWZiMWU4YTkiLCAic3RlcF9sYWJlbCI6IG51bGx9XSwgImV4cG9ydF9rZXkiOiAiZm5fY3Jl
YXRlX3Bhc3RlYmluIiwgImxhc3RfbW9kaWZpZWRfYnkiOiB7ImRpc3BsYXlfbmFtZSI6ICJBZG1p
biBVc2VyIiwgInR5cGUiOiAidXNlciIsICJpZCI6IDMsICJuYW1lIjogImFkbWluQHJlcy5jb20i
fSwgIm5hbWUiOiAiZm5fY3JlYXRlX3Bhc3RlYmluIiwgInZlcnNpb24iOiAzLCAid29ya2Zsb3dz
IjogW3sicHJvZ3JhbW1hdGljX25hbWUiOiAiZXhhbXBsZV9jcmVhdGVfcGFzdGViaW4iLCAib2Jq
ZWN0X3R5cGUiOiAiYXJ0aWZhY3QiLCAidXVpZCI6IG51bGwsICJhY3Rpb25zIjogW10sICJuYW1l
IjogIkV4YW1wbGU6IENyZWF0ZSBQYXN0ZWJpbiIsICJ3b3JrZmxvd19pZCI6IDcsICJkZXNjcmlw
dGlvbiI6IG51bGx9XSwgImxhc3RfbW9kaWZpZWRfdGltZSI6IDE1NDA1Njc2NDIwMTQsICJkZXN0
aW5hdGlvbl9oYW5kbGUiOiAiZm5fcGFzdGViaW4iLCAiaWQiOiA3LCAiZGVzY3JpcHRpb24iOiB7
ImNvbnRlbnQiOiAiRnVuY3Rpb24gdGhhdCBkdW1wcyBhbnkgdGV4dC9jb2RlIHRvIHBhc3RlYmlu
LmNvbSBhbmQgcmV0dXJucyBhIGxpbmsgdG8gdGhhdCBwYXN0ZSIsICJmb3JtYXQiOiAidGV4dCJ9
fV0sICJub3RpZmljYXRpb25zIjogbnVsbCwgInJlZ3VsYXRvcnMiOiBudWxsLCAiaW5jaWRlbnRf
dHlwZXMiOiBbeyJjcmVhdGVfZGF0ZSI6IDE1NDA1NzQ1NzY2NjIsICJkZXNjcmlwdGlvbiI6ICJD
dXN0b21pemF0aW9uIFBhY2thZ2VzIChpbnRlcm5hbCkiLCAiZXhwb3J0X2tleSI6ICJDdXN0b21p
emF0aW9uIFBhY2thZ2VzIChpbnRlcm5hbCkiLCAiaWQiOiAwLCAibmFtZSI6ICJDdXN0b21pemF0
aW9uIFBhY2thZ2VzIChpbnRlcm5hbCkiLCAidXBkYXRlX2RhdGUiOiAxNTQwNTc0NTc2NjYyLCAi
dXVpZCI6ICJiZmVlYzJkNC0zNzcwLTExZTgtYWQzOS00YTAwMDQwNDRhYTAiLCAiZW5hYmxlZCI6
IGZhbHNlLCAic3lzdGVtIjogZmFsc2UsICJwYXJlbnRfaWQiOiBudWxsLCAiaGlkZGVuIjogZmFs
c2V9XSwgInNjcmlwdHMiOiBbXSwgInR5cGVzIjogW10sICJtZXNzYWdlX2Rlc3RpbmF0aW9ucyI6
IFt7InV1aWQiOiAiNTZmYjNhMjgtMjZhYS00ZDdjLTlkYmEtMDYyMmJlNWE3YmNlIiwgImV4cG9y
dF9rZXkiOiAiZm5fcGFzdGViaW4iLCAibmFtZSI6ICJmbl9wYXN0ZWJpbiIsICJkZXN0aW5hdGlv
bl90eXBlIjogMCwgInByb2dyYW1tYXRpY19uYW1lIjogImZuX3Bhc3RlYmluIiwgImV4cGVjdF9h
Y2siOiB0cnVlLCAidXNlcnMiOiBbImludGVncmF0aW9uc0BleGFtcGxlLmNvbSJdfV0sICJpbmNp
ZGVudF9hcnRpZmFjdF90eXBlcyI6IFtdLCAicm9sZXMiOiBbXSwgImZpZWxkcyI6IFt7Im9wZXJh
dGlvbnMiOiBbXSwgInJlYWRfb25seSI6IHRydWUsICJ1dWlkIjogImMzZjBlM2VkLTIxZTEtNGQ1
My1hZmZiLWZlNWNhMzMwOGNjYSIsICJ0ZW1wbGF0ZXMiOiBbXSwgInR5cGVfaWQiOiAwLCAiY2hv
c2VuIjogZmFsc2UsICJ0ZXh0IjogIlNpbXVsYXRpb24iLCAiZGVmYXVsdF9jaG9zZW5fYnlfc2Vy
dmVyIjogZmFsc2UsICJleHBvcnRfa2V5IjogImluY2lkZW50L2luY190cmFpbmluZyIsICJ0b29s
dGlwIjogIldoZXRoZXIgdGhlIGluY2lkZW50IGlzIGEgc2ltdWxhdGlvbiBvciBhIHJlZ3VsYXIg
aW5jaWRlbnQuICBUaGlzIGZpZWxkIGlzIHJlYWQtb25seS4iLCAicmljaF90ZXh0IjogZmFsc2Us
ICJvcGVyYXRpb25fcGVybXMiOiB7fSwgInByZWZpeCI6IG51bGwsICJpbnRlcm5hbCI6IGZhbHNl
LCAidmFsdWVzIjogW10sICJibGFua19vcHRpb24iOiBmYWxzZSwgImlucHV0X3R5cGUiOiAiYm9v
bGVhbiIsICJjaGFuZ2VhYmxlIjogdHJ1ZSwgImhpZGVfbm90aWZpY2F0aW9uIjogZmFsc2UsICJp
ZCI6IDM4LCAibmFtZSI6ICJpbmNfdHJhaW5pbmcifSwgeyJvcGVyYXRpb25zIjogW10sICJ0eXBl
X2lkIjogMTEsICJvcGVyYXRpb25fcGVybXMiOiB7fSwgInRleHQiOiAicGFzdGViaW5fZXhwaXJh
dGlvbiIsICJibGFua19vcHRpb24iOiBmYWxzZSwgInByZWZpeCI6IG51bGwsICJjaGFuZ2VhYmxl
IjogdHJ1ZSwgImlkIjogOTgsICJyZWFkX29ubHkiOiBmYWxzZSwgInV1aWQiOiAiYzQ4YTllNzIt
OTRiYy00Y2NlLWIwZGMtYzc3ZWVmYjFlOGE5IiwgImNob3NlbiI6IGZhbHNlLCAiaW5wdXRfdHlw
ZSI6ICJ0ZXh0IiwgInRvb2x0aXAiOiAiVGhpcyBzZXRzIHRoZSBleHBpcmF0aW9uIGRhdGUgb2Yg
eW91ciBwYXN0ZS4iLCAiaW50ZXJuYWwiOiBmYWxzZSwgInJpY2hfdGV4dCI6IGZhbHNlLCAidGVt
cGxhdGVzIjogW10sICJleHBvcnRfa2V5IjogIl9fZnVuY3Rpb24vcGFzdGViaW5fZXhwaXJhdGlv
biIsICJoaWRlX25vdGlmaWNhdGlvbiI6IGZhbHNlLCAicGxhY2Vob2xkZXIiOiAiIiwgIm5hbWUi
OiAicGFzdGViaW5fZXhwaXJhdGlvbiIsICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxz
ZSwgInZhbHVlcyI6IFtdfSwgeyJvcGVyYXRpb25zIjogW10sICJ0eXBlX2lkIjogMTEsICJvcGVy
YXRpb25fcGVybXMiOiB7fSwgInRleHQiOiAicGFzdGViaW5fbmFtZSIsICJibGFua19vcHRpb24i
OiBmYWxzZSwgInByZWZpeCI6IG51bGwsICJjaGFuZ2VhYmxlIjogdHJ1ZSwgImlkIjogOTUsICJy
ZWFkX29ubHkiOiBmYWxzZSwgInV1aWQiOiAiYWFhNzIwMzUtYTlkOC00ZmVlLWFlMDYtOWVkYWYx
NGZiODU3IiwgImNob3NlbiI6IGZhbHNlLCAiaW5wdXRfdHlwZSI6ICJ0ZXh0IiwgInRvb2x0aXAi
OiAiVGhpcyB3aWxsIGJlIHRoZSBuYW1lIC8gdGl0bGUgb2YgeW91ciBwYXN0ZS4iLCAiaW50ZXJu
YWwiOiBmYWxzZSwgInJpY2hfdGV4dCI6IGZhbHNlLCAidGVtcGxhdGVzIjogW10sICJleHBvcnRf
a2V5IjogIl9fZnVuY3Rpb24vcGFzdGViaW5fbmFtZSIsICJoaWRlX25vdGlmaWNhdGlvbiI6IGZh
bHNlLCAicGxhY2Vob2xkZXIiOiAiIiwgIm5hbWUiOiAicGFzdGViaW5fbmFtZSIsICJkZWZhdWx0
X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZSwgInZhbHVlcyI6IFtdfSwgeyJvcGVyYXRpb25zIjog
W10sICJ0eXBlX2lkIjogMTEsICJvcGVyYXRpb25fcGVybXMiOiB7fSwgInRleHQiOiAicGFzdGVi
aW5fZm9ybWF0IiwgImJsYW5rX29wdGlvbiI6IGZhbHNlLCAicHJlZml4IjogbnVsbCwgImNoYW5n
ZWFibGUiOiB0cnVlLCAiaWQiOiA5NiwgInJlYWRfb25seSI6IGZhbHNlLCAidXVpZCI6ICIzZTMy
N2M2ZC1hZWQ2LTQwMmMtOGFkOC04MzcyOTY5NzhkZDUiLCAiY2hvc2VuIjogZmFsc2UsICJpbnB1
dF90eXBlIjogInRleHQiLCAidG9vbHRpcCI6ICJUaGlzIHdpbGwgYmUgdGhlIHN5bnRheCBoaWdo
bGlnaHRpbmcgdmFsdWUiLCAiaW50ZXJuYWwiOiBmYWxzZSwgInJpY2hfdGV4dCI6IGZhbHNlLCAi
dGVtcGxhdGVzIjogW10sICJleHBvcnRfa2V5IjogIl9fZnVuY3Rpb24vcGFzdGViaW5fZm9ybWF0
IiwgImhpZGVfbm90aWZpY2F0aW9uIjogZmFsc2UsICJwbGFjZWhvbGRlciI6ICIiLCAibmFtZSI6
ICJwYXN0ZWJpbl9mb3JtYXQiLCAiZGVmYXVsdF9jaG9zZW5fYnlfc2VydmVyIjogZmFsc2UsICJ2
YWx1ZXMiOiBbXX0sIHsib3BlcmF0aW9ucyI6IFtdLCAidHlwZV9pZCI6IDExLCAib3BlcmF0aW9u
X3Blcm1zIjoge30sICJ0ZXh0IjogInBhc3RlYmluX3ByaXZhY3kiLCAiYmxhbmtfb3B0aW9uIjog
ZmFsc2UsICJwcmVmaXgiOiBudWxsLCAiY2hhbmdlYWJsZSI6IHRydWUsICJpZCI6IDk5LCAicmVh
ZF9vbmx5IjogZmFsc2UsICJ1dWlkIjogIjBjOTUxYzVhLTEwMWEtNDM5My04NzQ0LWQ0ZWQ0NWVi
Njg0YSIsICJjaG9zZW4iOiBmYWxzZSwgImlucHV0X3R5cGUiOiAibnVtYmVyIiwgInRvb2x0aXAi
OiAiVGhpcyBtYWtlcyBhIHBhc3RlIHB1YmxpYywgdW5saXN0ZWQgb3IgcHJpdmF0ZS4gKFB1Ymxp
YyA9IDAuIFVubGlzdGVkID0gMS4gUHJpdmF0ZSA9IDIpIiwgImludGVybmFsIjogZmFsc2UsICJy
aWNoX3RleHQiOiBmYWxzZSwgInRlbXBsYXRlcyI6IFtdLCAiZXhwb3J0X2tleSI6ICJfX2Z1bmN0
aW9uL3Bhc3RlYmluX3ByaXZhY3kiLCAiaGlkZV9ub3RpZmljYXRpb24iOiBmYWxzZSwgInBsYWNl
aG9sZGVyIjogIiIsICJuYW1lIjogInBhc3RlYmluX3ByaXZhY3kiLCAiZGVmYXVsdF9jaG9zZW5f
Ynlfc2VydmVyIjogZmFsc2UsICJ2YWx1ZXMiOiBbXX0sIHsib3BlcmF0aW9ucyI6IFtdLCAidHlw
ZV9pZCI6IDExLCAib3BlcmF0aW9uX3Blcm1zIjoge30sICJ0ZXh0IjogInBhc3RlYmluX2NvZGUi
LCAiYmxhbmtfb3B0aW9uIjogZmFsc2UsICJwcmVmaXgiOiBudWxsLCAiY2hhbmdlYWJsZSI6IHRy
dWUsICJpZCI6IDk0LCAicmVhZF9vbmx5IjogZmFsc2UsICJ1dWlkIjogIjMxOGMxNGZiLTNlZGQt
NGQ0OC04NzdjLWZjZDUxNWQzN2E3YSIsICJjaG9zZW4iOiBmYWxzZSwgImlucHV0X3R5cGUiOiAi
dGV4dCIsICJ0b29sdGlwIjogIlRoaXMgaXMgdGhlIHRleHQgdGhhdCB3aWxsIGJlIHdyaXR0ZW4g
aW5zaWRlIHlvdXIgcGFzdGUuIiwgImludGVybmFsIjogZmFsc2UsICJyaWNoX3RleHQiOiBmYWxz
ZSwgInRlbXBsYXRlcyI6IFtdLCAiZXhwb3J0X2tleSI6ICJfX2Z1bmN0aW9uL3Bhc3RlYmluX2Nv
ZGUiLCAiaGlkZV9ub3RpZmljYXRpb24iOiBmYWxzZSwgInBsYWNlaG9sZGVyIjogIiIsICJuYW1l
IjogInBhc3RlYmluX2NvZGUiLCAiZGVmYXVsdF9jaG9zZW5fYnlfc2VydmVyIjogZmFsc2UsICJy
ZXF1aXJlZCI6ICJhbHdheXMiLCAidmFsdWVzIjogW119XSwgIm92ZXJyaWRlcyI6IFtdLCAiZXhw
b3J0X2RhdGUiOiAxNTQwNTc0NDYxNzMxfQ==
"""
    )

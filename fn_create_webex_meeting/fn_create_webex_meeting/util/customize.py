# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_create_webex_meeting"""

from __future__ import print_function
from resilient_circuits.util import *

def codegen_reload_data():
    """Parameters to codegen used to generate the fn_create_webex_meeting package"""
    reload_params = {"package": u"fn_create_webex_meeting",
                    "incident_fields": [], 
                    "action_fields": [], 
                    "function_params": [u"webex_meeting_agenda", u"webex_meeting_end_time", u"webex_meeting_name", u"webex_meeting_password", u"webex_meeting_start_time"], 
                    "datatables": [], 
                    "message_destinations": [u"fn_create_webex_meeting"], 
                    "functions": [u"fn_create_webex_meeting"], 
                    "phases": [], 
                    "automatic_tasks": [], 
                    "scripts": [], 
                    "workflows": [u"example_create_webex_meeting"], 
                    "actions": [u"Example: Create WebEx Meeting: Incident"] 
                    }
    return reload_params


def customization_data(client=None):
    """Produce any customization definitions (types, fields, message destinations, etc)
       that should be installed by `resilient-circuits customize`
    """

    # This import data contains:
    #   Function inputs:
    #     webex_meeting_agenda
    #     webex_meeting_end_time
    #     webex_meeting_name
    #     webex_meeting_password
    #     webex_meeting_start_time
    #   Message Destinations:
    #     fn_create_webex_meeting
    #   Functions:
    #     fn_create_webex_meeting
    #   Workflows:
    #     example_create_webex_meeting
    #   Rules:
    #     Example: Create WebEx Meeting: Incident


    yield ImportDefinition(u"""
eyJzZXJ2ZXJfdmVyc2lvbiI6IHsibWFqb3IiOiAzMCwgIm1pbm9yIjogMCwgImJ1aWxkX251
bWJlciI6IDAsICJ2ZXJzaW9uIjogIjMwLjAuMCJ9LCAiZXhwb3J0X2Zvcm1hdF92ZXJzaW9u
IjogMiwgImlkIjogMzIsICJleHBvcnRfZGF0ZSI6IDE1NDA0MTA0MTg1NzIsICJmaWVsZHMi
OiBbeyJpZCI6IDUxLCAibmFtZSI6ICJpbmNfdHJhaW5pbmciLCAidGV4dCI6ICJTaW11bGF0
aW9uIiwgInByZWZpeCI6IG51bGwsICJ0eXBlX2lkIjogMCwgInRvb2x0aXAiOiAiV2hldGhl
ciB0aGUgaW5jaWRlbnQgaXMgYSBzaW11bGF0aW9uIG9yIGEgcmVndWxhciBpbmNpZGVudC4g
IFRoaXMgZmllbGQgaXMgcmVhZC1vbmx5LiIsICJpbnB1dF90eXBlIjogImJvb2xlYW4iLCAi
aGlkZV9ub3RpZmljYXRpb24iOiBmYWxzZSwgImNob3NlbiI6IGZhbHNlLCAiZGVmYXVsdF9j
aG9zZW5fYnlfc2VydmVyIjogZmFsc2UsICJibGFua19vcHRpb24iOiBmYWxzZSwgImludGVy
bmFsIjogZmFsc2UsICJ1dWlkIjogImMzZjBlM2VkLTIxZTEtNGQ1My1hZmZiLWZlNWNhMzMw
OGNjYSIsICJvcGVyYXRpb25zIjogW10sICJvcGVyYXRpb25fcGVybXMiOiB7fSwgInZhbHVl
cyI6IFtdLCAicmVhZF9vbmx5IjogdHJ1ZSwgImNoYW5nZWFibGUiOiB0cnVlLCAicmljaF90
ZXh0IjogZmFsc2UsICJleHBvcnRfa2V5IjogImluY2lkZW50L2luY190cmFpbmluZyIsICJ0
ZW1wbGF0ZXMiOiBbXSwgImRlcHJlY2F0ZWQiOiBmYWxzZX0sIHsiaWQiOiAzMjgsICJuYW1l
IjogIndlYmV4X21lZXRpbmdfbmFtZSIsICJ0ZXh0IjogIndlYmV4X21lZXRpbmdfbmFtZSIs
ICJwcmVmaXgiOiBudWxsLCAidHlwZV9pZCI6IDExLCAidG9vbHRpcCI6ICJNZWV0aW5nIG5h
bWUiLCAicGxhY2Vob2xkZXIiOiAiIiwgImlucHV0X3R5cGUiOiAidGV4dCIsICJoaWRlX25v
dGlmaWNhdGlvbiI6IGZhbHNlLCAiY2hvc2VuIjogZmFsc2UsICJkZWZhdWx0X2Nob3Nlbl9i
eV9zZXJ2ZXIiOiBmYWxzZSwgImJsYW5rX29wdGlvbiI6IGZhbHNlLCAiaW50ZXJuYWwiOiBm
YWxzZSwgInV1aWQiOiAiMTQ0MzhkYzctNDg3NC00OTcxLTlhYTctNTU5NmIxMzI3NmExIiwg
Im9wZXJhdGlvbnMiOiBbXSwgIm9wZXJhdGlvbl9wZXJtcyI6IHt9LCAidmFsdWVzIjogW10s
ICJyZWFkX29ubHkiOiBmYWxzZSwgImNoYW5nZWFibGUiOiB0cnVlLCAicmljaF90ZXh0Ijog
ZmFsc2UsICJleHBvcnRfa2V5IjogIl9fZnVuY3Rpb24vd2ViZXhfbWVldGluZ19uYW1lIiwg
InRlbXBsYXRlcyI6IFtdLCAiZGVwcmVjYXRlZCI6IGZhbHNlfSwgeyJpZCI6IDMzMSwgIm5h
bWUiOiAid2ViZXhfbWVldGluZ19hZ2VuZGEiLCAidGV4dCI6ICJ3ZWJleF9tZWV0aW5nX2Fn
ZW5kYSIsICJwcmVmaXgiOiBudWxsLCAidHlwZV9pZCI6IDExLCAidG9vbHRpcCI6ICJNZWV0
aW5nIGFnZW5kYSIsICJwbGFjZWhvbGRlciI6ICIiLCAiaW5wdXRfdHlwZSI6ICJ0ZXh0Iiwg
ImhpZGVfbm90aWZpY2F0aW9uIjogZmFsc2UsICJjaG9zZW4iOiBmYWxzZSwgImRlZmF1bHRf
Y2hvc2VuX2J5X3NlcnZlciI6IGZhbHNlLCAiYmxhbmtfb3B0aW9uIjogZmFsc2UsICJpbnRl
cm5hbCI6IGZhbHNlLCAidXVpZCI6ICI0YjE3OTg5Ny0zY2ZjLTRhOTgtODg2NC1kOWMwOWU2
ODVkNWEiLCAib3BlcmF0aW9ucyI6IFtdLCAib3BlcmF0aW9uX3Blcm1zIjoge30sICJ2YWx1
ZXMiOiBbXSwgInJlYWRfb25seSI6IGZhbHNlLCAiY2hhbmdlYWJsZSI6IHRydWUsICJyaWNo
X3RleHQiOiBmYWxzZSwgImV4cG9ydF9rZXkiOiAiX19mdW5jdGlvbi93ZWJleF9tZWV0aW5n
X2FnZW5kYSIsICJ0ZW1wbGF0ZXMiOiBbXSwgImRlcHJlY2F0ZWQiOiBmYWxzZX0sIHsiaWQi
OiAzMjcsICJuYW1lIjogIndlYmV4X21lZXRpbmdfc3RhcnRfdGltZSIsICJ0ZXh0IjogIndl
YmV4X21lZXRpbmdfc3RhcnRfdGltZSIsICJwcmVmaXgiOiBudWxsLCAidHlwZV9pZCI6IDEx
LCAidG9vbHRpcCI6ICIiLCAicGxhY2Vob2xkZXIiOiAiIiwgImlucHV0X3R5cGUiOiAiZGF0
ZXRpbWVwaWNrZXIiLCAiaGlkZV9ub3RpZmljYXRpb24iOiBmYWxzZSwgImNob3NlbiI6IGZh
bHNlLCAiZGVmYXVsdF9jaG9zZW5fYnlfc2VydmVyIjogZmFsc2UsICJibGFua19vcHRpb24i
OiBmYWxzZSwgImludGVybmFsIjogZmFsc2UsICJ1dWlkIjogIjU3MDZhYzYyLTk3ZWUtNGI1
NC05ODA3LTlmNGIxMjRlY2VjYyIsICJvcGVyYXRpb25zIjogW10sICJvcGVyYXRpb25fcGVy
bXMiOiB7fSwgInZhbHVlcyI6IFtdLCAicmVhZF9vbmx5IjogZmFsc2UsICJjaGFuZ2VhYmxl
IjogdHJ1ZSwgInJpY2hfdGV4dCI6IGZhbHNlLCAiZXhwb3J0X2tleSI6ICJfX2Z1bmN0aW9u
L3dlYmV4X21lZXRpbmdfc3RhcnRfdGltZSIsICJ0ZW1wbGF0ZXMiOiBbXSwgImRlcHJlY2F0
ZWQiOiBmYWxzZX0sIHsiaWQiOiAzMzAsICJuYW1lIjogIndlYmV4X21lZXRpbmdfcGFzc3dv
cmQiLCAidGV4dCI6ICJ3ZWJleF9tZWV0aW5nX3Bhc3N3b3JkIiwgInByZWZpeCI6IG51bGws
ICJ0eXBlX2lkIjogMTEsICJ0b29sdGlwIjogIk1lZXRpbmcgcGFzc3dvcmQiLCAicGxhY2Vo
b2xkZXIiOiAiIiwgImlucHV0X3R5cGUiOiAidGV4dCIsICJoaWRlX25vdGlmaWNhdGlvbiI6
IGZhbHNlLCAiY2hvc2VuIjogZmFsc2UsICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBm
YWxzZSwgImJsYW5rX29wdGlvbiI6IGZhbHNlLCAiaW50ZXJuYWwiOiBmYWxzZSwgInV1aWQi
OiAiMDNkZDE1MzEtYWNiYi00ZGI4LTk5NTAtNTM1MjBlYWJiYjVjIiwgIm9wZXJhdGlvbnMi
OiBbXSwgIm9wZXJhdGlvbl9wZXJtcyI6IHt9LCAidmFsdWVzIjogW10sICJyZWFkX29ubHki
OiBmYWxzZSwgImNoYW5nZWFibGUiOiB0cnVlLCAicmljaF90ZXh0IjogZmFsc2UsICJleHBv
cnRfa2V5IjogIl9fZnVuY3Rpb24vd2ViZXhfbWVldGluZ19wYXNzd29yZCIsICJ0ZW1wbGF0
ZXMiOiBbXSwgImRlcHJlY2F0ZWQiOiBmYWxzZX0sIHsiaWQiOiAzMjksICJuYW1lIjogIndl
YmV4X21lZXRpbmdfZW5kX3RpbWUiLCAidGV4dCI6ICJ3ZWJleF9tZWV0aW5nX2VuZF90aW1l
IiwgInByZWZpeCI6IG51bGwsICJ0eXBlX2lkIjogMTEsICJ0b29sdGlwIjogIiIsICJwbGFj
ZWhvbGRlciI6ICIiLCAiaW5wdXRfdHlwZSI6ICJkYXRldGltZXBpY2tlciIsICJoaWRlX25v
dGlmaWNhdGlvbiI6IGZhbHNlLCAiY2hvc2VuIjogZmFsc2UsICJkZWZhdWx0X2Nob3Nlbl9i
eV9zZXJ2ZXIiOiBmYWxzZSwgImJsYW5rX29wdGlvbiI6IGZhbHNlLCAiaW50ZXJuYWwiOiBm
YWxzZSwgInV1aWQiOiAiOWQzNjhhMmYtZWRmNC00MzUzLWE4YmEtMzdmODZjNWE4NGU3Iiwg
Im9wZXJhdGlvbnMiOiBbXSwgIm9wZXJhdGlvbl9wZXJtcyI6IHt9LCAidmFsdWVzIjogW10s
ICJyZWFkX29ubHkiOiBmYWxzZSwgImNoYW5nZWFibGUiOiB0cnVlLCAicmljaF90ZXh0Ijog
ZmFsc2UsICJleHBvcnRfa2V5IjogIl9fZnVuY3Rpb24vd2ViZXhfbWVldGluZ19lbmRfdGlt
ZSIsICJ0ZW1wbGF0ZXMiOiBbXSwgImRlcHJlY2F0ZWQiOiBmYWxzZX1dLCAiaW5jaWRlbnRf
dHlwZXMiOiBbeyJ1cGRhdGVfZGF0ZSI6IDE1NDA0MTEyNDg4NjAsICJjcmVhdGVfZGF0ZSI6
IDE1NDA0MTEyNDg4NjAsICJ1dWlkIjogImJmZWVjMmQ0LTM3NzAtMTFlOC1hZDM5LTRhMDAw
NDA0NGFhMCIsICJkZXNjcmlwdGlvbiI6ICJDdXN0b21pemF0aW9uIFBhY2thZ2VzIChpbnRl
cm5hbCkiLCAiZXhwb3J0X2tleSI6ICJDdXN0b21pemF0aW9uIFBhY2thZ2VzIChpbnRlcm5h
bCkiLCAibmFtZSI6ICJDdXN0b21pemF0aW9uIFBhY2thZ2VzIChpbnRlcm5hbCkiLCAiZW5h
YmxlZCI6IGZhbHNlLCAic3lzdGVtIjogZmFsc2UsICJwYXJlbnRfaWQiOiBudWxsLCAiaGlk
ZGVuIjogZmFsc2UsICJpZCI6IDB9XSwgInBoYXNlcyI6IFtdLCAiYXV0b21hdGljX3Rhc2tz
IjogW10sICJvdmVycmlkZXMiOiBbXSwgIm1lc3NhZ2VfZGVzdGluYXRpb25zIjogW3sibmFt
ZSI6ICJmbl9jcmVhdGVfd2ViZXhfbWVldGluZyIsICJwcm9ncmFtbWF0aWNfbmFtZSI6ICJm
bl9jcmVhdGVfd2ViZXhfbWVldGluZyIsICJkZXN0aW5hdGlvbl90eXBlIjogMCwgImV4cGVj
dF9hY2siOiB0cnVlLCAidXNlcnMiOiBbImJAYS5jb20iXSwgInV1aWQiOiAiOTdjYjMyZWMt
OGJiZi00ZGRiLWEzYWQtNGVjYjQ2NjQzNmQxIiwgImV4cG9ydF9rZXkiOiAiZm5fY3JlYXRl
X3dlYmV4X21lZXRpbmcifV0sICJhY3Rpb25zIjogW3siaWQiOiA5NCwgIm5hbWUiOiAiRXhh
bXBsZTogQ3JlYXRlIFdlYkV4IE1lZXRpbmc6IEluY2lkZW50IiwgInR5cGUiOiAxLCAib2Jq
ZWN0X3R5cGUiOiAiaW5jaWRlbnQiLCAiY29uZGl0aW9ucyI6IFtdLCAiYXV0b21hdGlvbnMi
OiBbXSwgIm1lc3NhZ2VfZGVzdGluYXRpb25zIjogW10sICJ3b3JrZmxvd3MiOiBbImV4YW1w
bGVfY3JlYXRlX3dlYmV4X21lZXRpbmciXSwgInZpZXdfaXRlbXMiOiBbXSwgInRpbWVvdXRf
c2Vjb25kcyI6IDg2NDAwLCAidXVpZCI6ICJmYjg0ZGVkYy1jMDVhLTQwMDMtOGEzNS1jNjI2
MmUyMDUyMGQiLCAiZXhwb3J0X2tleSI6ICJFeGFtcGxlOiBDcmVhdGUgV2ViRXggTWVldGlu
ZzogSW5jaWRlbnQiLCAibG9naWNfdHlwZSI6ICJhbGwifV0sICJsYXlvdXRzIjogW10sICJu
b3RpZmljYXRpb25zIjogbnVsbCwgInRpbWVmcmFtZXMiOiBudWxsLCAiaW5kdXN0cmllcyI6
IG51bGwsICJyZWd1bGF0b3JzIjogbnVsbCwgImdlb3MiOiBudWxsLCAidGFza19vcmRlciI6
IFtdLCAiYWN0aW9uX29yZGVyIjogW10sICJ0eXBlcyI6IFtdLCAic2NyaXB0cyI6IFtdLCAi
aW5jaWRlbnRfYXJ0aWZhY3RfdHlwZXMiOiBbXSwgIndvcmtmbG93cyI6IFt7IndvcmtmbG93
X2lkIjogNzEsICJuYW1lIjogIkV4YW1wbGU6IENyZWF0ZSBXZWJFeCBNZWV0aW5nOiBJbmNp
ZGVudCIsICJwcm9ncmFtbWF0aWNfbmFtZSI6ICJleGFtcGxlX2NyZWF0ZV93ZWJleF9tZWV0
aW5nIiwgIm9iamVjdF90eXBlIjogImluY2lkZW50IiwgImRlc2NyaXB0aW9uIjogIkFuIGV4
YW1wbGUgdGhhdCBjcmVhdGVzIGEgQ2lzY28gV2ViRXggbWVldGluZyBiYXNlZCBvbiBpbmNp
ZGVudCBwcm9wZXJ0aWVzLiIsICJjcmVhdG9yX2lkIjogImJAYS5jb20iLCAibGFzdF9tb2Rp
ZmllZF9ieSI6ICJsMkBhYmxlLmNvbSIsICJsYXN0X21vZGlmaWVkX3RpbWUiOiAxNTQwNDA4
OTI4ODUwLCAiZXhwb3J0X2tleSI6ICJleGFtcGxlX2NyZWF0ZV93ZWJleF9tZWV0aW5nIiwg
InV1aWQiOiAiNGM1YjdlYjMtMWMyYi00MTFmLWJkODMtYjRhMTFlMDZmODAxIiwgImNvbnRl
bnQiOiB7IndvcmtmbG93X2lkIjogImV4YW1wbGVfY3JlYXRlX3dlYmV4X21lZXRpbmciLCAi
eG1sIjogIjw/eG1sIHZlcnNpb249XCIxLjBcIiBlbmNvZGluZz1cIlVURi04XCI/PjxkZWZp
bml0aW9ucyB4bWxucz1cImh0dHA6Ly93d3cub21nLm9yZy9zcGVjL0JQTU4vMjAxMDA1MjQv
TU9ERUxcIiB4bWxuczpicG1uZGk9XCJodHRwOi8vd3d3Lm9tZy5vcmcvc3BlYy9CUE1OLzIw
MTAwNTI0L0RJXCIgeG1sbnM6b21nZGM9XCJodHRwOi8vd3d3Lm9tZy5vcmcvc3BlYy9ERC8y
MDEwMDUyNC9EQ1wiIHhtbG5zOm9tZ2RpPVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMvREQv
MjAxMDA1MjQvRElcIiB4bWxuczpyZXNpbGllbnQ9XCJodHRwOi8vcmVzaWxpZW50LmlibS5j
b20vYnBtblwiIHhtbG5zOnhzZD1cImh0dHA6Ly93d3cudzMub3JnLzIwMDEvWE1MU2NoZW1h
XCIgeG1sbnM6eHNpPVwiaHR0cDovL3d3dy53My5vcmcvMjAwMS9YTUxTY2hlbWEtaW5zdGFu
Y2VcIiB0YXJnZXROYW1lc3BhY2U9XCJodHRwOi8vd3d3LmNhbXVuZGEub3JnL3Rlc3RcIj48
cHJvY2VzcyBpZD1cImV4YW1wbGVfY3JlYXRlX3dlYmV4X21lZXRpbmdcIiBpc0V4ZWN1dGFi
bGU9XCJ0cnVlXCIgbmFtZT1cIkV4YW1wbGU6IENyZWF0ZSBXZWJFeCBNZWV0aW5nOiBJbmNp
ZGVudFwiPjxkb2N1bWVudGF0aW9uPkFuIGV4YW1wbGUgdGhhdCBjcmVhdGVzIGEgQ2lzY28g
V2ViRXggbWVldGluZyBiYXNlZCBvbiBpbmNpZGVudCBwcm9wZXJ0aWVzLjwvZG9jdW1lbnRh
dGlvbj48c3RhcnRFdmVudCBpZD1cIlN0YXJ0RXZlbnRfMTU1YXN4bVwiPjxvdXRnb2luZz5T
ZXF1ZW5jZUZsb3dfMHh6eW9raTwvb3V0Z29pbmc+PC9zdGFydEV2ZW50PjxzZXJ2aWNlVGFz
ayBpZD1cIlNlcnZpY2VUYXNrXzBiMG91d2RcIiBuYW1lPVwiQ3JlYXRlIFdlYkV4IE1lZXRp
bmdcIiByZXNpbGllbnQ6dHlwZT1cImZ1bmN0aW9uXCI+PGV4dGVuc2lvbkVsZW1lbnRzPjxy
ZXNpbGllbnQ6ZnVuY3Rpb24gdXVpZD1cImFiOWJkNjNhLTcyOGUtNGM4MC1hYTM2LTI3ZTI4
ODgxM2MzNFwiPntcImlucHV0c1wiOntcIjAzZGQxNTMxLWFjYmItNGRiOC05OTUwLTUzNTIw
ZWFiYmI1Y1wiOntcImlucHV0X3R5cGVcIjpcInN0YXRpY1wiLFwic3RhdGljX2lucHV0XCI6
e1wibXVsdGlzZWxlY3RfdmFsdWVcIjpbXSxcInRleHRfdmFsdWVcIjpcImFiY1wifX0sXCI1
NzA2YWM2Mi05N2VlLTRiNTQtOTgwNy05ZjRiMTI0ZWNlY2NcIjp7XCJpbnB1dF90eXBlXCI6
XCJzdGF0aWNcIixcInN0YXRpY19pbnB1dFwiOntcImRhdGVfdmFsdWVcIjoxNTQwNDk3NjAw
MDAwLFwibXVsdGlzZWxlY3RfdmFsdWVcIjpbXX19LFwiOWQzNjhhMmYtZWRmNC00MzUzLWE4
YmEtMzdmODZjNWE4NGU3XCI6e1wiaW5wdXRfdHlwZVwiOlwic3RhdGljXCIsXCJzdGF0aWNf
aW5wdXRcIjp7XCJkYXRlX3ZhbHVlXCI6MTU0MDQ5ODgwMDAwMCxcIm11bHRpc2VsZWN0X3Zh
bHVlXCI6W119fX0sXCJwb3N0X3Byb2Nlc3Npbmdfc2NyaXB0XCI6XCJob3N0X3VybCA9IHJl
c3VsdHMuaG9zdF91cmxcXG5hdHRlbmRlZV91cmwgPSByZXN1bHRzLmF0dGVuZGVlX3VybFxc
blxcbmlmIGhvc3RfdXJsIGlzIE5vbmU6XFxuICBob3N0X3VybCA9IFxcXCJcXFwiXFxuXFxu
aWYgYXR0ZW5kZWVfdXJsIGlzIE5vbmU6XFxuICBhdHRlbmRlZV91cmwgPSBcXFwiXFxcIlxc
blxcbnRleHQgPSBcXFwiQ2lzY28gV2ViRXggTWVldGluZzpcXFxcblxcXFx0SG9zdCBVUkw6
IFxcXCIgKyByZXN1bHRzLmhvc3RfdXJsICsgXFxcIlxcXFxuXFxcXHRBdHRlbmRlZSBVUkw6
IFxcXCIgKyByZXN1bHRzLmF0dGVuZGVlX3VybFxcbm5vdGUgPSBoZWxwZXIuY3JlYXRlUGxh
aW5UZXh0KHRleHQpXFxuaW5jaWRlbnQuYWRkTm90ZShub3RlKVwiLFwicHJlX3Byb2Nlc3Np
bmdfc2NyaXB0XCI6XCIjIFRvIHNldCBtZWV0aW5nIG5hbWUgdG8gdGhlIHdvcmtmbG93IGlu
cHV0cywgdW5jb21tZW50IHRoZSBmb2xsb3dpbmcgbGluZXNcXG5pbnB1dHMud2ViZXhfbWVl
dGluZ19uYW1lID0gaW5jaWRlbnQubmFtZVxcbmlmIGluY2lkZW50LmRlc2NyaXB0aW9uIGlz
IG5vdCBOb25lIGFuZCBpbmNpZGVudC5kZXNjcmlwdGlvbi5jb250ZW50IGlzIG5vdCBOb25l
OlxcbiAgaW5wdXRzLndlYmV4X21lZXRpbmdfYWdlbmRhID0gaW5jaWRlbnQuZGVzY3JpcHRp
b24uY29udGVudFxcbmVsc2U6XFxuICBpbnB1dHMud2ViZXhfbWVldGluZ19hZ2VuZGEgPSBc
XFwiXFxcIlwiLFwicmVzdWx0X25hbWVcIjpcIlwifTwvcmVzaWxpZW50OmZ1bmN0aW9uPjwv
ZXh0ZW5zaW9uRWxlbWVudHM+PGluY29taW5nPlNlcXVlbmNlRmxvd18weHp5b2tpPC9pbmNv
bWluZz48b3V0Z29pbmc+U2VxdWVuY2VGbG93XzBrbHJjbjk8L291dGdvaW5nPjwvc2Vydmlj
ZVRhc2s+PHNlcXVlbmNlRmxvdyBpZD1cIlNlcXVlbmNlRmxvd18weHp5b2tpXCIgc291cmNl
UmVmPVwiU3RhcnRFdmVudF8xNTVhc3htXCIgdGFyZ2V0UmVmPVwiU2VydmljZVRhc2tfMGIw
b3V3ZFwiLz48ZW5kRXZlbnQgaWQ9XCJFbmRFdmVudF8wcnVuNGx4XCI+PGluY29taW5nPlNl
cXVlbmNlRmxvd18wa2xyY245PC9pbmNvbWluZz48L2VuZEV2ZW50PjxzZXF1ZW5jZUZsb3cg
aWQ9XCJTZXF1ZW5jZUZsb3dfMGtscmNuOVwiIHNvdXJjZVJlZj1cIlNlcnZpY2VUYXNrXzBi
MG91d2RcIiB0YXJnZXRSZWY9XCJFbmRFdmVudF8wcnVuNGx4XCIvPjx0ZXh0QW5ub3RhdGlv
biBpZD1cIlRleHRBbm5vdGF0aW9uXzFreHhpeXRcIj48dGV4dD5TdGFydCB5b3VyIHdvcmtm
bG93IGhlcmU8L3RleHQ+PC90ZXh0QW5ub3RhdGlvbj48YXNzb2NpYXRpb24gaWQ9XCJBc3Nv
Y2lhdGlvbl8xc2V1ajQ4XCIgc291cmNlUmVmPVwiU3RhcnRFdmVudF8xNTVhc3htXCIgdGFy
Z2V0UmVmPVwiVGV4dEFubm90YXRpb25fMWt4eGl5dFwiLz48dGV4dEFubm90YXRpb24gaWQ9
XCJUZXh0QW5ub3RhdGlvbl8xbzhtZHhvXCI+PHRleHQ+aW5wdXRzOlx1MDBhMHdlYmV4X21l
ZXRpbmdfbmFtZSwgd2ViZXhfbWVldGluZ19hZ2VuZGEsIGFuZCB3ZWJleF9tZWV0aW5nX3Bh
c3N3b3JkPC90ZXh0PjwvdGV4dEFubm90YXRpb24+PGFzc29jaWF0aW9uIGlkPVwiQXNzb2Np
YXRpb25fMGYzMHFveFwiIHNvdXJjZVJlZj1cIlNlcnZpY2VUYXNrXzBiMG91d2RcIiB0YXJn
ZXRSZWY9XCJUZXh0QW5ub3RhdGlvbl8xbzhtZHhvXCIvPjx0ZXh0QW5ub3RhdGlvbiBpZD1c
IlRleHRBbm5vdGF0aW9uXzBlN2Rxc3pcIj48dGV4dD5vdXRwdXRzOiBob3N0X3VybCBhbmQg
YXR0ZW5kZWVfdXJsIGFkZGVkIHRvIGluY2lkZW50IG5vdGVzPC90ZXh0PjwvdGV4dEFubm90
YXRpb24+PGFzc29jaWF0aW9uIGlkPVwiQXNzb2NpYXRpb25fMTczazV2blwiIHNvdXJjZVJl
Zj1cIlNlcnZpY2VUYXNrXzBiMG91d2RcIiB0YXJnZXRSZWY9XCJUZXh0QW5ub3RhdGlvbl8w
ZTdkcXN6XCIvPjwvcHJvY2Vzcz48YnBtbmRpOkJQTU5EaWFncmFtIGlkPVwiQlBNTkRpYWdy
YW1fMVwiPjxicG1uZGk6QlBNTlBsYW5lIGJwbW5FbGVtZW50PVwidW5kZWZpbmVkXCIgaWQ9
XCJCUE1OUGxhbmVfMVwiPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVtZW50PVwiU3RhcnRF
dmVudF8xNTVhc3htXCIgaWQ9XCJTdGFydEV2ZW50XzE1NWFzeG1fZGlcIj48b21nZGM6Qm91
bmRzIGhlaWdodD1cIjM2XCIgd2lkdGg9XCIzNlwiIHg9XCIxNjJcIiB5PVwiMTg4XCIvPjxi
cG1uZGk6QlBNTkxhYmVsPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMFwiIHdpZHRoPVwiOTBc
IiB4PVwiMTU3XCIgeT1cIjIyM1wiLz48L2JwbW5kaTpCUE1OTGFiZWw+PC9icG1uZGk6QlBN
TlNoYXBlPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVtZW50PVwiVGV4dEFubm90YXRpb25f
MWt4eGl5dFwiIGlkPVwiVGV4dEFubm90YXRpb25fMWt4eGl5dF9kaVwiPjxvbWdkYzpCb3Vu
ZHMgaGVpZ2h0PVwiMzBcIiB3aWR0aD1cIjEwMFwiIHg9XCI5OVwiIHk9XCIyNTRcIi8+PC9i
cG1uZGk6QlBNTlNoYXBlPjxicG1uZGk6QlBNTkVkZ2UgYnBtbkVsZW1lbnQ9XCJBc3NvY2lh
dGlvbl8xc2V1ajQ4XCIgaWQ9XCJBc3NvY2lhdGlvbl8xc2V1ajQ4X2RpXCI+PG9tZ2RpOndh
eXBvaW50IHg9XCIxNjlcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIyMFwiLz48
b21nZGk6d2F5cG9pbnQgeD1cIjE1M1wiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwi
MjU0XCIvPjwvYnBtbmRpOkJQTU5FZGdlPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVtZW50
PVwiU2VydmljZVRhc2tfMGIwb3V3ZFwiIGlkPVwiU2VydmljZVRhc2tfMGIwb3V3ZF9kaVwi
PjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiODBcIiB3aWR0aD1cIjEwMFwiIHg9XCIzMTVcIiB5
PVwiMTY2XCIvPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5FZGdlIGJwbW5FbGVt
ZW50PVwiU2VxdWVuY2VGbG93XzB4enlva2lcIiBpZD1cIlNlcXVlbmNlRmxvd18weHp5b2tp
X2RpXCI+PG9tZ2RpOndheXBvaW50IHg9XCIxOThcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50
XCIgeT1cIjIwNlwiLz48b21nZGk6d2F5cG9pbnQgeD1cIjMxNVwiIHhzaTp0eXBlPVwib21n
ZGM6UG9pbnRcIiB5PVwiMjA2XCIvPjxicG1uZGk6QlBNTkxhYmVsPjxvbWdkYzpCb3VuZHMg
aGVpZ2h0PVwiMTNcIiB3aWR0aD1cIjBcIiB4PVwiMjU2LjVcIiB5PVwiMTg0XCIvPjwvYnBt
bmRpOkJQTU5MYWJlbD48L2JwbW5kaTpCUE1ORWRnZT48YnBtbmRpOkJQTU5TaGFwZSBicG1u
RWxlbWVudD1cIkVuZEV2ZW50XzBydW40bHhcIiBpZD1cIkVuZEV2ZW50XzBydW40bHhfZGlc
Ij48b21nZGM6Qm91bmRzIGhlaWdodD1cIjM2XCIgd2lkdGg9XCIzNlwiIHg9XCI1MjRcIiB5
PVwiMTg4XCIvPjxicG1uZGk6QlBNTkxhYmVsPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMTNc
IiB3aWR0aD1cIjBcIiB4PVwiNTQyXCIgeT1cIjIyN1wiLz48L2JwbW5kaTpCUE1OTGFiZWw+
PC9icG1uZGk6QlBNTlNoYXBlPjxicG1uZGk6QlBNTkVkZ2UgYnBtbkVsZW1lbnQ9XCJTZXF1
ZW5jZUZsb3dfMGtscmNuOVwiIGlkPVwiU2VxdWVuY2VGbG93XzBrbHJjbjlfZGlcIj48b21n
ZGk6d2F5cG9pbnQgeD1cIjQxNVwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjA2
XCIvPjxvbWdkaTp3YXlwb2ludCB4PVwiNTI0XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwi
IHk9XCIyMDZcIi8+PGJwbW5kaTpCUE1OTGFiZWw+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIx
M1wiIHdpZHRoPVwiMFwiIHg9XCI0NjkuNVwiIHk9XCIxODRcIi8+PC9icG1uZGk6QlBNTkxh
YmVsPjwvYnBtbmRpOkJQTU5FZGdlPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVtZW50PVwi
VGV4dEFubm90YXRpb25fMW84bWR4b1wiIGlkPVwiVGV4dEFubm90YXRpb25fMW84bWR4b19k
aVwiPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMzFcIiB3aWR0aD1cIjQxMVwiIHg9XCItOTVc
IiB5PVwiNjFcIi8+PC9icG1uZGk6QlBNTlNoYXBlPjxicG1uZGk6QlBNTkVkZ2UgYnBtbkVs
ZW1lbnQ9XCJBc3NvY2lhdGlvbl8wZjMwcW94XCIgaWQ9XCJBc3NvY2lhdGlvbl8wZjMwcW94
X2RpXCI+PG9tZ2RpOndheXBvaW50IHg9XCIzMTVcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50
XCIgeT1cIjE4MVwiLz48b21nZGk6d2F5cG9pbnQgeD1cIjE0MVwiIHhzaTp0eXBlPVwib21n
ZGM6UG9pbnRcIiB5PVwiOTJcIi8+PC9icG1uZGk6QlBNTkVkZ2U+PGJwbW5kaTpCUE1OU2hh
cGUgYnBtbkVsZW1lbnQ9XCJUZXh0QW5ub3RhdGlvbl8wZTdkcXN6XCIgaWQ9XCJUZXh0QW5u
b3RhdGlvbl8wZTdkcXN6X2RpXCI+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIzMFwiIHdpZHRo
PVwiMzM2XCIgeD1cIjQwNVwiIHk9XCI2MlwiLz48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5k
aTpCUE1ORWRnZSBicG1uRWxlbWVudD1cIkFzc29jaWF0aW9uXzE3M2s1dm5cIiBpZD1cIkFz
c29jaWF0aW9uXzE3M2s1dm5fZGlcIj48b21nZGk6d2F5cG9pbnQgeD1cIjQxM1wiIHhzaTp0
eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMTc0XCIvPjxvbWdkaTp3YXlwb2ludCB4PVwiNTMy
XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCI5MlwiLz48L2JwbW5kaTpCUE1ORWRn
ZT48L2JwbW5kaTpCUE1OUGxhbmU+PC9icG1uZGk6QlBNTkRpYWdyYW0+PC9kZWZpbml0aW9u
cz4iLCAidmVyc2lvbiI6IDZ9LCAiYWN0aW9ucyI6IFtdfV0sICJyb2xlcyI6IFtdLCAid29y
a3NwYWNlcyI6IFtdLCAiZnVuY3Rpb25zIjogW3siaWQiOiA5NCwgIm5hbWUiOiAiZm5fY3Jl
YXRlX3dlYmV4X21lZXRpbmciLCAiZGlzcGxheV9uYW1lIjogIkNyZWF0ZSBXZWJFeCBNZWV0
aW5nIiwgImRlc2NyaXB0aW9uIjogeyJmb3JtYXQiOiAidGV4dCIsICJjb250ZW50IjogIkNy
ZWF0ZXMgYSB3ZWJleCBtZWV0aW5nIGFuZCByZXR1cm5zIHRoZSBVUkwifSwgImRlc3RpbmF0
aW9uX2hhbmRsZSI6ICJmbl9jcmVhdGVfd2ViZXhfbWVldGluZyIsICJleHBvcnRfa2V5Ijog
ImZuX2NyZWF0ZV93ZWJleF9tZWV0aW5nIiwgInV1aWQiOiAiYWI5YmQ2M2EtNzI4ZS00Yzgw
LWFhMzYtMjdlMjg4ODEzYzM0IiwgInZlcnNpb24iOiAxLCAiY3JlYXRvciI6IHsiaWQiOiAz
LCAidHlwZSI6ICJ1c2VyIiwgIm5hbWUiOiAiYkBhLmNvbSIsICJkaXNwbGF5X25hbWUiOiAi
UmVzaWxpZW50IFN5c2FkbWluIn0sICJsYXN0X21vZGlmaWVkX2J5IjogeyJpZCI6IDMsICJ0
eXBlIjogInVzZXIiLCAibmFtZSI6ICJiQGEuY29tIiwgImRpc3BsYXlfbmFtZSI6ICJSZXNp
bGllbnQgU3lzYWRtaW4ifSwgImxhc3RfbW9kaWZpZWRfdGltZSI6IDE1NDAzMjYwMjkzMjMs
ICJ2aWV3X2l0ZW1zIjogW3sic3RlcF9sYWJlbCI6IG51bGwsICJzaG93X2lmIjogbnVsbCwg
ImVsZW1lbnQiOiAiZmllbGRfdXVpZCIsICJmaWVsZF90eXBlIjogIl9fZnVuY3Rpb24iLCAi
Y29udGVudCI6ICIxNDQzOGRjNy00ODc0LTQ5NzEtOWFhNy01NTk2YjEzMjc2YTEiLCAic2hv
d19saW5rX2hlYWRlciI6IGZhbHNlfSwgeyJzdGVwX2xhYmVsIjogbnVsbCwgInNob3dfaWYi
OiBudWxsLCAiZWxlbWVudCI6ICJmaWVsZF91dWlkIiwgImZpZWxkX3R5cGUiOiAiX19mdW5j
dGlvbiIsICJjb250ZW50IjogIjRiMTc5ODk3LTNjZmMtNGE5OC04ODY0LWQ5YzA5ZTY4NWQ1
YSIsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2V9LCB7InN0ZXBfbGFiZWwiOiBudWxsLCAi
c2hvd19pZiI6IG51bGwsICJlbGVtZW50IjogImZpZWxkX3V1aWQiLCAiZmllbGRfdHlwZSI6
ICJfX2Z1bmN0aW9uIiwgImNvbnRlbnQiOiAiMDNkZDE1MzEtYWNiYi00ZGI4LTk5NTAtNTM1
MjBlYWJiYjVjIiwgInNob3dfbGlua19oZWFkZXIiOiBmYWxzZX0sIHsic3RlcF9sYWJlbCI6
IG51bGwsICJzaG93X2lmIjogbnVsbCwgImVsZW1lbnQiOiAiZmllbGRfdXVpZCIsICJmaWVs
ZF90eXBlIjogIl9fZnVuY3Rpb24iLCAiY29udGVudCI6ICI1NzA2YWM2Mi05N2VlLTRiNTQt
OTgwNy05ZjRiMTI0ZWNlY2MiLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlfSwgeyJzdGVw
X2xhYmVsIjogbnVsbCwgInNob3dfaWYiOiBudWxsLCAiZWxlbWVudCI6ICJmaWVsZF91dWlk
IiwgImZpZWxkX3R5cGUiOiAiX19mdW5jdGlvbiIsICJjb250ZW50IjogIjlkMzY4YTJmLWVk
ZjQtNDM1My1hOGJhLTM3Zjg2YzVhODRlNyIsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2V9
XSwgIndvcmtmbG93cyI6IFt7IndvcmtmbG93X2lkIjogNzEsICJuYW1lIjogIkV4YW1wbGU6
IENyZWF0ZSBXZWJFeCBNZWV0aW5nOiBJbmNpZGVudCIsICJwcm9ncmFtbWF0aWNfbmFtZSI6
ICJleGFtcGxlX2NyZWF0ZV93ZWJleF9tZWV0aW5nIiwgIm9iamVjdF90eXBlIjogImluY2lk
ZW50IiwgImRlc2NyaXB0aW9uIjogbnVsbCwgInV1aWQiOiBudWxsLCAiYWN0aW9ucyI6IFtd
fSwgeyJ3b3JrZmxvd19pZCI6IDcyLCAibmFtZSI6ICJleGFtcGxlX2NyZWF0ZV93ZWJleF9t
ZWV0aW5nMiIsICJwcm9ncmFtbWF0aWNfbmFtZSI6ICJleGFtcGxlX2NyZWF0ZV93ZWJleF9t
ZWV0aW5nMiIsICJvYmplY3RfdHlwZSI6ICJpbmNpZGVudCIsICJkZXNjcmlwdGlvbiI6IG51
bGwsICJ1dWlkIjogbnVsbCwgImFjdGlvbnMiOiBbXX0sIHsid29ya2Zsb3dfaWQiOiA3Mywg
Im5hbWUiOiAid2ViZXgiLCAicHJvZ3JhbW1hdGljX25hbWUiOiAid2ViZXgiLCAib2JqZWN0
X3R5cGUiOiAiaW5jaWRlbnQiLCAiZGVzY3JpcHRpb24iOiBudWxsLCAidXVpZCI6IG51bGws
ICJhY3Rpb25zIjogW119XX1dfQo=
"""
    )
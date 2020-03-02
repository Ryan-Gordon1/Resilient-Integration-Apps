# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_ioc_parser_v2"""

from __future__ import print_function
from resilient_circuits.util import *

def codegen_reload_data():
    """Parameters to codegen used to generate the fn_ioc_parser_v2 package"""
    reload_params = {"package": u"fn_ioc_parser_v2",
                    "incident_fields": [], 
                    "action_fields": [], 
                    "function_params": [u"ioc_parser_v2_artifact_id", u"ioc_parser_v2_artifact_value", u"ioc_parser_v2_attachment_id", u"ioc_parser_v2_incident_id", u"ioc_parser_v2_task_id"], 
                    "datatables": [], 
                    "message_destinations": [u"fn_ioc_parser_v2"], 
                    "functions": [u"func_ioc_parser_v2"], 
                    "phases": [], 
                    "automatic_tasks": [], 
                    "scripts": [], 
                    "workflows": [u"example_parse_iocs_artifact", u"example_parse_iocs_attachment"], 
                    "actions": [u"Example: Parse IOCs (Artifact)", u"Example: Parse IOCs (Attachment)"], 
                    "incident_artifact_types": [] 
                    }
    return reload_params


def customization_data(client=None):
    """Produce any customization definitions (types, fields, message destinations, etc)
       that should be installed by `resilient-circuits customize`
    """

    # This import data contains:
    #   Function inputs:
    #     ioc_parser_v2_artifact_id
    #     ioc_parser_v2_artifact_value
    #     ioc_parser_v2_attachment_id
    #     ioc_parser_v2_incident_id
    #     ioc_parser_v2_task_id
    #   Message Destinations:
    #     fn_ioc_parser_v2
    #   Functions:
    #     func_ioc_parser_v2
    #   Workflows:
    #     example_parse_iocs_artifact
    #     example_parse_iocs_attachment
    #   Rules:
    #     Example: Parse IOCs (Artifact)
    #     Example: Parse IOCs (Attachment)


    yield ImportDefinition(u"""
eyJ0YXNrX29yZGVyIjogW10sICJ3b3JrZmxvd3MiOiBbeyJ1dWlkIjogIjVhMjZjMGYxLTM0Mzct
NGY3MC1iODc0LWQzYmUwOTY1ZjQxNSIsICJkZXNjcmlwdGlvbiI6ICJFeGFtcGxlIHdvcmtmbG93
IHNob3dpbmcgaG93IHRvIGV4dHJhY3QgSU9DJ3MgKEluZGljYXRvcnMgb2YgQ29tcHJvbWlzZSkg
ZnJvbSBJbmNpZGVudC9UYXNrIEF0dGFjaG1lbnRzLiBFYWNoIHVuaXF1ZSBJT0MgaXMgYWRkZWQg
dG8gdGhlIEluY2lkZW50IGFzIGFuIEFydGlmYWN0IiwgIm9iamVjdF90eXBlIjogImF0dGFjaG1l
bnQiLCAiZXhwb3J0X2tleSI6ICJleGFtcGxlX3BhcnNlX2lvY3NfYXR0YWNobWVudCIsICJ3b3Jr
Zmxvd19pZCI6IDIzLCAibGFzdF9tb2RpZmllZF9ieSI6ICJhZG1pbkBleGFtcGxlLmNvbSIsICJj
b250ZW50IjogeyJ4bWwiOiAiPD94bWwgdmVyc2lvbj1cIjEuMFwiIGVuY29kaW5nPVwiVVRGLThc
Ij8+PGRlZmluaXRpb25zIHhtbG5zPVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMvQlBNTi8yMDEw
MDUyNC9NT0RFTFwiIHhtbG5zOmJwbW5kaT1cImh0dHA6Ly93d3cub21nLm9yZy9zcGVjL0JQTU4v
MjAxMDA1MjQvRElcIiB4bWxuczpvbWdkYz1cImh0dHA6Ly93d3cub21nLm9yZy9zcGVjL0RELzIw
MTAwNTI0L0RDXCIgeG1sbnM6b21nZGk9XCJodHRwOi8vd3d3Lm9tZy5vcmcvc3BlYy9ERC8yMDEw
MDUyNC9ESVwiIHhtbG5zOnJlc2lsaWVudD1cImh0dHA6Ly9yZXNpbGllbnQuaWJtLmNvbS9icG1u
XCIgeG1sbnM6eHNkPVwiaHR0cDovL3d3dy53My5vcmcvMjAwMS9YTUxTY2hlbWFcIiB4bWxuczp4
c2k9XCJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYS1pbnN0YW5jZVwiIHRhcmdldE5h
bWVzcGFjZT1cImh0dHA6Ly93d3cuY2FtdW5kYS5vcmcvdGVzdFwiPjxwcm9jZXNzIGlkPVwiZXhh
bXBsZV9wYXJzZV9pb2NzX2F0dGFjaG1lbnRcIiBpc0V4ZWN1dGFibGU9XCJ0cnVlXCIgbmFtZT1c
IkV4YW1wbGU6IFBhcnNlIElPQ3MgKEF0dGFjaG1lbnQpXCI+PGRvY3VtZW50YXRpb24+PCFbQ0RB
VEFbRXhhbXBsZSB3b3JrZmxvdyBzaG93aW5nIGhvdyB0byBleHRyYWN0IElPQydzIChJbmRpY2F0
b3JzIG9mIENvbXByb21pc2UpIGZyb20gSW5jaWRlbnQvVGFzayBBdHRhY2htZW50cy4gRWFjaCB1
bmlxdWUgSU9DIGlzIGFkZGVkIHRvIHRoZSBJbmNpZGVudCBhcyBhbiBBcnRpZmFjdF1dPjwvZG9j
dW1lbnRhdGlvbj48c3RhcnRFdmVudCBpZD1cIlN0YXJ0RXZlbnRfMTU1YXN4bVwiPjxvdXRnb2lu
Zz5TZXF1ZW5jZUZsb3dfMGhiang2bTwvb3V0Z29pbmc+PC9zdGFydEV2ZW50PjxzZXJ2aWNlVGFz
ayBpZD1cIlNlcnZpY2VUYXNrXzFxYm43MG9cIiBuYW1lPVwiSU9DIFBhcnNlciB2MlwiIHJlc2ls
aWVudDp0eXBlPVwiZnVuY3Rpb25cIj48ZXh0ZW5zaW9uRWxlbWVudHM+PHJlc2lsaWVudDpmdW5j
dGlvbiB1dWlkPVwiNTI4MDM1ODEtMDE5YS00YzY4LThmOGQtOGJlOWNhMzFiMmY2XCI+e1wiaW5w
dXRzXCI6e30sXCJwb3N0X3Byb2Nlc3Npbmdfc2NyaXB0XCI6XCJpbXBvcnQgcmVcXG5cXG5kZWYg
Z2V0X2FydGlmYWN0X3R5cGUoYXJ0aWZhY3RfdmFsdWUsIGFydGlmYWN0X3R5cGUpOlxcbiAgXFxc
IlxcXCJcXFwiVXNlIHNvbWUgcmVnZXggZXhwcmVzc2lvbnMgdG8gdHJ5IGFuZCBpZGVudGlmeVxc
biAgZnJvbSB0aGUgQXJ0aWZhY3QncyB2YWx1ZSwgd2hhdCBBcnRpZmFjdCB0eXBlIGl0IGlzLlxc
biAgUmV0dXJuIG9yaWdpbmFsIGFydGlmYWN0X3R5cGUgaWYgd2UgY2Fubm90IGZpZ3VyZSBpdCBv
dXRcXFwiXFxcIlxcXCJcXG5cXG4gIGRuc19uYW1lX3JlZ2V4ID0gcmUuY29tcGlsZShyJ14oKFth
LXpBLVpdezF9KXwoW2EtekEtWl17MX1bYS16QS1aXXsxfSl8KFthLXpBLVpdezF9WzAtOV17MX0p
fChbMC05XXsxfVthLXpBLVpdezF9KXwoW2EtekEtWjAtOV1bYS16QS1aMC05LV9dezEsNjF9W2Et
ekEtWjAtOV0pKVxcXFwuKFthLXpBLVpdezIsNn18W2EtekEtWjAtOS1dezIsMzB9XFxcXC5bYS16
QS1aXXsyLDN9KSQnKVxcbiAgXFxuICBpZiByZS5tYXRjaChkbnNfbmFtZV9yZWdleCwgYXJ0aWZh
Y3RfdmFsdWUpOlxcbiAgICByZXR1cm4gXFxcIkROUyBOYW1lXFxcIlxcbiAgXFxuICByZXR1cm4g
YXJ0aWZhY3RfdHlwZVxcblxcbiMgTWFwIGlvYy50eXBlIHRvIFJlc2lsaWVudCBBcnRpZmFjdCBU
eXBlXFxuaW9jX3R5cGVfdG9fYXJ0aWZhY3RfdHlwZV9tYXAgPSB7XFxuICAgICd1cmknOiAnVVJJ
IFBhdGgnLFxcbiAgICAnSVAnOiAnSVAgQWRkcmVzcycsXFxuICAgICdtZDUnOiAnTWFsd2FyZSBN
RDUgSGFzaCcsXFxuICAgICdzaGExJzogJ01hbHdhcmUgU0hBLTEgSGFzaCcsXFxuICAgICdzaGEy
NTYnOiAnTWFsd2FyZSBTSEEtMjU2IEhhc2gnLFxcbiAgICAnQ1ZFJzogJ1RocmVhdCBDVkUgSUQn
LFxcbiAgICAnZW1haWwnOiAnRW1haWwgU2VuZGVyJyxcXG4gICAgJ2ZpbGVuYW1lJzogJ0ZpbGUg
TmFtZScsXFxuICAgICdmaWxlJzogJ0ZpbGUgTmFtZSdcXG59XFxuXFxuIyBHZXQgdGhlIElPQ3Nc
XG5pb2NzID0gcmVzdWx0cy5pb2NzXFxuXFxuaWYgaW9jczpcXG4gICAgIyBMb29wIElPQ3MgYW5k
IGFkZCBlYWNoIG9uIGFzIGFuIEFydGlmYWN0XFxuICAgIGZvciBpb2MgaW4gaW9jczpcXG4gICAg
ICBhcnRpZmFjdF9kZXNjcmlwdGlvbiA9IHVcXFwiVGhpcyBJT0Mgb2NjdXJyZWQgezB9IHRpbWUo
cykgaW4gdGhlIGFydGlmYWN0OiB7MX1cXFwiLmZvcm1hdCggdW5pY29kZShpb2MuY291bnQpLCB1
bmljb2RlKHJlc3VsdHMuYXR0YWNobWVudF9maWxlX25hbWUpIClcXG4gICAgICBhcnRpZmFjdF92
YWx1ZSA9IGlvYy52YWx1ZVxcbiAgICAgIGFydGlmYWN0X3R5cGUgPSBpb2NfdHlwZV90b19hcnRp
ZmFjdF90eXBlX21hcC5nZXQoaW9jLnR5cGUsIFxcXCJTdHJpbmdcXFwiKVxcbiAgICAgIFxcbiAg
ICAgICMgSWYgdGhlIGFydGlmYWN0X3R5cGUgaXMgJ1VSSSBQYXRoJywgY2FsbCBnZXRfYXJ0aWZh
Y3RfdHlwZSB0byB0cnkgaW50ZW50aWZ5IHRoZSB0eXBlIHVzaW5nIHJlZ2V4XFxuICAgICAgaWYg
YXJ0aWZhY3RfdHlwZSA9PSBcXFwiVVJJIFBhdGhcXFwiOlxcbiAgICAgICAgYXJ0aWZhY3RfdHlw
ZSA9IGdldF9hcnRpZmFjdF90eXBlKGFydGlmYWN0X3ZhbHVlLCBhcnRpZmFjdF90eXBlKVxcbiAg
ICAgIFxcbiAgICAgIGluY2lkZW50LmFkZEFydGlmYWN0KGFydGlmYWN0X3R5cGUsIGFydGlmYWN0
X3ZhbHVlLCBhcnRpZmFjdF9kZXNjcmlwdGlvbilcXG5cIixcInByZV9wcm9jZXNzaW5nX3Njcmlw
dFwiOlwiIyBEZWZpbmUgUHJlLVByb2Nlc3MgSW5wdXRzXFxuaW5wdXRzLmlvY19wYXJzZXJfdjJf
aW5jaWRlbnRfaWQgPSBpbmNpZGVudC5pZFxcbmlucHV0cy5pb2NfcGFyc2VyX3YyX2F0dGFjaG1l
bnRfaWQgPSBhdHRhY2htZW50LmlkXFxuXFxuIyBJZiB0aGlzIGlzIGEgVGFzaywgc2V0IHRoZSBU
YXNrIElEXFxuaWYgdGFzazpcXG4gICAgIGlucHV0cy5pb2NfcGFyc2VyX3YyX3Rhc2tfaWQgPSB0
YXNrLmlkXCJ9PC9yZXNpbGllbnQ6ZnVuY3Rpb24+PC9leHRlbnNpb25FbGVtZW50cz48aW5jb21p
bmc+U2VxdWVuY2VGbG93XzBoYmp4Nm08L2luY29taW5nPjxvdXRnb2luZz5TZXF1ZW5jZUZsb3df
MGV5cWNxbDwvb3V0Z29pbmc+PC9zZXJ2aWNlVGFzaz48ZW5kRXZlbnQgaWQ9XCJFbmRFdmVudF8x
NHBteHZmXCI+PGluY29taW5nPlNlcXVlbmNlRmxvd18wZXlxY3FsPC9pbmNvbWluZz48L2VuZEV2
ZW50PjxzZXF1ZW5jZUZsb3cgaWQ9XCJTZXF1ZW5jZUZsb3dfMGV5cWNxbFwiIHNvdXJjZVJlZj1c
IlNlcnZpY2VUYXNrXzFxYm43MG9cIiB0YXJnZXRSZWY9XCJFbmRFdmVudF8xNHBteHZmXCIvPjxz
ZXF1ZW5jZUZsb3cgaWQ9XCJTZXF1ZW5jZUZsb3dfMGhiang2bVwiIHNvdXJjZVJlZj1cIlN0YXJ0
RXZlbnRfMTU1YXN4bVwiIHRhcmdldFJlZj1cIlNlcnZpY2VUYXNrXzFxYm43MG9cIi8+PC9wcm9j
ZXNzPjxicG1uZGk6QlBNTkRpYWdyYW0gaWQ9XCJCUE1ORGlhZ3JhbV8xXCI+PGJwbW5kaTpCUE1O
UGxhbmUgYnBtbkVsZW1lbnQ9XCJ1bmRlZmluZWRcIiBpZD1cIkJQTU5QbGFuZV8xXCI+PGJwbW5k
aTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJTdGFydEV2ZW50XzE1NWFzeG1cIiBpZD1cIlN0YXJ0
RXZlbnRfMTU1YXN4bV9kaVwiPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMzZcIiB3aWR0aD1cIjM2
XCIgeD1cIjE3OVwiIHk9XCIxODhcIi8+PGJwbW5kaTpCUE1OTGFiZWw+PG9tZ2RjOkJvdW5kcyBo
ZWlnaHQ9XCIwXCIgd2lkdGg9XCI5MFwiIHg9XCIxNzRcIiB5PVwiMjIzXCIvPjwvYnBtbmRpOkJQ
TU5MYWJlbD48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9
XCJTZXJ2aWNlVGFza18xcWJuNzBvXCIgaWQ9XCJTZXJ2aWNlVGFza18xcWJuNzBvX2RpXCI+PG9t
Z2RjOkJvdW5kcyBoZWlnaHQ9XCI4MFwiIHdpZHRoPVwiMTAwXCIgeD1cIjMyOVwiIHk9XCIxNjZc
Ii8+PC9icG1uZGk6QlBNTlNoYXBlPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVtZW50PVwiRW5k
RXZlbnRfMTRwbXh2ZlwiIGlkPVwiRW5kRXZlbnRfMTRwbXh2Zl9kaVwiPjxvbWdkYzpCb3VuZHMg
aGVpZ2h0PVwiMzZcIiB3aWR0aD1cIjM2XCIgeD1cIjUyOVwiIHk9XCIxODhcIi8+PGJwbW5kaTpC
UE1OTGFiZWw+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIxM1wiIHdpZHRoPVwiMFwiIHg9XCI1NDdc
IiB5PVwiMjI3XCIvPjwvYnBtbmRpOkJQTU5MYWJlbD48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5k
aTpCUE1ORWRnZSBicG1uRWxlbWVudD1cIlNlcXVlbmNlRmxvd18wZXlxY3FsXCIgaWQ9XCJTZXF1
ZW5jZUZsb3dfMGV5cWNxbF9kaVwiPjxvbWdkaTp3YXlwb2ludCB4PVwiNDI5XCIgeHNpOnR5cGU9
XCJvbWdkYzpQb2ludFwiIHk9XCIyMDZcIi8+PG9tZ2RpOndheXBvaW50IHg9XCI1MjlcIiB4c2k6
dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIwNlwiLz48YnBtbmRpOkJQTU5MYWJlbD48b21nZGM6
Qm91bmRzIGhlaWdodD1cIjEzXCIgd2lkdGg9XCIwXCIgeD1cIjQ3OVwiIHk9XCIxODRcIi8+PC9i
cG1uZGk6QlBNTkxhYmVsPjwvYnBtbmRpOkJQTU5FZGdlPjxicG1uZGk6QlBNTkVkZ2UgYnBtbkVs
ZW1lbnQ9XCJTZXF1ZW5jZUZsb3dfMGhiang2bVwiIGlkPVwiU2VxdWVuY2VGbG93XzBoYmp4Nm1f
ZGlcIj48b21nZGk6d2F5cG9pbnQgeD1cIjIxNVwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5
PVwiMjA2XCIvPjxvbWdkaTp3YXlwb2ludCB4PVwiMzI5XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2lu
dFwiIHk9XCIyMDZcIi8+PGJwbW5kaTpCUE1OTGFiZWw+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIx
M1wiIHdpZHRoPVwiMFwiIHg9XCIyNzJcIiB5PVwiMTg0LjVcIi8+PC9icG1uZGk6QlBNTkxhYmVs
PjwvYnBtbmRpOkJQTU5FZGdlPjwvYnBtbmRpOkJQTU5QbGFuZT48L2JwbW5kaTpCUE1ORGlhZ3Jh
bT48L2RlZmluaXRpb25zPiIsICJ3b3JrZmxvd19pZCI6ICJleGFtcGxlX3BhcnNlX2lvY3NfYXR0
YWNobWVudCIsICJ2ZXJzaW9uIjogN30sICJsYXN0X21vZGlmaWVkX3RpbWUiOiAxNTYzODExNzkz
NzQ2LCAiY3JlYXRvcl9pZCI6ICJhZG1pbkBleGFtcGxlLmNvbSIsICJhY3Rpb25zIjogW10sICJw
cm9ncmFtbWF0aWNfbmFtZSI6ICJleGFtcGxlX3BhcnNlX2lvY3NfYXR0YWNobWVudCIsICJuYW1l
IjogIkV4YW1wbGU6IFBhcnNlIElPQ3MgKEF0dGFjaG1lbnQpIn0sIHsidXVpZCI6ICI3YWQ4ZTIx
MC1jNDdlLTQ3MjUtOThiZC00NzgyNDBmZmYwZjkiLCAiZGVzY3JpcHRpb24iOiAiRXhhbXBsZSB3
b3JrZmxvdyBzaG93aW5nIGhvdyB0byBleHRyYWN0IElPQydzIChJbmRpY2F0b3JzIG9mIENvbXBy
b21pc2UpIGZyb20gYW4gQXJ0aWZhY3QgRmlsZSBvciBUZXh0LUJhc2VkIEFydGlmYWN0LiBFYWNo
IHVuaXF1ZSBJT0MgaXMgYWRkZWQgdG8gdGhlIEluY2lkZW50IGFzIGFuIEFydGlmYWN0LiIsICJv
YmplY3RfdHlwZSI6ICJhcnRpZmFjdCIsICJleHBvcnRfa2V5IjogImV4YW1wbGVfcGFyc2VfaW9j
c19hcnRpZmFjdCIsICJ3b3JrZmxvd19pZCI6IDI0LCAibGFzdF9tb2RpZmllZF9ieSI6ICJhZG1p
bkBleGFtcGxlLmNvbSIsICJjb250ZW50IjogeyJ4bWwiOiAiPD94bWwgdmVyc2lvbj1cIjEuMFwi
IGVuY29kaW5nPVwiVVRGLThcIj8+PGRlZmluaXRpb25zIHhtbG5zPVwiaHR0cDovL3d3dy5vbWcu
b3JnL3NwZWMvQlBNTi8yMDEwMDUyNC9NT0RFTFwiIHhtbG5zOmJwbW5kaT1cImh0dHA6Ly93d3cu
b21nLm9yZy9zcGVjL0JQTU4vMjAxMDA1MjQvRElcIiB4bWxuczpvbWdkYz1cImh0dHA6Ly93d3cu
b21nLm9yZy9zcGVjL0RELzIwMTAwNTI0L0RDXCIgeG1sbnM6b21nZGk9XCJodHRwOi8vd3d3Lm9t
Zy5vcmcvc3BlYy9ERC8yMDEwMDUyNC9ESVwiIHhtbG5zOnJlc2lsaWVudD1cImh0dHA6Ly9yZXNp
bGllbnQuaWJtLmNvbS9icG1uXCIgeG1sbnM6eHNkPVwiaHR0cDovL3d3dy53My5vcmcvMjAwMS9Y
TUxTY2hlbWFcIiB4bWxuczp4c2k9XCJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYS1p
bnN0YW5jZVwiIHRhcmdldE5hbWVzcGFjZT1cImh0dHA6Ly93d3cuY2FtdW5kYS5vcmcvdGVzdFwi
Pjxwcm9jZXNzIGlkPVwiZXhhbXBsZV9wYXJzZV9pb2NzX2FydGlmYWN0XCIgaXNFeGVjdXRhYmxl
PVwidHJ1ZVwiIG5hbWU9XCJFeGFtcGxlOiBQYXJzZSBJT0NzIChBcnRpZmFjdClcIj48ZG9jdW1l
bnRhdGlvbj48IVtDREFUQVtFeGFtcGxlIHdvcmtmbG93IHNob3dpbmcgaG93IHRvIGV4dHJhY3Qg
SU9DJ3MgKEluZGljYXRvcnMgb2YgQ29tcHJvbWlzZSkgZnJvbSBhbiBBcnRpZmFjdCBGaWxlIG9y
IFRleHQtQmFzZWQgQXJ0aWZhY3QuIEVhY2ggdW5pcXVlIElPQyBpcyBhZGRlZCB0byB0aGUgSW5j
aWRlbnQgYXMgYW4gQXJ0aWZhY3QuXV0+PC9kb2N1bWVudGF0aW9uPjxzdGFydEV2ZW50IGlkPVwi
U3RhcnRFdmVudF8xNTVhc3htXCI+PG91dGdvaW5nPlNlcXVlbmNlRmxvd18wMGpyczR1PC9vdXRn
b2luZz48L3N0YXJ0RXZlbnQ+PHNlcnZpY2VUYXNrIGlkPVwiU2VydmljZVRhc2tfMDhzdjl2ZFwi
IG5hbWU9XCJJT0MgUGFyc2VyIHYyXCIgcmVzaWxpZW50OnR5cGU9XCJmdW5jdGlvblwiPjxleHRl
bnNpb25FbGVtZW50cz48cmVzaWxpZW50OmZ1bmN0aW9uIHV1aWQ9XCI1MjgwMzU4MS0wMTlhLTRj
NjgtOGY4ZC04YmU5Y2EzMWIyZjZcIj57XCJpbnB1dHNcIjp7fSxcInBvc3RfcHJvY2Vzc2luZ19z
Y3JpcHRcIjpcImltcG9ydCByZVxcblxcbmRlZiBnZXRfYXJ0aWZhY3RfdHlwZShhcnRpZmFjdF92
YWx1ZSwgYXJ0aWZhY3RfdHlwZSk6XFxuICBcXFwiXFxcIlxcXCJVc2Ugc29tZSByZWdleCBleHBy
ZXNzaW9ucyB0byB0cnkgYW5kIGlkZW50aWZ5XFxuICBmcm9tIHRoZSBBcnRpZmFjdCdzIHZhbHVl
LCB3aGF0IEFydGlmYWN0IHR5cGUgaXQgaXMuXFxuICBSZXR1cm4gb3JpZ2luYWwgYXJ0aWZhY3Rf
dHlwZSBpZiB3ZSBjYW5ub3QgZmlndXJlIGl0IG91dFxcXCJcXFwiXFxcIlxcblxcbiAgZG5zX25h
bWVfcmVnZXggPSByZS5jb21waWxlKHInXigoW2EtekEtWl17MX0pfChbYS16QS1aXXsxfVthLXpB
LVpdezF9KXwoW2EtekEtWl17MX1bMC05XXsxfSl8KFswLTldezF9W2EtekEtWl17MX0pfChbYS16
QS1aMC05XVthLXpBLVowLTktX117MSw2MX1bYS16QS1aMC05XSkpXFxcXC4oW2EtekEtWl17Miw2
fXxbYS16QS1aMC05LV17MiwzMH1cXFxcLlthLXpBLVpdezIsM30pJCcpXFxuICBcXG4gIGlmIHJl
Lm1hdGNoKGRuc19uYW1lX3JlZ2V4LCBhcnRpZmFjdF92YWx1ZSk6XFxuICAgIHJldHVybiBcXFwi
RE5TIE5hbWVcXFwiXFxuICBcXG4gIHJldHVybiBhcnRpZmFjdF90eXBlXFxuXFxuIyBNYXAgaW9j
LnR5cGUgdG8gUmVzaWxpZW50IEFydGlmYWN0IFR5cGVcXG5pb2NfdHlwZV90b19hcnRpZmFjdF90
eXBlX21hcCA9IHtcXG4gICAgJ3VyaSc6ICdVUkkgUGF0aCcsXFxuICAgICdJUCc6ICdJUCBBZGRy
ZXNzJyxcXG4gICAgJ21kNSc6ICdNYWx3YXJlIE1ENSBIYXNoJyxcXG4gICAgJ3NoYTEnOiAnTWFs
d2FyZSBTSEEtMSBIYXNoJyxcXG4gICAgJ3NoYTI1Nic6ICdNYWx3YXJlIFNIQS0yNTYgSGFzaCcs
XFxuICAgICdDVkUnOiAnVGhyZWF0IENWRSBJRCcsXFxuICAgICdlbWFpbCc6ICdFbWFpbCBTZW5k
ZXInLFxcbiAgICAnZmlsZW5hbWUnOiAnRmlsZSBOYW1lJyxcXG4gICAgJ2ZpbGUnOiAnRmlsZSBO
YW1lJ1xcbn1cXG5cXG4jIEdldCB0aGUgSU9Dc1xcbmlvY3MgPSByZXN1bHRzLmlvY3NcXG5cXG5p
ZiBpb2NzOlxcbiAgICAjIExvb3AgSU9DcyBhbmQgYWRkIGVhY2ggb24gYXMgYW4gQXJ0aWZhY3Rc
XG4gICAgZm9yIGlvYyBpbiBpb2NzOlxcbiAgICAgIFxcbiAgICAgICMgSWYgYXR0YWNobWVudF9m
aWxlX25hbWUgaXMgbm90IGRlZmluZWQsIHVzZSB0aGUgaW9jLnZhbHVlIGFzIGluIHRoZSBBcnRp
ZmFjdCdzIERlc2NyaXB0aW9uXFxuICAgICAgaWYgcmVzdWx0cy5hdHRhY2htZW50X2ZpbGVfbmFt
ZTpcXG4gICAgICAgIGFydGlmYWN0X2Rlc2NyaXB0aW9uID0gdVxcXCJUaGlzIElPQyBvY2N1cnJl
ZCB7MH0gdGltZShzKSBpbiB0aGUgYXJ0aWZhY3Q6IHsxfVxcXCIuZm9ybWF0KCB1bmljb2RlKGlv
Yy5jb3VudCksIHVuaWNvZGUocmVzdWx0cy5hdHRhY2htZW50X2ZpbGVfbmFtZSkgKVxcbiAgICAg
IFxcbiAgICAgIGVsc2U6XFxuICAgICAgICBhcnRpZmFjdF9kZXNjcmlwdGlvbiA9IHVcXFwiVGhp
cyBJT0Mgb2NjdXJyZWQgezB9IHRpbWUocykgaW4gdGhlIGFydGlmYWN0OiB7MX1cXFwiLmZvcm1h
dCggdW5pY29kZShpb2MuY291bnQpLCB1bmljb2RlKGlvYy52YWx1ZSkgKVxcblxcbiAgICAgIGFy
dGlmYWN0X3ZhbHVlID0gaW9jLnZhbHVlXFxuICAgICAgYXJ0aWZhY3RfdHlwZSA9IGlvY190eXBl
X3RvX2FydGlmYWN0X3R5cGVfbWFwLmdldChpb2MudHlwZSwgXFxcIlN0cmluZ1xcXCIpXFxuICAg
ICAgXFxuICAgICAgIyBJZiB0aGUgYXJ0aWZhY3RfdHlwZSBpcyAnVVJJIFBhdGgnLCBjYWxsIGdl
dF9hcnRpZmFjdF90eXBlIHRvIHRyeSBpbnRlbnRpZnkgdGhlIHR5cGUgdXNpbmcgcmVnZXhcXG4g
ICAgICBpZiBhcnRpZmFjdF90eXBlID09IFxcXCJVUkkgUGF0aFxcXCI6XFxuICAgICAgICBhcnRp
ZmFjdF90eXBlID0gZ2V0X2FydGlmYWN0X3R5cGUoYXJ0aWZhY3RfdmFsdWUsIGFydGlmYWN0X3R5
cGUpXFxuICAgICAgXFxuICAgICAgaW5jaWRlbnQuYWRkQXJ0aWZhY3QoYXJ0aWZhY3RfdHlwZSwg
YXJ0aWZhY3RfdmFsdWUsIGFydGlmYWN0X2Rlc2NyaXB0aW9uKVxcblwiLFwicHJlX3Byb2Nlc3Np
bmdfc2NyaXB0XCI6XCIjIERlZmluZSBQcmUtUHJvY2VzcyBJbnB1dHNcXG5pbnB1dHMuaW9jX3Bh
cnNlcl92Ml9pbmNpZGVudF9pZCA9IGluY2lkZW50LmlkXFxuaW5wdXRzLmlvY19wYXJzZXJfdjJf
YXJ0aWZhY3RfaWQgPSBhcnRpZmFjdC5pZFxcbmlucHV0cy5pb2NfcGFyc2VyX3YyX2FydGlmYWN0
X3ZhbHVlID0gYXJ0aWZhY3QudmFsdWVcIn08L3Jlc2lsaWVudDpmdW5jdGlvbj48L2V4dGVuc2lv
bkVsZW1lbnRzPjxpbmNvbWluZz5TZXF1ZW5jZUZsb3dfMDBqcnM0dTwvaW5jb21pbmc+PG91dGdv
aW5nPlNlcXVlbmNlRmxvd18wajl2cWc1PC9vdXRnb2luZz48L3NlcnZpY2VUYXNrPjxzZXF1ZW5j
ZUZsb3cgaWQ9XCJTZXF1ZW5jZUZsb3dfMDBqcnM0dVwiIHNvdXJjZVJlZj1cIlN0YXJ0RXZlbnRf
MTU1YXN4bVwiIHRhcmdldFJlZj1cIlNlcnZpY2VUYXNrXzA4c3Y5dmRcIi8+PGVuZEV2ZW50IGlk
PVwiRW5kRXZlbnRfMGZoMXlpaFwiPjxpbmNvbWluZz5TZXF1ZW5jZUZsb3dfMGo5dnFnNTwvaW5j
b21pbmc+PC9lbmRFdmVudD48c2VxdWVuY2VGbG93IGlkPVwiU2VxdWVuY2VGbG93XzBqOXZxZzVc
IiBzb3VyY2VSZWY9XCJTZXJ2aWNlVGFza18wOHN2OXZkXCIgdGFyZ2V0UmVmPVwiRW5kRXZlbnRf
MGZoMXlpaFwiLz48L3Byb2Nlc3M+PGJwbW5kaTpCUE1ORGlhZ3JhbSBpZD1cIkJQTU5EaWFncmFt
XzFcIj48YnBtbmRpOkJQTU5QbGFuZSBicG1uRWxlbWVudD1cInVuZGVmaW5lZFwiIGlkPVwiQlBN
TlBsYW5lXzFcIj48YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIlN0YXJ0RXZlbnRfMTU1
YXN4bVwiIGlkPVwiU3RhcnRFdmVudF8xNTVhc3htX2RpXCI+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9
XCIzNlwiIHdpZHRoPVwiMzZcIiB4PVwiMTYyXCIgeT1cIjE4OFwiLz48YnBtbmRpOkJQTU5MYWJl
bD48b21nZGM6Qm91bmRzIGhlaWdodD1cIjBcIiB3aWR0aD1cIjkwXCIgeD1cIjE1N1wiIHk9XCIy
MjNcIi8+PC9icG1uZGk6QlBNTkxhYmVsPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5T
aGFwZSBicG1uRWxlbWVudD1cIlNlcnZpY2VUYXNrXzA4c3Y5dmRcIiBpZD1cIlNlcnZpY2VUYXNr
XzA4c3Y5dmRfZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjgwXCIgd2lkdGg9XCIxMDBcIiB4
PVwiMzQ5XCIgeT1cIjE2NlwiLz48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1ORWRnZSBi
cG1uRWxlbWVudD1cIlNlcXVlbmNlRmxvd18wMGpyczR1XCIgaWQ9XCJTZXF1ZW5jZUZsb3dfMDBq
cnM0dV9kaVwiPjxvbWdkaTp3YXlwb2ludCB4PVwiMTk4XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2lu
dFwiIHk9XCIyMDZcIi8+PG9tZ2RpOndheXBvaW50IHg9XCIzNDlcIiB4c2k6dHlwZT1cIm9tZ2Rj
OlBvaW50XCIgeT1cIjIwNlwiLz48YnBtbmRpOkJQTU5MYWJlbD48b21nZGM6Qm91bmRzIGhlaWdo
dD1cIjEzXCIgd2lkdGg9XCIwXCIgeD1cIjI3My41XCIgeT1cIjE4NFwiLz48L2JwbW5kaTpCUE1O
TGFiZWw+PC9icG1uZGk6QlBNTkVkZ2U+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJF
bmRFdmVudF8wZmgxeWloXCIgaWQ9XCJFbmRFdmVudF8wZmgxeWloX2RpXCI+PG9tZ2RjOkJvdW5k
cyBoZWlnaHQ9XCIzNlwiIHdpZHRoPVwiMzZcIiB4PVwiNTg4XCIgeT1cIjE4OFwiLz48YnBtbmRp
OkJQTU5MYWJlbD48b21nZGM6Qm91bmRzIGhlaWdodD1cIjEzXCIgd2lkdGg9XCIwXCIgeD1cIjYw
NlwiIHk9XCIyMjdcIi8+PC9icG1uZGk6QlBNTkxhYmVsPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBt
bmRpOkJQTU5FZGdlIGJwbW5FbGVtZW50PVwiU2VxdWVuY2VGbG93XzBqOXZxZzVcIiBpZD1cIlNl
cXVlbmNlRmxvd18wajl2cWc1X2RpXCI+PG9tZ2RpOndheXBvaW50IHg9XCI0NDlcIiB4c2k6dHlw
ZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIwNlwiLz48b21nZGk6d2F5cG9pbnQgeD1cIjU4OFwiIHhz
aTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjA2XCIvPjxicG1uZGk6QlBNTkxhYmVsPjxvbWdk
YzpCb3VuZHMgaGVpZ2h0PVwiMTNcIiB3aWR0aD1cIjBcIiB4PVwiNTE4LjVcIiB5PVwiMTg0XCIv
PjwvYnBtbmRpOkJQTU5MYWJlbD48L2JwbW5kaTpCUE1ORWRnZT48L2JwbW5kaTpCUE1OUGxhbmU+
PC9icG1uZGk6QlBNTkRpYWdyYW0+PC9kZWZpbml0aW9ucz4iLCAid29ya2Zsb3dfaWQiOiAiZXhh
bXBsZV9wYXJzZV9pb2NzX2FydGlmYWN0IiwgInZlcnNpb24iOiA3fSwgImxhc3RfbW9kaWZpZWRf
dGltZSI6IDE1NjM4MTE3Njc0OTIsICJjcmVhdG9yX2lkIjogImFkbWluQGV4YW1wbGUuY29tIiwg
ImFjdGlvbnMiOiBbXSwgInByb2dyYW1tYXRpY19uYW1lIjogImV4YW1wbGVfcGFyc2VfaW9jc19h
cnRpZmFjdCIsICJuYW1lIjogIkV4YW1wbGU6IFBhcnNlIElPQ3MgKEFydGlmYWN0KSJ9XSwgImFj
dGlvbnMiOiBbeyJsb2dpY190eXBlIjogImFsbCIsICJuYW1lIjogIkV4YW1wbGU6IFBhcnNlIElP
Q3MgKEFydGlmYWN0KSIsICJ2aWV3X2l0ZW1zIjogW10sICJ0eXBlIjogMSwgIndvcmtmbG93cyI6
IFsiZXhhbXBsZV9wYXJzZV9pb2NzX2FydGlmYWN0Il0sICJvYmplY3RfdHlwZSI6ICJhcnRpZmFj
dCIsICJ0aW1lb3V0X3NlY29uZHMiOiA4NjQwMCwgInV1aWQiOiAiYjVjZTQ1ZDAtYjU1Mi00YmI3
LThkNGItNDRjYTFmZjcyMjgwIiwgImF1dG9tYXRpb25zIjogW10sICJleHBvcnRfa2V5IjogIkV4
YW1wbGU6IFBhcnNlIElPQ3MgKEFydGlmYWN0KSIsICJjb25kaXRpb25zIjogW3sidHlwZSI6IG51
bGwsICJldmFsdWF0aW9uX2lkIjogbnVsbCwgImZpZWxkX25hbWUiOiAiYXJ0aWZhY3QudHlwZSIs
ICJtZXRob2QiOiAiaW4iLCAidmFsdWUiOiBbIlJGQyA4MjIgRW1haWwgTWVzc2FnZSBGaWxlIiwg
IkVtYWlsIEF0dGFjaG1lbnQiLCAiTG9nIEZpbGUiLCAiT3RoZXIgRmlsZSIsICJTdHJpbmciXX1d
LCAiaWQiOiAzNiwgIm1lc3NhZ2VfZGVzdGluYXRpb25zIjogW119LCB7ImxvZ2ljX3R5cGUiOiAi
YWxsIiwgIm5hbWUiOiAiRXhhbXBsZTogUGFyc2UgSU9DcyAoQXR0YWNobWVudCkiLCAidmlld19p
dGVtcyI6IFtdLCAidHlwZSI6IDEsICJ3b3JrZmxvd3MiOiBbImV4YW1wbGVfcGFyc2VfaW9jc19h
dHRhY2htZW50Il0sICJvYmplY3RfdHlwZSI6ICJhdHRhY2htZW50IiwgInRpbWVvdXRfc2Vjb25k
cyI6IDg2NDAwLCAidXVpZCI6ICI2ZWYwYjQwMS1mOThkLTQzYTMtYjhlMC1hMjkwODZiZmQxZTgi
LCAiYXV0b21hdGlvbnMiOiBbXSwgImV4cG9ydF9rZXkiOiAiRXhhbXBsZTogUGFyc2UgSU9DcyAo
QXR0YWNobWVudCkiLCAiY29uZGl0aW9ucyI6IFtdLCAiaWQiOiAzNywgIm1lc3NhZ2VfZGVzdGlu
YXRpb25zIjogW119XSwgImxheW91dHMiOiBbXSwgImV4cG9ydF9mb3JtYXRfdmVyc2lvbiI6IDIs
ICJpZCI6IDQsICJpbmR1c3RyaWVzIjogbnVsbCwgInBoYXNlcyI6IFtdLCAiYWN0aW9uX29yZGVy
IjogW10sICJnZW9zIjogbnVsbCwgImxvY2FsZSI6IG51bGwsICJzZXJ2ZXJfdmVyc2lvbiI6IHsi
bWFqb3IiOiAzMSwgInZlcnNpb24iOiAiMzEuMC40MjU0IiwgImJ1aWxkX251bWJlciI6IDQyNTQs
ICJtaW5vciI6IDB9LCAidGltZWZyYW1lcyI6IG51bGwsICJ3b3Jrc3BhY2VzIjogW10sICJhdXRv
bWF0aWNfdGFza3MiOiBbXSwgImZ1bmN0aW9ucyI6IFt7ImRpc3BsYXlfbmFtZSI6ICJJT0MgUGFy
c2VyIHYyIiwgImRlc2NyaXB0aW9uIjogeyJjb250ZW50IjogIkV4dHJhY3QgSU9DcyBmcm9tIElu
Y2lkZW50L1Rhc2sgQXR0YWNobWVudHMsIFRleHQtQmFzZWQgQXJ0aWZhY3RzIGFuZCBBcnRpZmFj
dCBmaWxlcy4iLCAiZm9ybWF0IjogInRleHQifSwgImNyZWF0b3IiOiB7ImRpc3BsYXlfbmFtZSI6
ICJBZG1pbiBVc2VyIiwgInR5cGUiOiAidXNlciIsICJpZCI6IDcxLCAibmFtZSI6ICJhZG1pbkBl
eGFtcGxlLmNvbSJ9LCAidmlld19pdGVtcyI6IFt7InNob3dfaWYiOiBudWxsLCAiZmllbGRfdHlw
ZSI6ICJfX2Z1bmN0aW9uIiwgInNob3dfbGlua19oZWFkZXIiOiBmYWxzZSwgImVsZW1lbnQiOiAi
ZmllbGRfdXVpZCIsICJjb250ZW50IjogImRjYzljODg0LTI3NDItNGYxNy1hMGRlLTU2MjRiNjhi
N2IxMyIsICJzdGVwX2xhYmVsIjogbnVsbH0sIHsic2hvd19pZiI6IG51bGwsICJmaWVsZF90eXBl
IjogIl9fZnVuY3Rpb24iLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAiZWxlbWVudCI6ICJm
aWVsZF91dWlkIiwgImNvbnRlbnQiOiAiZGVkOTBkMTUtNDUyMS00NWQzLTljNGEtMmIxN2E0MmU5
N2VjIiwgInN0ZXBfbGFiZWwiOiBudWxsfSwgeyJzaG93X2lmIjogbnVsbCwgImZpZWxkX3R5cGUi
OiAiX19mdW5jdGlvbiIsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2UsICJlbGVtZW50IjogImZp
ZWxkX3V1aWQiLCAiY29udGVudCI6ICIxNjFjMzM1OS1lN2UzLTRiNDktYjM0Yy02ZjM5MDEyNmE5
ZDEiLCAic3RlcF9sYWJlbCI6IG51bGx9LCB7InNob3dfaWYiOiBudWxsLCAiZmllbGRfdHlwZSI6
ICJfX2Z1bmN0aW9uIiwgInNob3dfbGlua19oZWFkZXIiOiBmYWxzZSwgImVsZW1lbnQiOiAiZmll
bGRfdXVpZCIsICJjb250ZW50IjogIjZlNjRjYjkxLTlhOWUtNDhkNS05ZjA4LWY0ODliZTU0YzMw
YiIsICJzdGVwX2xhYmVsIjogbnVsbH0sIHsic2hvd19pZiI6IG51bGwsICJmaWVsZF90eXBlIjog
Il9fZnVuY3Rpb24iLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAiZWxlbWVudCI6ICJmaWVs
ZF91dWlkIiwgImNvbnRlbnQiOiAiNWFiYzhhZGUtYTJkZS00Y2E0LTg1MzgtZWNjNGE1NDE1MmQz
IiwgInN0ZXBfbGFiZWwiOiBudWxsfV0sICJleHBvcnRfa2V5IjogImZ1bmNfaW9jX3BhcnNlcl92
MiIsICJ1dWlkIjogIjUyODAzNTgxLTAxOWEtNGM2OC04ZjhkLThiZTljYTMxYjJmNiIsICJsYXN0
X21vZGlmaWVkX2J5IjogeyJkaXNwbGF5X25hbWUiOiAiQWRtaW4gVXNlciIsICJ0eXBlIjogInVz
ZXIiLCAiaWQiOiA3MSwgIm5hbWUiOiAiYWRtaW5AZXhhbXBsZS5jb20ifSwgInZlcnNpb24iOiA0
LCAid29ya2Zsb3dzIjogW3siZGVzY3JpcHRpb24iOiBudWxsLCAib2JqZWN0X3R5cGUiOiAiYXJ0
aWZhY3QiLCAiYWN0aW9ucyI6IFtdLCAibmFtZSI6ICJFeGFtcGxlOiBQYXJzZSBJT0NzIChBcnRp
ZmFjdCkiLCAid29ya2Zsb3dfaWQiOiAyNCwgInByb2dyYW1tYXRpY19uYW1lIjogImV4YW1wbGVf
cGFyc2VfaW9jc19hcnRpZmFjdCIsICJ1dWlkIjogbnVsbH0sIHsiZGVzY3JpcHRpb24iOiBudWxs
LCAib2JqZWN0X3R5cGUiOiAiYXR0YWNobWVudCIsICJhY3Rpb25zIjogW10sICJuYW1lIjogIkV4
YW1wbGU6IFBhcnNlIElPQ3MgKEF0dGFjaG1lbnQpIiwgIndvcmtmbG93X2lkIjogMjMsICJwcm9n
cmFtbWF0aWNfbmFtZSI6ICJleGFtcGxlX3BhcnNlX2lvY3NfYXR0YWNobWVudCIsICJ1dWlkIjog
bnVsbH1dLCAibGFzdF9tb2RpZmllZF90aW1lIjogMTU2MzgwMTYwNzA1NywgImRlc3RpbmF0aW9u
X2hhbmRsZSI6ICJmbl9pb2NfcGFyc2VyX3YyIiwgImlkIjogNTUsICJuYW1lIjogImZ1bmNfaW9j
X3BhcnNlcl92MiJ9XSwgIm5vdGlmaWNhdGlvbnMiOiBudWxsLCAicmVndWxhdG9ycyI6IG51bGws
ICJpbmNpZGVudF90eXBlcyI6IFt7ImNyZWF0ZV9kYXRlIjogMTU2MzgxMTg0NDY4MiwgImRlc2Ny
aXB0aW9uIjogIkN1c3RvbWl6YXRpb24gUGFja2FnZXMgKGludGVybmFsKSIsICJleHBvcnRfa2V5
IjogIkN1c3RvbWl6YXRpb24gUGFja2FnZXMgKGludGVybmFsKSIsICJpZCI6IDAsICJuYW1lIjog
IkN1c3RvbWl6YXRpb24gUGFja2FnZXMgKGludGVybmFsKSIsICJ1cGRhdGVfZGF0ZSI6IDE1NjM4
MTE4NDQ2ODIsICJ1dWlkIjogImJmZWVjMmQ0LTM3NzAtMTFlOC1hZDM5LTRhMDAwNDA0NGFhMCIs
ICJlbmFibGVkIjogZmFsc2UsICJzeXN0ZW0iOiBmYWxzZSwgInBhcmVudF9pZCI6IG51bGwsICJo
aWRkZW4iOiBmYWxzZX1dLCAic2NyaXB0cyI6IFtdLCAidHlwZXMiOiBbXSwgIm1lc3NhZ2VfZGVz
dGluYXRpb25zIjogW3sidXVpZCI6ICIzNzdlY2QzZC1kZTg3LTQ4YTQtODlmZi1hNjI2Y2I3OGE0
MDEiLCAiZXhwb3J0X2tleSI6ICJmbl9pb2NfcGFyc2VyX3YyIiwgIm5hbWUiOiAiZm5faW9jX3Bh
cnNlcl92MiIsICJkZXN0aW5hdGlvbl90eXBlIjogMCwgInByb2dyYW1tYXRpY19uYW1lIjogImZu
X2lvY19wYXJzZXJfdjIiLCAiZXhwZWN0X2FjayI6IHRydWUsICJ1c2VycyI6IFsiaW50ZWdyYXRp
b25zQGV4YW1wbGUuY29tIl19XSwgImluY2lkZW50X2FydGlmYWN0X3R5cGVzIjogW10sICJyb2xl
cyI6IFtdLCAiZmllbGRzIjogW3sib3BlcmF0aW9ucyI6IFtdLCAidHlwZV9pZCI6IDAsICJvcGVy
YXRpb25fcGVybXMiOiB7fSwgInRleHQiOiAiU2ltdWxhdGlvbiIsICJibGFua19vcHRpb24iOiBm
YWxzZSwgInByZWZpeCI6IG51bGwsICJjaGFuZ2VhYmxlIjogdHJ1ZSwgImlkIjogMzgsICJyZWFk
X29ubHkiOiB0cnVlLCAidXVpZCI6ICJjM2YwZTNlZC0yMWUxLTRkNTMtYWZmYi1mZTVjYTMzMDhj
Y2EiLCAiY2hvc2VuIjogZmFsc2UsICJpbnB1dF90eXBlIjogImJvb2xlYW4iLCAidG9vbHRpcCI6
ICJXaGV0aGVyIHRoZSBpbmNpZGVudCBpcyBhIHNpbXVsYXRpb24gb3IgYSByZWd1bGFyIGluY2lk
ZW50LiAgVGhpcyBmaWVsZCBpcyByZWFkLW9ubHkuIiwgImludGVybmFsIjogZmFsc2UsICJyaWNo
X3RleHQiOiBmYWxzZSwgInRlbXBsYXRlcyI6IFtdLCAiZXhwb3J0X2tleSI6ICJpbmNpZGVudC9p
bmNfdHJhaW5pbmciLCAiaGlkZV9ub3RpZmljYXRpb24iOiBmYWxzZSwgIm5hbWUiOiAiaW5jX3Ry
YWluaW5nIiwgImRlcHJlY2F0ZWQiOiBmYWxzZSwgImRlZmF1bHRfY2hvc2VuX2J5X3NlcnZlciI6
IGZhbHNlLCAidmFsdWVzIjogW119LCB7Im9wZXJhdGlvbnMiOiBbXSwgInR5cGVfaWQiOiAxMSwg
Im9wZXJhdGlvbl9wZXJtcyI6IHt9LCAidGV4dCI6ICJpb2NfcGFyc2VyX3YyX3Rhc2tfaWQiLCAi
Ymxhbmtfb3B0aW9uIjogZmFsc2UsICJwcmVmaXgiOiBudWxsLCAiY2hhbmdlYWJsZSI6IHRydWUs
ICJpZCI6IDIxOSwgInJlYWRfb25seSI6IGZhbHNlLCAidXVpZCI6ICI1YWJjOGFkZS1hMmRlLTRj
YTQtODUzOC1lY2M0YTU0MTUyZDMiLCAiY2hvc2VuIjogZmFsc2UsICJpbnB1dF90eXBlIjogIm51
bWJlciIsICJ0b29sdGlwIjogIklEIG9mIHRoZSB0YXNrIiwgImludGVybmFsIjogZmFsc2UsICJy
aWNoX3RleHQiOiBmYWxzZSwgInRlbXBsYXRlcyI6IFtdLCAiZXhwb3J0X2tleSI6ICJfX2Z1bmN0
aW9uL2lvY19wYXJzZXJfdjJfdGFza19pZCIsICJoaWRlX25vdGlmaWNhdGlvbiI6IGZhbHNlLCAi
cGxhY2Vob2xkZXIiOiAiIiwgIm5hbWUiOiAiaW9jX3BhcnNlcl92Ml90YXNrX2lkIiwgImRlcHJl
Y2F0ZWQiOiBmYWxzZSwgImRlZmF1bHRfY2hvc2VuX2J5X3NlcnZlciI6IGZhbHNlLCAidmFsdWVz
IjogW119LCB7Im9wZXJhdGlvbnMiOiBbXSwgInR5cGVfaWQiOiAxMSwgIm9wZXJhdGlvbl9wZXJt
cyI6IHt9LCAidGV4dCI6ICJpb2NfcGFyc2VyX3YyX2luY2lkZW50X2lkIiwgImJsYW5rX29wdGlv
biI6IGZhbHNlLCAicHJlZml4IjogbnVsbCwgImNoYW5nZWFibGUiOiB0cnVlLCAiaWQiOiAyMjAs
ICJyZWFkX29ubHkiOiBmYWxzZSwgInV1aWQiOiAiZGNjOWM4ODQtMjc0Mi00ZjE3LWEwZGUtNTYy
NGI2OGI3YjEzIiwgImNob3NlbiI6IGZhbHNlLCAiaW5wdXRfdHlwZSI6ICJudW1iZXIiLCAidG9v
bHRpcCI6ICJJRCBvZiB0aGUgaW5jaWRlbnQiLCAiaW50ZXJuYWwiOiBmYWxzZSwgInJpY2hfdGV4
dCI6IGZhbHNlLCAidGVtcGxhdGVzIjogW10sICJleHBvcnRfa2V5IjogIl9fZnVuY3Rpb24vaW9j
X3BhcnNlcl92Ml9pbmNpZGVudF9pZCIsICJoaWRlX25vdGlmaWNhdGlvbiI6IGZhbHNlLCAicGxh
Y2Vob2xkZXIiOiAiIiwgIm5hbWUiOiAiaW9jX3BhcnNlcl92Ml9pbmNpZGVudF9pZCIsICJkZXBy
ZWNhdGVkIjogZmFsc2UsICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZSwgInZhbHVl
cyI6IFtdfSwgeyJvcGVyYXRpb25zIjogW10sICJ0eXBlX2lkIjogMTEsICJvcGVyYXRpb25fcGVy
bXMiOiB7fSwgInRleHQiOiAiaW9jX3BhcnNlcl92Ml9hcnRpZmFjdF92YWx1ZSIsICJibGFua19v
cHRpb24iOiBmYWxzZSwgInByZWZpeCI6IG51bGwsICJjaGFuZ2VhYmxlIjogdHJ1ZSwgImlkIjog
MjE2LCAicmVhZF9vbmx5IjogZmFsc2UsICJ1dWlkIjogIjE2MWMzMzU5LWU3ZTMtNGI0OS1iMzRj
LTZmMzkwMTI2YTlkMSIsICJjaG9zZW4iOiBmYWxzZSwgImlucHV0X3R5cGUiOiAidGV4dCIsICJ0
b29sdGlwIjogIkFydGlmYWN0J3MgdmFsdWUiLCAiaW50ZXJuYWwiOiBmYWxzZSwgInJpY2hfdGV4
dCI6IGZhbHNlLCAidGVtcGxhdGVzIjogW10sICJleHBvcnRfa2V5IjogIl9fZnVuY3Rpb24vaW9j
X3BhcnNlcl92Ml9hcnRpZmFjdF92YWx1ZSIsICJoaWRlX25vdGlmaWNhdGlvbiI6IGZhbHNlLCAi
cGxhY2Vob2xkZXIiOiAiIiwgIm5hbWUiOiAiaW9jX3BhcnNlcl92Ml9hcnRpZmFjdF92YWx1ZSIs
ICJkZXByZWNhdGVkIjogZmFsc2UsICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZSwg
InZhbHVlcyI6IFtdfSwgeyJvcGVyYXRpb25zIjogW10sICJ0eXBlX2lkIjogMTEsICJvcGVyYXRp
b25fcGVybXMiOiB7fSwgInRleHQiOiAiaW9jX3BhcnNlcl92Ml9hcnRpZmFjdF9pZCIsICJibGFu
a19vcHRpb24iOiBmYWxzZSwgInByZWZpeCI6IG51bGwsICJjaGFuZ2VhYmxlIjogdHJ1ZSwgImlk
IjogMjE1LCAicmVhZF9vbmx5IjogZmFsc2UsICJ1dWlkIjogImRlZDkwZDE1LTQ1MjEtNDVkMy05
YzRhLTJiMTdhNDJlOTdlYyIsICJjaG9zZW4iOiBmYWxzZSwgImlucHV0X3R5cGUiOiAibnVtYmVy
IiwgInRvb2x0aXAiOiAiSUQgb2YgdGhlIGFydGlmYWN0IiwgImludGVybmFsIjogZmFsc2UsICJy
aWNoX3RleHQiOiBmYWxzZSwgInRlbXBsYXRlcyI6IFtdLCAiZXhwb3J0X2tleSI6ICJfX2Z1bmN0
aW9uL2lvY19wYXJzZXJfdjJfYXJ0aWZhY3RfaWQiLCAiaGlkZV9ub3RpZmljYXRpb24iOiBmYWxz
ZSwgInBsYWNlaG9sZGVyIjogIiIsICJuYW1lIjogImlvY19wYXJzZXJfdjJfYXJ0aWZhY3RfaWQi
LCAiZGVwcmVjYXRlZCI6IGZhbHNlLCAiZGVmYXVsdF9jaG9zZW5fYnlfc2VydmVyIjogZmFsc2Us
ICJ2YWx1ZXMiOiBbXX0sIHsib3BlcmF0aW9ucyI6IFtdLCAidHlwZV9pZCI6IDExLCAib3BlcmF0
aW9uX3Blcm1zIjoge30sICJ0ZXh0IjogImlvY19wYXJzZXJfdjJfYXR0YWNobWVudF9pZCIsICJi
bGFua19vcHRpb24iOiBmYWxzZSwgInByZWZpeCI6IG51bGwsICJjaGFuZ2VhYmxlIjogdHJ1ZSwg
ImlkIjogMjE3LCAicmVhZF9vbmx5IjogZmFsc2UsICJ1dWlkIjogIjZlNjRjYjkxLTlhOWUtNDhk
NS05ZjA4LWY0ODliZTU0YzMwYiIsICJjaG9zZW4iOiBmYWxzZSwgImlucHV0X3R5cGUiOiAibnVt
YmVyIiwgInRvb2x0aXAiOiAiSUQgb2YgdGhlIGF0dGFjaG1lbnQiLCAiaW50ZXJuYWwiOiBmYWxz
ZSwgInJpY2hfdGV4dCI6IGZhbHNlLCAidGVtcGxhdGVzIjogW10sICJleHBvcnRfa2V5IjogIl9f
ZnVuY3Rpb24vaW9jX3BhcnNlcl92Ml9hdHRhY2htZW50X2lkIiwgImhpZGVfbm90aWZpY2F0aW9u
IjogZmFsc2UsICJwbGFjZWhvbGRlciI6ICIiLCAibmFtZSI6ICJpb2NfcGFyc2VyX3YyX2F0dGFj
aG1lbnRfaWQiLCAiZGVwcmVjYXRlZCI6IGZhbHNlLCAiZGVmYXVsdF9jaG9zZW5fYnlfc2VydmVy
IjogZmFsc2UsICJ2YWx1ZXMiOiBbXX1dLCAib3ZlcnJpZGVzIjogW10sICJleHBvcnRfZGF0ZSI6
IDE1NjM4MTE4NDM2MDJ9
"""
    )
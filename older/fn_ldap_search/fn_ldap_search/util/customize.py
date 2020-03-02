# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_ldap_search"""

from __future__ import print_function
from resilient_circuits.util import *


def customization_data(client=None):
    """Produce any customization definitions (types, fields, message destinations, etc)
       that should be installed by `resilient-circuits customize`
    """

    # This import data contains:
    #   Function inputs:
    #     ldap_param
    #     ldap_search_attributes
    #     ldap_search_base
    #     ldap_search_filter
    #   DataTables:
    #     ldap_query_results
    #   Message Destinations:
    #     ldap
    #   Functions:
    #     ldap_search
    #   Workflows:
    #     wf_ldap_search
    #   Rules:
    #     Example: LDAP Search - Person


    yield ImportDefinition(u"""
eyJ0YXNrX29yZGVyIjogW10sICJ3b3JrZmxvd3MiOiBbeyJwcm9ncmFtbWF0aWNfbmFtZSI6ICJ3
Zl9sZGFwX3NlYXJjaCIsICJvYmplY3RfdHlwZSI6ICJhcnRpZmFjdCIsICJleHBvcnRfa2V5Ijog
IndmX2xkYXBfc2VhcmNoIiwgInV1aWQiOiAiOGExMzdkZTQtYjZkNi00YjJkLTkxMWMtYjMxNGQ2
ZjRkMzJhIiwgImxhc3RfbW9kaWZpZWRfYnkiOiAiYUBhLmNvbSIsICJuYW1lIjogIkV4YW1wbGU6
IExEQVAgU2VhcmNoIC0gUGVyc29uIiwgImNvbnRlbnQiOiB7InhtbCI6ICI8P3htbCB2ZXJzaW9u
PVwiMS4wXCIgZW5jb2Rpbmc9XCJVVEYtOFwiPz48ZGVmaW5pdGlvbnMgeG1sbnM9XCJodHRwOi8v
d3d3Lm9tZy5vcmcvc3BlYy9CUE1OLzIwMTAwNTI0L01PREVMXCIgeG1sbnM6YnBtbmRpPVwiaHR0
cDovL3d3dy5vbWcub3JnL3NwZWMvQlBNTi8yMDEwMDUyNC9ESVwiIHhtbG5zOm9tZ2RjPVwiaHR0
cDovL3d3dy5vbWcub3JnL3NwZWMvREQvMjAxMDA1MjQvRENcIiB4bWxuczpvbWdkaT1cImh0dHA6
Ly93d3cub21nLm9yZy9zcGVjL0RELzIwMTAwNTI0L0RJXCIgeG1sbnM6cmVzaWxpZW50PVwiaHR0
cDovL3Jlc2lsaWVudC5pYm0uY29tL2JwbW5cIiB4bWxuczp4c2Q9XCJodHRwOi8vd3d3LnczLm9y
Zy8yMDAxL1hNTFNjaGVtYVwiIHhtbG5zOnhzaT1cImh0dHA6Ly93d3cudzMub3JnLzIwMDEvWE1M
U2NoZW1hLWluc3RhbmNlXCIgdGFyZ2V0TmFtZXNwYWNlPVwiaHR0cDovL3d3dy5jYW11bmRhLm9y
Zy90ZXN0XCI+PHByb2Nlc3MgaWQ9XCJ3Zl9sZGFwX3NlYXJjaFwiIGlzRXhlY3V0YWJsZT1cInRy
dWVcIiBuYW1lPVwiRXhhbXBsZTogTERBUCBTZWFyY2ggLSBQZXJzb25cIj48ZG9jdW1lbnRhdGlv
bj5FeGFtcGxlIHdvcmtmbG93IHdoaWNoIHJ1bnMgYSBwZXJzb24gcXVlcnkgYWdhaW5zdCBhbiBM
REFQIHNlcnZlci48L2RvY3VtZW50YXRpb24+PHN0YXJ0RXZlbnQgaWQ9XCJTdGFydEV2ZW50XzE1
NWFzeG1cIj48b3V0Z29pbmc+U2VxdWVuY2VGbG93XzA3d3h0Zmw8L291dGdvaW5nPjwvc3RhcnRF
dmVudD48c2VydmljZVRhc2sgaWQ9XCJTZXJ2aWNlVGFza18xaDQ0N2YxXCIgbmFtZT1cImxkYXBf
c2VhcmNoXCIgcmVzaWxpZW50OnR5cGU9XCJmdW5jdGlvblwiPjxleHRlbnNpb25FbGVtZW50cz48
cmVzaWxpZW50OmZ1bmN0aW9uIHV1aWQ9XCI1YjI0MDg4Ni02Y2MxLTQ0ZDQtOTk3Yi02NTI0MDFm
ZGFmZjZcIj57XCJpbnB1dHNcIjp7fSxcInByZV9wcm9jZXNzaW5nX3NjcmlwdFwiOlwiIyMgIExE
QVAgU2VhcmNoIFdvcmtmbG93IC0gcHJlLXByb2Nlc3Npbmcgc2NyaXB0ICMjXFxuaW5wdXRzLmxk
YXBfc2VhcmNoX2Jhc2UgPSBcXFwiZGM9ZXhhbXBsZSxkYz1jb21cXFwiXFxuaW5wdXRzLmxkYXBf
c2VhcmNoX2ZpbHRlciA9IFxcXCIoJmFtcDsob2JqZWN0Q2xhc3M9cGVyc29uKSh1aWQ9JWxkYXBf
cGFyYW0lKSlcXFwiXFxuaW5wdXRzLmxkYXBfc2VhcmNoX2F0dHJpYnV0ZXMgPSBcXFwiY24sc24s
bWFpbCx0ZWxlcGhvbmVOdW1iZXJcXFwiXFxuaW5wdXRzLmxkYXBfcGFyYW0gPSAgYXJ0aWZhY3Qu
dmFsdWVcIixcInJlc3VsdF9uYW1lXCI6XCJcIixcInBvc3RfcHJvY2Vzc2luZ19zY3JpcHRcIjpc
IiMjICBMREFQIHNlYXJjaCB3b3JrZmxvdyAtIHBvc3QgcHJvY2Vzc2luZyBzY3JpcHQgIyNcXG4j
IEV4YW1wbGUgb2YgZXhwZWN0ZWQgcmVzdWx0cyAtIE9wZW5MZGFwXFxuXFxcIlxcXCJcXFwiXFxu
J2VudHJpZXMnOiBbe1xcXCJkblxcXCI6IFxcXCJ1aWQ9bmV3dG9uLGRjPWV4YW1wbGUsZGM9Y29t
XFxcIiwgXFxcInRlbGVwaG9uZU51bWJlclxcXCI6IFtdLCBcXFwidWlkXFxcIjogW1xcXCJuZXd0
b25cXFwiXSxcXG4gICAgXFxcIm1haWxcXFwiOiBbXFxcIm5ld3RvbkBsZGFwLmZvcnVtc3lzLmNv
bVxcXCJdLCBcXFwic25cXFwiOiBbXFxcIk5ld3RvblxcXCJdLCBcXFwiY25cXFwiOiBbXFxcIklz
YWFjIE5ld3RvblxcXCJdfSxcXG4gICAge1xcXCJkblxcXCI6IFxcXCJ1aWQ9ZWluc3RlaW4sZGM9
ZXhhbXBsZSxkYz1jb21cXFwiLCBcXFwidGVsZXBob25lTnVtYmVyXFxcIjogW1xcXCIzMTQtMTU5
LTI2NTNcXFwiXSwgXFxcInVpZFxcXCI6IFtcXFwiZWluc3RlaW5cXFwiXSxcXG4gICAgXFxcIm1h
aWxcXFwiOiBbXFxcImVpbnN0ZWluQGxkYXAuZm9ydW1zeXMuY29tXFxcIl0sIFxcXCJzblxcXCI6
IFtcXFwiRWluc3RlaW5cXFwiXSwgXFxcImNuXFxcIjogW1xcXCJBbGJlcnQgRWluc3RlaW5cXFwi
XX1dXFxuXFxcIlxcXCJcXFwiXFxuIyBFeGFtcGxlIG9mIGV4cGVjdGVkIHJlc3VsdHMgLSBBRFxc
blxcXCJcXFwiXFxcIlxcbiAnZW50cmllcyc6IFt7dSdkbic6IHUnQ049SXNhYWMgTmV3dG9uLE9V
PUlCTVJlc2lsaWVudCxEQz1pYm0sREM9cmVzaWxpZW50LERDPWNvbScsIFxcbiAgICAgICAgICAg
ICAgdSd0ZWxlcGhvbmVOdW1iZXInOiB1JzMxNC0xNTktMjY1MycsIHUnY24nOiB1J0lzYWFjIE5l
d3RvbicsIFxcbiAgICAgICAgICAgICAgdSdtYWlsJzogdSdlaW5zdGVpbkByZXNpbGllbnQuaWJt
LmNvbScsIHUnc24nOiB1J05ld3Rvbid9XVxcblxcXCJcXFwiXFxcIlxcbiMgIEdsb2JhbHNcXG5F
TlRSWV9UT19EQVRBVEFCTEVfTUFQID0ge1xcbiAgIFxcXCJ1aWRcXFwiOiBcXFwidWlkXFxcIixc
XG4gICBcXFwiY25cXFwiOiBcXFwiZnVsbG5hbWVcXFwiLFxcbiAgIFxcXCJzblxcXCI6IFxcXCJz
dXJuYW1lXFxcIixcXG4gICBcXFwibWFpbFxcXCI6IFxcXCJlbWFpbF9hZGRyZXNzXFxcIixcXG4g
ICBcXFwidGVsZXBob25lTnVtYmVyXFxcIjogXFxcInRlbGVwaG9uZV9udW1iZXJcXFwiXFxufVxc
biMgUHJvY2Vzc2luZ1xcbmZvciBlbnRyeSBpbiByZXN1bHRzLmVudHJpZXM6XFxuIGlmIGVudHJ5
IGlzIE5vbmU6XFxuICAgICBicmVha1xcbiBlbHNlOlxcbiAgICAgcm93ID0gaW5jaWRlbnQuYWRk
Um93KFxcXCJsZGFwX3F1ZXJ5X3Jlc3VsdHNcXFwiKVxcbiBmb3IgayBpbiBFTlRSWV9UT19EQVRB
VEFCTEVfTUFQOlxcbiAgICBpZiBlbnRyeVtrXSBpcyBOb25lOlxcbiAgICAgICAgcm93W0VOVFJZ
X1RPX0RBVEFUQUJMRV9NQVBba11dID0gXFxcIk4vQVxcXCJcXG4gICAgZWxzZTpcXG4gICAgICAg
IHRyeTpcXG4gICAgICAgICAgICBpZiBpc2luc3RhbmNlKGVudHJ5W2tdLCB1bmljb2RlKSBvciBs
ZW4oZW50cnlba10pID09IDA6XFxuICAgICAgICAgICAgICAgIHJvd1tFTlRSWV9UT19EQVRBVEFC
TEVfTUFQW2tdXSA9IHN0cihlbnRyeVtrXSlcXG4gICAgICAgICAgICBlbHNlOlxcbiAgICAgICAg
ICAgICAgICByb3dbRU5UUllfVE9fREFUQVRBQkxFX01BUFtrXV0gPSBzdHIoZW50cnlba11bMF0p
XFxuICAgICAgICBleGNlcHQgSW5kZXhFcnJvcjpcXG4gICAgICAgICAgICByb3dbRU5UUllfVE9f
REFUQVRBQkxFX01BUFtrXV0gPSBcXFwiTi9BXFxcIlxcblxcblxcblwifTwvcmVzaWxpZW50OmZ1
bmN0aW9uPjwvZXh0ZW5zaW9uRWxlbWVudHM+PGluY29taW5nPlNlcXVlbmNlRmxvd18wN3d4dGZs
PC9pbmNvbWluZz48b3V0Z29pbmc+U2VxdWVuY2VGbG93XzBraWc2MXc8L291dGdvaW5nPjwvc2Vy
dmljZVRhc2s+PHNlcXVlbmNlRmxvdyBpZD1cIlNlcXVlbmNlRmxvd18wN3d4dGZsXCIgc291cmNl
UmVmPVwiU3RhcnRFdmVudF8xNTVhc3htXCIgdGFyZ2V0UmVmPVwiU2VydmljZVRhc2tfMWg0NDdm
MVwiLz48ZW5kRXZlbnQgaWQ9XCJFbmRFdmVudF8xa2gwajZuXCI+PGluY29taW5nPlNlcXVlbmNl
Rmxvd18wa2lnNjF3PC9pbmNvbWluZz48L2VuZEV2ZW50PjxzZXF1ZW5jZUZsb3cgaWQ9XCJTZXF1
ZW5jZUZsb3dfMGtpZzYxd1wiIHNvdXJjZVJlZj1cIlNlcnZpY2VUYXNrXzFoNDQ3ZjFcIiB0YXJn
ZXRSZWY9XCJFbmRFdmVudF8xa2gwajZuXCIvPjx0ZXh0QW5ub3RhdGlvbiBpZD1cIlRleHRBbm5v
dGF0aW9uXzFreHhpeXRcIj48dGV4dD5TdGFydCB5b3VyIHdvcmtmbG93IGhlcmU8L3RleHQ+PC90
ZXh0QW5ub3RhdGlvbj48YXNzb2NpYXRpb24gaWQ9XCJBc3NvY2lhdGlvbl8xc2V1ajQ4XCIgc291
cmNlUmVmPVwiU3RhcnRFdmVudF8xNTVhc3htXCIgdGFyZ2V0UmVmPVwiVGV4dEFubm90YXRpb25f
MWt4eGl5dFwiLz48L3Byb2Nlc3M+PGJwbW5kaTpCUE1ORGlhZ3JhbSBpZD1cIkJQTU5EaWFncmFt
XzFcIj48YnBtbmRpOkJQTU5QbGFuZSBicG1uRWxlbWVudD1cInVuZGVmaW5lZFwiIGlkPVwiQlBN
TlBsYW5lXzFcIj48YnBtbmRpOkJQTU5TaGFwZSBicG1uRWxlbWVudD1cIlN0YXJ0RXZlbnRfMTU1
YXN4bVwiIGlkPVwiU3RhcnRFdmVudF8xNTVhc3htX2RpXCI+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9
XCIzNlwiIHdpZHRoPVwiMzZcIiB4PVwiMTYyXCIgeT1cIjE4OFwiLz48YnBtbmRpOkJQTU5MYWJl
bD48b21nZGM6Qm91bmRzIGhlaWdodD1cIjBcIiB3aWR0aD1cIjkwXCIgeD1cIjE1N1wiIHk9XCIy
MjNcIi8+PC9icG1uZGk6QlBNTkxhYmVsPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5T
aGFwZSBicG1uRWxlbWVudD1cIlRleHRBbm5vdGF0aW9uXzFreHhpeXRcIiBpZD1cIlRleHRBbm5v
dGF0aW9uXzFreHhpeXRfZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjMwXCIgd2lkdGg9XCIx
MDBcIiB4PVwiOTlcIiB5PVwiMjU0XCIvPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5F
ZGdlIGJwbW5FbGVtZW50PVwiQXNzb2NpYXRpb25fMXNldWo0OFwiIGlkPVwiQXNzb2NpYXRpb25f
MXNldWo0OF9kaVwiPjxvbWdkaTp3YXlwb2ludCB4PVwiMTY5XCIgeHNpOnR5cGU9XCJvbWdkYzpQ
b2ludFwiIHk9XCIyMjBcIi8+PG9tZ2RpOndheXBvaW50IHg9XCIxNTNcIiB4c2k6dHlwZT1cIm9t
Z2RjOlBvaW50XCIgeT1cIjI1NFwiLz48L2JwbW5kaTpCUE1ORWRnZT48YnBtbmRpOkJQTU5TaGFw
ZSBicG1uRWxlbWVudD1cIlNlcnZpY2VUYXNrXzFoNDQ3ZjFcIiBpZD1cIlNlcnZpY2VUYXNrXzFo
NDQ3ZjFfZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjgwXCIgd2lkdGg9XCIxMDBcIiB4PVwi
MjY2XCIgeT1cIjE2NlwiLz48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1ORWRnZSBicG1u
RWxlbWVudD1cIlNlcXVlbmNlRmxvd18wN3d4dGZsXCIgaWQ9XCJTZXF1ZW5jZUZsb3dfMDd3eHRm
bF9kaVwiPjxvbWdkaTp3YXlwb2ludCB4PVwiMTk4XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwi
IHk9XCIyMDZcIi8+PG9tZ2RpOndheXBvaW50IHg9XCIyNjZcIiB4c2k6dHlwZT1cIm9tZ2RjOlBv
aW50XCIgeT1cIjIwNlwiLz48YnBtbmRpOkJQTU5MYWJlbD48b21nZGM6Qm91bmRzIGhlaWdodD1c
IjEzXCIgd2lkdGg9XCIwXCIgeD1cIjIzMlwiIHk9XCIxODRcIi8+PC9icG1uZGk6QlBNTkxhYmVs
PjwvYnBtbmRpOkJQTU5FZGdlPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVtZW50PVwiRW5kRXZl
bnRfMWtoMGo2blwiIGlkPVwiRW5kRXZlbnRfMWtoMGo2bl9kaVwiPjxvbWdkYzpCb3VuZHMgaGVp
Z2h0PVwiMzZcIiB3aWR0aD1cIjM2XCIgeD1cIjQyOFwiIHk9XCIxODhcIi8+PGJwbW5kaTpCUE1O
TGFiZWw+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIxM1wiIHdpZHRoPVwiMFwiIHg9XCI0NDZcIiB5
PVwiMjI3XCIvPjwvYnBtbmRpOkJQTU5MYWJlbD48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpC
UE1ORWRnZSBicG1uRWxlbWVudD1cIlNlcXVlbmNlRmxvd18wa2lnNjF3XCIgaWQ9XCJTZXF1ZW5j
ZUZsb3dfMGtpZzYxd19kaVwiPjxvbWdkaTp3YXlwb2ludCB4PVwiMzY2XCIgeHNpOnR5cGU9XCJv
bWdkYzpQb2ludFwiIHk9XCIyMDZcIi8+PG9tZ2RpOndheXBvaW50IHg9XCI0MjhcIiB4c2k6dHlw
ZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIwNlwiLz48YnBtbmRpOkJQTU5MYWJlbD48b21nZGM6Qm91
bmRzIGhlaWdodD1cIjEzXCIgd2lkdGg9XCIwXCIgeD1cIjM5N1wiIHk9XCIxODRcIi8+PC9icG1u
ZGk6QlBNTkxhYmVsPjwvYnBtbmRpOkJQTU5FZGdlPjwvYnBtbmRpOkJQTU5QbGFuZT48L2JwbW5k
aTpCUE1ORGlhZ3JhbT48L2RlZmluaXRpb25zPiIsICJ3b3JrZmxvd19pZCI6ICJ3Zl9sZGFwX3Nl
YXJjaCIsICJ2ZXJzaW9uIjogMTZ9LCAid29ya2Zsb3dfaWQiOiAxLCAiYWN0aW9ucyI6IFtdLCAi
bGFzdF9tb2RpZmllZF90aW1lIjogMTUyOTk0NzMwMDczMiwgImNyZWF0b3JfaWQiOiAiYUBhLmNv
bSIsICJkZXNjcmlwdGlvbiI6ICJFeGFtcGxlIHdvcmtmbG93IHdoaWNoIHJ1bnMgYSBwZXJzb24g
cXVlcnkgYWdhaW5zdCBhbiBMREFQIHNlcnZlci4ifV0sICJhY3Rpb25zIjogW3sibG9naWNfdHlw
ZSI6ICJhbGwiLCAibmFtZSI6ICJFeGFtcGxlOiBMREFQIFNlYXJjaCAtIFBlcnNvbiIsICJ2aWV3
X2l0ZW1zIjogW10sICJ0eXBlIjogMSwgIndvcmtmbG93cyI6IFsid2ZfbGRhcF9zZWFyY2giXSwg
Im9iamVjdF90eXBlIjogImFydGlmYWN0IiwgInRpbWVvdXRfc2Vjb25kcyI6IDg2NDAwLCAidXVp
ZCI6ICJhNGJmZTFhMC1mNjk0LTQ2NzUtYjRiYy04ZmEwODE5MWExNDAiLCAiYXV0b21hdGlvbnMi
OiBbXSwgImV4cG9ydF9rZXkiOiAiRXhhbXBsZTogTERBUCBTZWFyY2ggLSBQZXJzb24iLCAiY29u
ZGl0aW9ucyI6IFtdLCAiaWQiOiAyNywgIm1lc3NhZ2VfZGVzdGluYXRpb25zIjogW119XSwgImxh
eW91dHMiOiBbXSwgImV4cG9ydF9mb3JtYXRfdmVyc2lvbiI6IDIsICJpZCI6IDMsICJpbmR1c3Ry
aWVzIjogbnVsbCwgInBoYXNlcyI6IFtdLCAiYWN0aW9uX29yZGVyIjogW10sICJnZW9zIjogbnVs
bCwgInNlcnZlcl92ZXJzaW9uIjogeyJtYWpvciI6IDMwLCAidmVyc2lvbiI6ICIzMC4wLjAiLCAi
YnVpbGRfbnVtYmVyIjogMCwgIm1pbm9yIjogMH0sICJ0aW1lZnJhbWVzIjogbnVsbCwgIndvcmtz
cGFjZXMiOiBbXSwgImF1dG9tYXRpY190YXNrcyI6IFtdLCAiZnVuY3Rpb25zIjogW3siZGlzcGxh
eV9uYW1lIjogImxkYXBfc2VhcmNoIiwgInV1aWQiOiAiNWIyNDA4ODYtNmNjMS00NGQ0LTk5N2It
NjUyNDAxZmRhZmY2IiwgImNyZWF0b3IiOiB7ImRpc3BsYXlfbmFtZSI6ICJSZXNpbGllbnQgU3lz
YWRtaW4iLCAidHlwZSI6ICJ1c2VyIiwgImlkIjogNCwgIm5hbWUiOiAiYUBhLmNvbSJ9LCAidmll
d19pdGVtcyI6IFt7InNob3dfaWYiOiBudWxsLCAiZmllbGRfdHlwZSI6ICJfX2Z1bmN0aW9uIiwg
InNob3dfbGlua19oZWFkZXIiOiBmYWxzZSwgImVsZW1lbnQiOiAiZmllbGRfdXVpZCIsICJjb250
ZW50IjogImU3MmU0NjllLTM0MmUtNGVmOS04ODYzLWQ4NGRlZTI3NzU4YSIsICJzdGVwX2xhYmVs
IjogbnVsbH0sIHsic2hvd19pZiI6IG51bGwsICJmaWVsZF90eXBlIjogIl9fZnVuY3Rpb24iLCAi
c2hvd19saW5rX2hlYWRlciI6IGZhbHNlLCAiZWxlbWVudCI6ICJmaWVsZF91dWlkIiwgImNvbnRl
bnQiOiAiYTU1MGUwMTEtMzE4ZS00YjdjLWE0ZWUtN2VjMDExZWUwNDQ3IiwgInN0ZXBfbGFiZWwi
OiBudWxsfSwgeyJzaG93X2lmIjogbnVsbCwgImZpZWxkX3R5cGUiOiAiX19mdW5jdGlvbiIsICJz
aG93X2xpbmtfaGVhZGVyIjogZmFsc2UsICJlbGVtZW50IjogImZpZWxkX3V1aWQiLCAiY29udGVu
dCI6ICJkNDQ5YWE1My0yMGU4LTRhZjAtYmI2MS01MjVmNDIwOGIwN2IiLCAic3RlcF9sYWJlbCI6
IG51bGx9LCB7InNob3dfaWYiOiBudWxsLCAiZmllbGRfdHlwZSI6ICJfX2Z1bmN0aW9uIiwgInNo
b3dfbGlua19oZWFkZXIiOiBmYWxzZSwgImVsZW1lbnQiOiAiZmllbGRfdXVpZCIsICJjb250ZW50
IjogIjg0NmRmZjRmLTcxYjYtNGFiMi1iZmQzLWY5ZmYwMmUyNDY0MSIsICJzdGVwX2xhYmVsIjog
bnVsbH1dLCAiZXhwb3J0X2tleSI6ICJsZGFwX3NlYXJjaCIsICJsYXN0X21vZGlmaWVkX2J5Ijog
eyJkaXNwbGF5X25hbWUiOiAiUmVzaWxpZW50IFN5c2FkbWluIiwgInR5cGUiOiAidXNlciIsICJp
ZCI6IDQsICJuYW1lIjogImFAYS5jb20ifSwgIm5hbWUiOiAibGRhcF9zZWFyY2giLCAidmVyc2lv
biI6IDEsICJ3b3JrZmxvd3MiOiBbeyJwcm9ncmFtbWF0aWNfbmFtZSI6ICJ3Zl9sZGFwX3NlYXJj
aCIsICJvYmplY3RfdHlwZSI6ICJhcnRpZmFjdCIsICJ1dWlkIjogbnVsbCwgImFjdGlvbnMiOiBb
XSwgIm5hbWUiOiAiRXhhbXBsZTogTERBUCBTZWFyY2ggLSBQZXJzb24iLCAid29ya2Zsb3dfaWQi
OiAxLCAiZGVzY3JpcHRpb24iOiBudWxsfV0sICJsYXN0X21vZGlmaWVkX3RpbWUiOiAxNTI5OTM2
ODcyMTgyLCAiZGVzdGluYXRpb25faGFuZGxlIjogImxkYXAiLCAiaWQiOiAxLCAiZGVzY3JpcHRp
b24iOiB7ImNvbnRlbnQiOiAiUmVzaWxpZW50IEZ1bmN0aW9uIHRvIGRvIGEgc2VhcmNoIG9yIHF1
ZXJ5IGFnYWluc3QgYW4gTERBUCBzZXJ2ZXIuIiwgImZvcm1hdCI6ICJ0ZXh0In19XSwgIm5vdGlm
aWNhdGlvbnMiOiBudWxsLCAicmVndWxhdG9ycyI6IG51bGwsICJpbmNpZGVudF90eXBlcyI6IFt7
ImNyZWF0ZV9kYXRlIjogMTUzMDAwNjg2Mzc0MiwgImRlc2NyaXB0aW9uIjogIkN1c3RvbWl6YXRp
b24gUGFja2FnZXMgKGludGVybmFsKSIsICJleHBvcnRfa2V5IjogIkN1c3RvbWl6YXRpb24gUGFj
a2FnZXMgKGludGVybmFsKSIsICJpZCI6IDAsICJuYW1lIjogIkN1c3RvbWl6YXRpb24gUGFja2Fn
ZXMgKGludGVybmFsKSIsICJ1cGRhdGVfZGF0ZSI6IDE1MzAwMDY4NjM3NDIsICJ1dWlkIjogImJm
ZWVjMmQ0LTM3NzAtMTFlOC1hZDM5LTRhMDAwNDA0NGFhMCIsICJlbmFibGVkIjogZmFsc2UsICJz
eXN0ZW0iOiBmYWxzZSwgInBhcmVudF9pZCI6IG51bGwsICJoaWRkZW4iOiBmYWxzZX1dLCAic2Ny
aXB0cyI6IFtdLCAidHlwZXMiOiBbeyJkaXNwbGF5X25hbWUiOiAiTERBUCBRdWVyeSByZXN1bHRz
IiwgInV1aWQiOiAiMjc5NTM3MmEtOWU1ZS00YmI0LWEwN2EtMGNkMzg5ZjBjYjI5IiwgInR5cGVf
aWQiOiA4LCAiZmllbGRzIjogeyJ0ZWxlcGhvbmVfbnVtYmVyIjogeyJvcGVyYXRpb25zIjogW10s
ICJ0eXBlX2lkIjogMTAwMCwgIm9wZXJhdGlvbl9wZXJtcyI6IHt9LCAidGV4dCI6ICJUZWxlcGhv
bmUgTnVtYmVyIiwgImJsYW5rX29wdGlvbiI6IGZhbHNlLCAicHJlZml4IjogbnVsbCwgImNoYW5n
ZWFibGUiOiB0cnVlLCAiaWQiOiAxNTcsICJyZWFkX29ubHkiOiBmYWxzZSwgInV1aWQiOiAiMjZl
NDYwMjUtMTY2Yy00NTA1LWEwNTEtZGVlNDZlMTZkZjk4IiwgImNob3NlbiI6IGZhbHNlLCAiaW5w
dXRfdHlwZSI6ICJ0ZXh0IiwgInRvb2x0aXAiOiAiIiwgIndpZHRoIjogMTcyLCAiaW50ZXJuYWwi
OiBmYWxzZSwgInJpY2hfdGV4dCI6IGZhbHNlLCAidGVtcGxhdGVzIjogW10sICJleHBvcnRfa2V5
IjogImxkYXBfcXVlcnlfcmVzdWx0cy90ZWxlcGhvbmVfbnVtYmVyIiwgImhpZGVfbm90aWZpY2F0
aW9uIjogZmFsc2UsICJwbGFjZWhvbGRlciI6ICIiLCAibmFtZSI6ICJ0ZWxlcGhvbmVfbnVtYmVy
IiwgImRlZmF1bHRfY2hvc2VuX2J5X3NlcnZlciI6IGZhbHNlLCAidmFsdWVzIjogW10sICJvcmRl
ciI6IDR9LCAic3VybmFtZSI6IHsib3BlcmF0aW9ucyI6IFtdLCAidHlwZV9pZCI6IDEwMDAsICJv
cGVyYXRpb25fcGVybXMiOiB7fSwgInRleHQiOiAiU3VybmFtZSIsICJibGFua19vcHRpb24iOiBm
YWxzZSwgInByZWZpeCI6IG51bGwsICJjaGFuZ2VhYmxlIjogdHJ1ZSwgImlkIjogMTU1LCAicmVh
ZF9vbmx5IjogZmFsc2UsICJ1dWlkIjogIjU5NWY5NjQxLTQ2YzYtNDg1ZC04MDA1LThhZjk4ZWIy
YTk2YyIsICJjaG9zZW4iOiBmYWxzZSwgImlucHV0X3R5cGUiOiAidGV4dCIsICJ0b29sdGlwIjog
IiIsICJ3aWR0aCI6IDExMywgImludGVybmFsIjogZmFsc2UsICJyaWNoX3RleHQiOiBmYWxzZSwg
InRlbXBsYXRlcyI6IFtdLCAiZXhwb3J0X2tleSI6ICJsZGFwX3F1ZXJ5X3Jlc3VsdHMvc3VybmFt
ZSIsICJoaWRlX25vdGlmaWNhdGlvbiI6IGZhbHNlLCAicGxhY2Vob2xkZXIiOiAiIiwgIm5hbWUi
OiAic3VybmFtZSIsICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZSwgInZhbHVlcyI6
IFtdLCAib3JkZXIiOiAyfSwgImZ1bGxuYW1lIjogeyJvcGVyYXRpb25zIjogW10sICJ0eXBlX2lk
IjogMTAwMCwgIm9wZXJhdGlvbl9wZXJtcyI6IHt9LCAidGV4dCI6ICJGdWxsbmFtZSIsICJibGFu
a19vcHRpb24iOiBmYWxzZSwgInByZWZpeCI6IG51bGwsICJjaGFuZ2VhYmxlIjogdHJ1ZSwgImlk
IjogMTU2LCAicmVhZF9vbmx5IjogZmFsc2UsICJ1dWlkIjogImI0NjlkMGZlLWFiMzItNDEwMC1i
YmE1LTlkNDAyMTJmZDEyNyIsICJjaG9zZW4iOiBmYWxzZSwgImlucHV0X3R5cGUiOiAidGV4dCIs
ICJ0b29sdGlwIjogIiIsICJ3aWR0aCI6IDExMywgImludGVybmFsIjogZmFsc2UsICJyaWNoX3Rl
eHQiOiBmYWxzZSwgInRlbXBsYXRlcyI6IFtdLCAiZXhwb3J0X2tleSI6ICJsZGFwX3F1ZXJ5X3Jl
c3VsdHMvZnVsbG5hbWUiLCAiaGlkZV9ub3RpZmljYXRpb24iOiBmYWxzZSwgInBsYWNlaG9sZGVy
IjogIiIsICJuYW1lIjogImZ1bGxuYW1lIiwgImRlZmF1bHRfY2hvc2VuX2J5X3NlcnZlciI6IGZh
bHNlLCAidmFsdWVzIjogW10sICJvcmRlciI6IDF9LCAiZW1haWxfYWRkcmVzcyI6IHsib3BlcmF0
aW9ucyI6IFtdLCAidHlwZV9pZCI6IDEwMDAsICJvcGVyYXRpb25fcGVybXMiOiB7fSwgInRleHQi
OiAiRW1haWwgYWRkcmVzcyIsICJibGFua19vcHRpb24iOiBmYWxzZSwgInByZWZpeCI6IG51bGws
ICJjaGFuZ2VhYmxlIjogdHJ1ZSwgImlkIjogMTU5LCAicmVhZF9vbmx5IjogZmFsc2UsICJ1dWlk
IjogIjM5ODU5MmNiLTRkNTItNDczZS05MjZmLTMyYzdkMTJjYTExYyIsICJjaG9zZW4iOiBmYWxz
ZSwgImlucHV0X3R5cGUiOiAidGV4dCIsICJ0b29sdGlwIjogIiIsICJ3aWR0aCI6IDEzMiwgImlu
dGVybmFsIjogZmFsc2UsICJyaWNoX3RleHQiOiBmYWxzZSwgInRlbXBsYXRlcyI6IFtdLCAiZXhw
b3J0X2tleSI6ICJsZGFwX3F1ZXJ5X3Jlc3VsdHMvZW1haWxfYWRkcmVzcyIsICJoaWRlX25vdGlm
aWNhdGlvbiI6IGZhbHNlLCAicGxhY2Vob2xkZXIiOiAiIiwgIm5hbWUiOiAiZW1haWxfYWRkcmVz
cyIsICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZSwgInZhbHVlcyI6IFtdLCAib3Jk
ZXIiOiAzfSwgInVpZCI6IHsib3BlcmF0aW9ucyI6IFtdLCAidHlwZV9pZCI6IDEwMDAsICJvcGVy
YXRpb25fcGVybXMiOiB7fSwgInRleHQiOiAiVUlEIiwgImJsYW5rX29wdGlvbiI6IGZhbHNlLCAi
cHJlZml4IjogbnVsbCwgImNoYW5nZWFibGUiOiB0cnVlLCAiaWQiOiAxNTgsICJyZWFkX29ubHki
OiBmYWxzZSwgInV1aWQiOiAiOTQ1OTVlMjAtNDFjOC00ZTM3LWFkZmYtNzBlOTQ5YWE4ZGRjIiwg
ImNob3NlbiI6IGZhbHNlLCAiaW5wdXRfdHlwZSI6ICJ0ZXh0IiwgInRvb2x0aXAiOiAiIiwgIndp
ZHRoIjogMTEzLCAiaW50ZXJuYWwiOiBmYWxzZSwgInJpY2hfdGV4dCI6IGZhbHNlLCAidGVtcGxh
dGVzIjogW10sICJleHBvcnRfa2V5IjogImxkYXBfcXVlcnlfcmVzdWx0cy91aWQiLCAiaGlkZV9u
b3RpZmljYXRpb24iOiBmYWxzZSwgInBsYWNlaG9sZGVyIjogIiIsICJuYW1lIjogInVpZCIsICJk
ZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZSwgInZhbHVlcyI6IFtdLCAib3JkZXIiOiAw
fX0sICJwYXJlbnRfdHlwZXMiOiBbImluY2lkZW50Il0sICJ0eXBlX25hbWUiOiAibGRhcF9xdWVy
eV9yZXN1bHRzIiwgImV4cG9ydF9rZXkiOiAibGRhcF9xdWVyeV9yZXN1bHRzIiwgImZvcl9jdXN0
b21fZmllbGRzIjogZmFsc2UsICJhY3Rpb25zIjogW10sICJwcm9wZXJ0aWVzIjogeyJmb3Jfd2hv
IjogW10sICJjYW5fZGVzdHJveSI6IGZhbHNlLCAiY2FuX2NyZWF0ZSI6IGZhbHNlfSwgImZvcl9h
Y3Rpb25zIjogZmFsc2UsICJmb3Jfbm90aWZpY2F0aW9ucyI6IGZhbHNlLCAic2NyaXB0cyI6IFtd
LCAiaWQiOiBudWxsfV0sICJtZXNzYWdlX2Rlc3RpbmF0aW9ucyI6IFt7InV1aWQiOiAiMjdlNzNi
MmYtNjkxMC00YmQ4LThiNTItNDgxZmVjNDNiNWM2IiwgImV4cG9ydF9rZXkiOiAibGRhcCIsICJu
YW1lIjogImxkYXAiLCAiZGVzdGluYXRpb25fdHlwZSI6IDAsICJwcm9ncmFtbWF0aWNfbmFtZSI6
ICJsZGFwIiwgImV4cGVjdF9hY2siOiB0cnVlLCAidXNlcnMiOiBbImFAYS5jb20iXX1dLCAiaW5j
aWRlbnRfYXJ0aWZhY3RfdHlwZXMiOiBbXSwgInJvbGVzIjogW10sICJmaWVsZHMiOiBbeyJvcGVy
YXRpb25zIjogW10sICJyZWFkX29ubHkiOiB0cnVlLCAidXVpZCI6ICJjM2YwZTNlZC0yMWUxLTRk
NTMtYWZmYi1mZTVjYTMzMDhjY2EiLCAidGVtcGxhdGVzIjogW10sICJ0eXBlX2lkIjogMCwgImNo
b3NlbiI6IGZhbHNlLCAidGV4dCI6ICJTaW11bGF0aW9uIiwgImRlZmF1bHRfY2hvc2VuX2J5X3Nl
cnZlciI6IGZhbHNlLCAiZXhwb3J0X2tleSI6ICJpbmNpZGVudC9pbmNfdHJhaW5pbmciLCAidG9v
bHRpcCI6ICJXaGV0aGVyIHRoZSBpbmNpZGVudCBpcyBhIHNpbXVsYXRpb24gb3IgYSByZWd1bGFy
IGluY2lkZW50LiAgVGhpcyBmaWVsZCBpcyByZWFkLW9ubHkuIiwgInJpY2hfdGV4dCI6IGZhbHNl
LCAib3BlcmF0aW9uX3Blcm1zIjoge30sICJwcmVmaXgiOiBudWxsLCAiaW50ZXJuYWwiOiBmYWxz
ZSwgInZhbHVlcyI6IFtdLCAiYmxhbmtfb3B0aW9uIjogZmFsc2UsICJpbnB1dF90eXBlIjogImJv
b2xlYW4iLCAiY2hhbmdlYWJsZSI6IHRydWUsICJoaWRlX25vdGlmaWNhdGlvbiI6IGZhbHNlLCAi
aWQiOiAxMTEsICJuYW1lIjogImluY190cmFpbmluZyJ9LCB7Im9wZXJhdGlvbnMiOiBbXSwgInR5
cGVfaWQiOiAxMSwgIm9wZXJhdGlvbl9wZXJtcyI6IHt9LCAidGV4dCI6ICJsZGFwX3NlYXJjaF9m
aWx0ZXIiLCAiYmxhbmtfb3B0aW9uIjogZmFsc2UsICJwcmVmaXgiOiBudWxsLCAiY2hhbmdlYWJs
ZSI6IHRydWUsICJpZCI6IDE2MSwgInJlYWRfb25seSI6IGZhbHNlLCAidXVpZCI6ICJhNTUwZTAx
MS0zMThlLTRiN2MtYTRlZS03ZWMwMTFlZTA0NDciLCAiY2hvc2VuIjogZmFsc2UsICJpbnB1dF90
eXBlIjogInRleHRhcmVhIiwgInRvb2x0aXAiOiAiVGhlIGZpbHRlciBvZiB0aGUgTERBUCBzZWFy
Y2ggcmVxdWVzdCIsICJpbnRlcm5hbCI6IGZhbHNlLCAicmljaF90ZXh0IjogZmFsc2UsICJ0ZW1w
bGF0ZXMiOiBbXSwgImV4cG9ydF9rZXkiOiAiX19mdW5jdGlvbi9sZGFwX3NlYXJjaF9maWx0ZXIi
LCAiaGlkZV9ub3RpZmljYXRpb24iOiBmYWxzZSwgInBsYWNlaG9sZGVyIjogIiIsICJuYW1lIjog
ImxkYXBfc2VhcmNoX2ZpbHRlciIsICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZSwg
InZhbHVlcyI6IFtdfSwgeyJvcGVyYXRpb25zIjogW10sICJ0eXBlX2lkIjogMTEsICJvcGVyYXRp
b25fcGVybXMiOiB7fSwgInRleHQiOiAibGRhcF9zZWFyY2hfYmFzZSIsICJibGFua19vcHRpb24i
OiBmYWxzZSwgInByZWZpeCI6IG51bGwsICJjaGFuZ2VhYmxlIjogdHJ1ZSwgImlkIjogMTYwLCAi
cmVhZF9vbmx5IjogZmFsc2UsICJ1dWlkIjogImU3MmU0NjllLTM0MmUtNGVmOS04ODYzLWQ4NGRl
ZTI3NzU4YSIsICJjaG9zZW4iOiBmYWxzZSwgImlucHV0X3R5cGUiOiAidGV4dCIsICJ0b29sdGlw
IjogIlRoZSBiYXNlIG9mIHRoZSBMREFQIHNlYXJjaCByZXF1ZXN0LiIsICJpbnRlcm5hbCI6IGZh
bHNlLCAicmljaF90ZXh0IjogZmFsc2UsICJ0ZW1wbGF0ZXMiOiBbXSwgImV4cG9ydF9rZXkiOiAi
X19mdW5jdGlvbi9sZGFwX3NlYXJjaF9iYXNlIiwgImhpZGVfbm90aWZpY2F0aW9uIjogZmFsc2Us
ICJwbGFjZWhvbGRlciI6ICIiLCAibmFtZSI6ICJsZGFwX3NlYXJjaF9iYXNlIiwgImRlZmF1bHRf
Y2hvc2VuX2J5X3NlcnZlciI6IGZhbHNlLCAidmFsdWVzIjogW119LCB7Im9wZXJhdGlvbnMiOiBb
XSwgInR5cGVfaWQiOiAxMSwgIm9wZXJhdGlvbl9wZXJtcyI6IHt9LCAidGV4dCI6ICJsZGFwX3Bh
cmFtIiwgImJsYW5rX29wdGlvbiI6IGZhbHNlLCAicHJlZml4IjogbnVsbCwgImNoYW5nZWFibGUi
OiB0cnVlLCAiaWQiOiAxNjIsICJyZWFkX29ubHkiOiBmYWxzZSwgInV1aWQiOiAiODQ2ZGZmNGYt
NzFiNi00YWIyLWJmZDMtZjlmZjAyZTI0NjQxIiwgImNob3NlbiI6IGZhbHNlLCAiaW5wdXRfdHlw
ZSI6ICJ0ZXh0IiwgInRvb2x0aXAiOiAiUGFyYW1ldGVyIHVzZWQgaW4gTERBUCBzZWFyY2giLCAi
aW50ZXJuYWwiOiBmYWxzZSwgInJpY2hfdGV4dCI6IGZhbHNlLCAidGVtcGxhdGVzIjogW10sICJl
eHBvcnRfa2V5IjogIl9fZnVuY3Rpb24vbGRhcF9wYXJhbSIsICJoaWRlX25vdGlmaWNhdGlvbiI6
IGZhbHNlLCAicGxhY2Vob2xkZXIiOiAiIiwgIm5hbWUiOiAibGRhcF9wYXJhbSIsICJkZWZhdWx0
X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZSwgInZhbHVlcyI6IFtdfSwgeyJvcGVyYXRpb25zIjog
W10sICJ0eXBlX2lkIjogMTEsICJvcGVyYXRpb25fcGVybXMiOiB7fSwgInRleHQiOiAibGRhcF9z
ZWFyY2hfYXR0cmlidXRlcyIsICJibGFua19vcHRpb24iOiBmYWxzZSwgInByZWZpeCI6IG51bGws
ICJjaGFuZ2VhYmxlIjogdHJ1ZSwgImlkIjogMTYzLCAicmVhZF9vbmx5IjogZmFsc2UsICJ1dWlk
IjogImQ0NDlhYTUzLTIwZTgtNGFmMC1iYjYxLTUyNWY0MjA4YjA3YiIsICJjaG9zZW4iOiBmYWxz
ZSwgImlucHV0X3R5cGUiOiAidGV4dCIsICJ0b29sdGlwIjogIkEgc2luZ2xlIGF0dHJpYnV0ZSBv
ciBhIGxpc3Qgb2YgYXR0cmlidXRlcyB0byBiZSByZXR1cm5lZCBieSB0aGUgTERBUCBzZWFyY2gg
IiwgImludGVybmFsIjogZmFsc2UsICJyaWNoX3RleHQiOiBmYWxzZSwgInRlbXBsYXRlcyI6IFtd
LCAiZXhwb3J0X2tleSI6ICJfX2Z1bmN0aW9uL2xkYXBfc2VhcmNoX2F0dHJpYnV0ZXMiLCAiaGlk
ZV9ub3RpZmljYXRpb24iOiBmYWxzZSwgInBsYWNlaG9sZGVyIjogIiIsICJuYW1lIjogImxkYXBf
c2VhcmNoX2F0dHJpYnV0ZXMiLCAiZGVmYXVsdF9jaG9zZW5fYnlfc2VydmVyIjogZmFsc2UsICJ2
YWx1ZXMiOiBbXX1dLCAib3ZlcnJpZGVzIjogW10sICJleHBvcnRfZGF0ZSI6IDE1Mjk5NDg5NDk4
NzB9
"""
    )

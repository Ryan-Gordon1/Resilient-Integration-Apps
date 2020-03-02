# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_html2pdf"""

from __future__ import print_function
from resilient_circuits.util import *

def codegen_reload_data():
    """Parameters to codegen used to generate the fn_html2pdf package"""
    reload_params = {"package": u"fn_html2pdf",
                    "incident_fields": [], 
                    "action_fields": [], 
                    "function_params": [u"html2pdf_data", u"html2pdf_data_type", u"html2pdf_stylesheet"], 
                    "datatables": [], 
                    "message_destinations": [u"fn_html2pdf"], 
                    "functions": [u"fn_html2pdf"], 
                    "phases": [], 
                    "automatic_tasks": [], 
                    "scripts": [], 
                    "workflows": [u"example_html2pdf"], 
                    "actions": [u"Example: HTML2PDF"] 
                    }
    return reload_params


def customization_data(client=None):
    """Produce any customization definitions (types, fields, message destinations, etc)
       that should be installed by `resilient-circuits customize`
    """

    # This import data contains:
    #   Function inputs:
    #     html2pdf_data
    #     html2pdf_data_type
    #     html2pdf_stylesheet
    #   Message Destinations:
    #     fn_html2pdf
    #   Functions:
    #     fn_html2pdf
    #   Workflows:
    #     example_html2pdf
    #   Rules:
    #     Example: HTML2PDF


    yield ImportDefinition(u"""
eyJzZXJ2ZXJfdmVyc2lvbiI6IHsibWFqb3IiOiAzMSwgIm1pbm9yIjogMCwgImJ1aWxkX251bWJl
ciI6IDQyNTQsICJ2ZXJzaW9uIjogIjMxLjAuNDI1NCJ9LCAiZXhwb3J0X2Zvcm1hdF92ZXJzaW9u
IjogMiwgImlkIjogMiwgImV4cG9ydF9kYXRlIjogMTU0NTIyOTk0ODUyOSwgImZpZWxkcyI6IFt7
ImlkIjogNTEsICJuYW1lIjogImluY190cmFpbmluZyIsICJ0ZXh0IjogIlNpbXVsYXRpb24iLCAi
cHJlZml4IjogbnVsbCwgInR5cGVfaWQiOiAwLCAidG9vbHRpcCI6ICJXaGV0aGVyIHRoZSBpbmNp
ZGVudCBpcyBhIHNpbXVsYXRpb24gb3IgYSByZWd1bGFyIGluY2lkZW50LiAgVGhpcyBmaWVsZCBp
cyByZWFkLW9ubHkuIiwgImlucHV0X3R5cGUiOiAiYm9vbGVhbiIsICJoaWRlX25vdGlmaWNhdGlv
biI6IGZhbHNlLCAiY2hvc2VuIjogZmFsc2UsICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBm
YWxzZSwgImJsYW5rX29wdGlvbiI6IGZhbHNlLCAiaW50ZXJuYWwiOiBmYWxzZSwgInV1aWQiOiAi
YzNmMGUzZWQtMjFlMS00ZDUzLWFmZmItZmU1Y2EzMzA4Y2NhIiwgIm9wZXJhdGlvbnMiOiBbXSwg
Im9wZXJhdGlvbl9wZXJtcyI6IHt9LCAidmFsdWVzIjogW10sICJyZWFkX29ubHkiOiB0cnVlLCAi
Y2hhbmdlYWJsZSI6IHRydWUsICJyaWNoX3RleHQiOiBmYWxzZSwgImV4cG9ydF9rZXkiOiAiaW5j
aWRlbnQvaW5jX3RyYWluaW5nIiwgInRlbXBsYXRlcyI6IFtdLCAiZGVwcmVjYXRlZCI6IGZhbHNl
fSwgeyJpZCI6IDE2MywgIm5hbWUiOiAiaHRtbDJwZGZfZGF0YSIsICJ0ZXh0IjogImh0bWwycGRm
X2RhdGEiLCAicHJlZml4IjogbnVsbCwgInR5cGVfaWQiOiAxMSwgInRvb2x0aXAiOiAic3BlY2lm
eSBlaXRoZXIgYSBodG1sIHN0cmluZyBvciB1cmwgcmVmZXJlbmNlIiwgInBsYWNlaG9sZGVyIjog
IiIsICJpbnB1dF90eXBlIjogInRleHQiLCAicmVxdWlyZWQiOiAiYWx3YXlzIiwgImhpZGVfbm90
aWZpY2F0aW9uIjogZmFsc2UsICJjaG9zZW4iOiBmYWxzZSwgImRlZmF1bHRfY2hvc2VuX2J5X3Nl
cnZlciI6IGZhbHNlLCAiYmxhbmtfb3B0aW9uIjogZmFsc2UsICJpbnRlcm5hbCI6IGZhbHNlLCAi
dXVpZCI6ICI5ZDBlMjg4Ny05MWJjLTQ1ZWMtODMxZi1iNTE5OTZlMDFmYTYiLCAib3BlcmF0aW9u
cyI6IFtdLCAib3BlcmF0aW9uX3Blcm1zIjoge30sICJ2YWx1ZXMiOiBbXSwgInJlYWRfb25seSI6
IGZhbHNlLCAiY2hhbmdlYWJsZSI6IHRydWUsICJyaWNoX3RleHQiOiBmYWxzZSwgImV4cG9ydF9r
ZXkiOiAiX19mdW5jdGlvbi9odG1sMnBkZl9kYXRhIiwgInRlbXBsYXRlcyI6IFtdLCAiZGVwcmVj
YXRlZCI6IGZhbHNlfSwgeyJpZCI6IDE2MiwgIm5hbWUiOiAiaHRtbDJwZGZfZGF0YV90eXBlIiwg
InRleHQiOiAiaHRtbDJwZGZfZGF0YV90eXBlIiwgInByZWZpeCI6IG51bGwsICJ0eXBlX2lkIjog
MTEsICJ0b29sdGlwIjogInRoZSB0eXBlIG9mIGRhdGEgcGFzc2VkLCB1c3VhbGx5IHRoZSBhcnRp
ZmFjdCB0eXBlLiBVUkwgb3IgVVJJIGFyZSBuZWVkZWQgZm9yIHdlYnBhZ2Ugc2NhcGluZyIsICJw
bGFjZWhvbGRlciI6ICIiLCAiaW5wdXRfdHlwZSI6ICJ0ZXh0IiwgInJlcXVpcmVkIjogImFsd2F5
cyIsICJoaWRlX25vdGlmaWNhdGlvbiI6IGZhbHNlLCAiY2hvc2VuIjogZmFsc2UsICJkZWZhdWx0
X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZSwgImJsYW5rX29wdGlvbiI6IGZhbHNlLCAiaW50ZXJu
YWwiOiBmYWxzZSwgInV1aWQiOiAiMjFhYzJhYzAtYWJjOS00ODVhLWE2NmUtNWFiNjgwNDE1YjQw
IiwgIm9wZXJhdGlvbnMiOiBbXSwgIm9wZXJhdGlvbl9wZXJtcyI6IHt9LCAidmFsdWVzIjogW10s
ICJyZWFkX29ubHkiOiBmYWxzZSwgImNoYW5nZWFibGUiOiB0cnVlLCAicmljaF90ZXh0IjogZmFs
c2UsICJleHBvcnRfa2V5IjogIl9fZnVuY3Rpb24vaHRtbDJwZGZfZGF0YV90eXBlIiwgInRlbXBs
YXRlcyI6IFtdLCAiZGVwcmVjYXRlZCI6IGZhbHNlfSwgeyJpZCI6IDE2MSwgIm5hbWUiOiAiaHRt
bDJwZGZfc3R5bGVzaGVldCIsICJ0ZXh0IjogImh0bWwycGRmX3N0eWxlc2hlZXQiLCAicHJlZml4
IjogbnVsbCwgInR5cGVfaWQiOiAxMSwgInRvb2x0aXAiOiAiY3NzIGZvcm1hdHRlZCBzdHlsZXNo
ZWV0IGluZm9ybWF0aW9uIHRvIHVzZSB3aGVuIHJlbmRlcmluZyBQREYgZG9jdW1lbnQiLCAicGxh
Y2Vob2xkZXIiOiAiQHBhZ2UgeyBzaXplOiBsYW5kc2NhcGU7IH0qIHsgZm9udC1mYW1pbHk6IEFy
aWFsOyBmb250LXNpemU6IHNtYWxsOyB9dGFibGUgeyBib3JkZXItY29sbGFwc2U6IGNvbGxhcHNl
OyB9dGFibGUsIHRoLCB0ZCB7IGJvcmRlcjogMXB4IHNvbGlkIGJsYWNrOyB9IiwgImlucHV0X3R5
cGUiOiAidGV4dCIsICJoaWRlX25vdGlmaWNhdGlvbiI6IGZhbHNlLCAiY2hvc2VuIjogZmFsc2Us
ICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZSwgImJsYW5rX29wdGlvbiI6IGZhbHNl
LCAiaW50ZXJuYWwiOiBmYWxzZSwgInV1aWQiOiAiM2IwMWQ2MWYtY2Q5My00N2Q3LWFiNGEtYjMy
YzJiOGUxYmZhIiwgIm9wZXJhdGlvbnMiOiBbXSwgIm9wZXJhdGlvbl9wZXJtcyI6IHt9LCAidmFs
dWVzIjogW10sICJyZWFkX29ubHkiOiBmYWxzZSwgImNoYW5nZWFibGUiOiB0cnVlLCAicmljaF90
ZXh0IjogZmFsc2UsICJleHBvcnRfa2V5IjogIl9fZnVuY3Rpb24vaHRtbDJwZGZfc3R5bGVzaGVl
dCIsICJ0ZW1wbGF0ZXMiOiBbXSwgImRlcHJlY2F0ZWQiOiBmYWxzZX1dLCAiaW5jaWRlbnRfdHlw
ZXMiOiBbeyJ1cGRhdGVfZGF0ZSI6IDE1NDUyNjc4OTIwMDMsICJjcmVhdGVfZGF0ZSI6IDE1NDUy
Njc4OTIwMDMsICJ1dWlkIjogImJmZWVjMmQ0LTM3NzAtMTFlOC1hZDM5LTRhMDAwNDA0NGFhMCIs
ICJkZXNjcmlwdGlvbiI6ICJDdXN0b21pemF0aW9uIFBhY2thZ2VzIChpbnRlcm5hbCkiLCAiZXhw
b3J0X2tleSI6ICJDdXN0b21pemF0aW9uIFBhY2thZ2VzIChpbnRlcm5hbCkiLCAibmFtZSI6ICJD
dXN0b21pemF0aW9uIFBhY2thZ2VzIChpbnRlcm5hbCkiLCAiZW5hYmxlZCI6IGZhbHNlLCAic3lz
dGVtIjogZmFsc2UsICJwYXJlbnRfaWQiOiBudWxsLCAiaGlkZGVuIjogZmFsc2UsICJpZCI6IDB9
XSwgInBoYXNlcyI6IFtdLCAiYXV0b21hdGljX3Rhc2tzIjogW10sICJvdmVycmlkZXMiOiBbXSwg
Im1lc3NhZ2VfZGVzdGluYXRpb25zIjogW3sibmFtZSI6ICJmbl9odG1sMnBkZiIsICJwcm9ncmFt
bWF0aWNfbmFtZSI6ICJmbl9odG1sMnBkZiIsICJkZXN0aW5hdGlvbl90eXBlIjogMCwgImV4cGVj
dF9hY2siOiB0cnVlLCAidXNlcnMiOiBbInRlc3RAZXhhbXBsZS5jb20iXSwgInV1aWQiOiAiOTA5
ODYzODgtODIzZi00ZTI0LWExMTAtYjJkY2ZmNjAyNzliIiwgImV4cG9ydF9rZXkiOiAiZm5faHRt
bDJwZGYifV0sICJhY3Rpb25zIjogW3siaWQiOiAzMywgIm5hbWUiOiAiRXhhbXBsZTogSFRNTDJQ
REYiLCAidHlwZSI6IDEsICJvYmplY3RfdHlwZSI6ICJhcnRpZmFjdCIsICJjb25kaXRpb25zIjog
W10sICJhdXRvbWF0aW9ucyI6IFtdLCAibWVzc2FnZV9kZXN0aW5hdGlvbnMiOiBbXSwgIndvcmtm
bG93cyI6IFsiZXhhbXBsZV9odG1sMnBkZiJdLCAidmlld19pdGVtcyI6IFtdLCAidGltZW91dF9z
ZWNvbmRzIjogODY0MDAsICJ1dWlkIjogImNkYjQ5YTM0LTA5MTItNGM0YS1iZWYzLTBiZjVjY2Uz
NGFlNiIsICJleHBvcnRfa2V5IjogIkV4YW1wbGU6IEhUTUwyUERGIiwgImxvZ2ljX3R5cGUiOiAi
YWxsIn1dLCAibGF5b3V0cyI6IFtdLCAibm90aWZpY2F0aW9ucyI6IG51bGwsICJ0aW1lZnJhbWVz
IjogbnVsbCwgImxvY2FsZSI6IG51bGwsICJpbmR1c3RyaWVzIjogbnVsbCwgInJlZ3VsYXRvcnMi
OiBudWxsLCAiZ2VvcyI6IG51bGwsICJ0YXNrX29yZGVyIjogW10sICJhY3Rpb25fb3JkZXIiOiBb
XSwgInR5cGVzIjogW10sICJzY3JpcHRzIjogW10sICJpbmNpZGVudF9hcnRpZmFjdF90eXBlcyI6
IFtdLCAid29ya2Zsb3dzIjogW3sid29ya2Zsb3dfaWQiOiAyMCwgIm5hbWUiOiAiRXhhbXBsZTog
SFRNTDJQREYiLCAicHJvZ3JhbW1hdGljX25hbWUiOiAiZXhhbXBsZV9odG1sMnBkZiIsICJvYmpl
Y3RfdHlwZSI6ICJhcnRpZmFjdCIsICJkZXNjcmlwdGlvbiI6ICJDb252ZXJ0IEhUTUwgY29kZWQg
c3RyaW5nIHRvIGJhc2U2NCBlbmNvZGVkIFBERiBmb3JtYXQiLCAiY3JlYXRvcl9pZCI6ICJ0ZXN0
QGV4YW1wbGUuY29tIiwgImxhc3RfbW9kaWZpZWRfYnkiOiAiYUBiLmNvbSIsICJsYXN0X21vZGlm
aWVkX3RpbWUiOiAxNTQ1MjI5NTk5MDE3LCAiZXhwb3J0X2tleSI6ICJleGFtcGxlX2h0bWwycGRm
IiwgInV1aWQiOiAiYjMxZTkwZjgtNTgzYy00NWMwLWE3YzAtMTVkOTRiOTY5YjM3IiwgImNvbnRl
bnQiOiB7IndvcmtmbG93X2lkIjogImV4YW1wbGVfaHRtbDJwZGYiLCAieG1sIjogIjw/eG1sIHZl
cnNpb249XCIxLjBcIiBlbmNvZGluZz1cIlVURi04XCI/PjxkZWZpbml0aW9ucyB4bWxucz1cImh0
dHA6Ly93d3cub21nLm9yZy9zcGVjL0JQTU4vMjAxMDA1MjQvTU9ERUxcIiB4bWxuczpicG1uZGk9
XCJodHRwOi8vd3d3Lm9tZy5vcmcvc3BlYy9CUE1OLzIwMTAwNTI0L0RJXCIgeG1sbnM6b21nZGM9
XCJodHRwOi8vd3d3Lm9tZy5vcmcvc3BlYy9ERC8yMDEwMDUyNC9EQ1wiIHhtbG5zOm9tZ2RpPVwi
aHR0cDovL3d3dy5vbWcub3JnL3NwZWMvREQvMjAxMDA1MjQvRElcIiB4bWxuczpyZXNpbGllbnQ9
XCJodHRwOi8vcmVzaWxpZW50LmlibS5jb20vYnBtblwiIHhtbG5zOnhzZD1cImh0dHA6Ly93d3cu
dzMub3JnLzIwMDEvWE1MU2NoZW1hXCIgeG1sbnM6eHNpPVwiaHR0cDovL3d3dy53My5vcmcvMjAw
MS9YTUxTY2hlbWEtaW5zdGFuY2VcIiB0YXJnZXROYW1lc3BhY2U9XCJodHRwOi8vd3d3LmNhbXVu
ZGEub3JnL3Rlc3RcIj48cHJvY2VzcyBpZD1cImV4YW1wbGVfaHRtbDJwZGZcIiBpc0V4ZWN1dGFi
bGU9XCJ0cnVlXCIgbmFtZT1cIkV4YW1wbGU6IEhUTUwyUERGXCI+PGRvY3VtZW50YXRpb24+Q29u
dmVydCBIVE1MIGNvZGVkIHN0cmluZyB0byBiYXNlNjQgZW5jb2RlZCBQREYgZm9ybWF0PC9kb2N1
bWVudGF0aW9uPjxzdGFydEV2ZW50IGlkPVwiU3RhcnRFdmVudF8xNTVhc3htXCI+PG91dGdvaW5n
PlNlcXVlbmNlRmxvd18wc3d6Nm9iPC9vdXRnb2luZz48L3N0YXJ0RXZlbnQ+PHNlcnZpY2VUYXNr
IGlkPVwiU2VydmljZVRhc2tfMDhucHVuZFwiIG5hbWU9XCJIVE1MIHRvIFBERlwiIHJlc2lsaWVu
dDp0eXBlPVwiZnVuY3Rpb25cIj48ZXh0ZW5zaW9uRWxlbWVudHM+PHJlc2lsaWVudDpmdW5jdGlv
biB1dWlkPVwiY2FiZmFhMWItMWU5Ny00Zjk2LWIwMzQtNzUzYWQ2ZGE1MTJjXCI+e1wiaW5wdXRz
XCI6e1wiOWQwZTI4ODctOTFiYy00NWVjLTgzMWYtYjUxOTk2ZTAxZmE2XCI6e1wiaW5wdXRfdHlw
ZVwiOlwic3RhdGljXCIsXCJzdGF0aWNfaW5wdXRcIjp7XCJtdWx0aXNlbGVjdF92YWx1ZVwiOltd
LFwidGV4dF92YWx1ZVwiOlwiJmx0O3RhYmxlJmd0OyZsdDt0ciZndDsmbHQ7dGQmZ3Q7YSZsdDsv
dGQmZ3Q7Jmx0O3RkJmd0O2ImbHQ7L3RkJmd0OyZsdDsvdHImZ3Q7Jmx0O3RyJmd0OyZsdDt0ZCZn
dDtjJmx0Oy90ZCZndDsmbHQ7dGQmZ3Q7ZCZsdDsvdGQmZ3Q7Jmx0Oy90ciZndDsmbHQ7L3RhYmxl
Jmd0O1wifX0sXCIzYjAxZDYxZi1jZDkzLTQ3ZDctYWI0YS1iMzJjMmI4ZTFiZmFcIjp7XCJpbnB1
dF90eXBlXCI6XCJzdGF0aWNcIixcInN0YXRpY19pbnB1dFwiOntcIm11bHRpc2VsZWN0X3ZhbHVl
XCI6W10sXCJ0ZXh0X3ZhbHVlXCI6XCJAcGFnZSB7IHNpemU6IGxhbmRzY2FwZTsgfSogeyBmb250
LWZhbWlseTogQXJpYWw7IGZvbnQtc2l6ZTogc21hbGw7IH10YWJsZSB7IGJvcmRlci1jb2xsYXBz
ZTogY29sbGFwc2U7IH10YWJsZSwgdGgsIHRkIHsgYm9yZGVyOiAxcHggc29saWQgYmxhY2s7IH1c
In19LFwiMjFhYzJhYzAtYWJjOS00ODVhLWE2NmUtNWFiNjgwNDE1YjQwXCI6e1wiaW5wdXRfdHlw
ZVwiOlwic3RhdGljXCIsXCJzdGF0aWNfaW5wdXRcIjp7XCJtdWx0aXNlbGVjdF92YWx1ZVwiOltd
LFwidGV4dF92YWx1ZVwiOlwic3RyaW5nXCJ9fX0sXCJwb3N0X3Byb2Nlc3Npbmdfc2NyaXB0XCI6
XCIjIHJlc3VsdHMgaW4gYmFzZTY0LiBzZWUgb3V0cHV0IHByb3BlcnR5ICdjb250ZW50JzpcXG4j
IHJlc3VsdHMuY29udGVudFxcbiMgb3IgdXNlIHdvcmtmbG93IHByb3BlcnRpZXMsIHN1Y2ggYXMg
J3BkZicsIHdoZW4gdXNpbmcgdGhpcyBmdW5jdGlvbiB3aXRoIGFub3RoZXIgZnVuY3Rpb24gc3Vj
aCBhcyB1dGlsaXRpZXM6IGJhc2U2NCB0byBhdHRhY2htZW50OlxcbiMgaW5wdXRzLmJhc2U2NGNv
bnRlbnQgPSB3b3JrZmxvdy5wcm9wZXJ0aWVzLnBkZi5jb250ZW50XCIsXCJyZXN1bHRfbmFtZVwi
OlwicGRmXCJ9PC9yZXNpbGllbnQ6ZnVuY3Rpb24+PC9leHRlbnNpb25FbGVtZW50cz48aW5jb21p
bmc+U2VxdWVuY2VGbG93XzBzd3o2b2I8L2luY29taW5nPjxvdXRnb2luZz5TZXF1ZW5jZUZsb3df
MHZwcjc5eDwvb3V0Z29pbmc+PC9zZXJ2aWNlVGFzaz48c2VxdWVuY2VGbG93IGlkPVwiU2VxdWVu
Y2VGbG93XzBzd3o2b2JcIiBzb3VyY2VSZWY9XCJTdGFydEV2ZW50XzE1NWFzeG1cIiB0YXJnZXRS
ZWY9XCJTZXJ2aWNlVGFza18wOG5wdW5kXCIvPjxlbmRFdmVudCBpZD1cIkVuZEV2ZW50XzA5M3dz
eHdcIj48aW5jb21pbmc+U2VxdWVuY2VGbG93XzB2cHI3OXg8L2luY29taW5nPjwvZW5kRXZlbnQ+
PHNlcXVlbmNlRmxvdyBpZD1cIlNlcXVlbmNlRmxvd18wdnByNzl4XCIgc291cmNlUmVmPVwiU2Vy
dmljZVRhc2tfMDhucHVuZFwiIHRhcmdldFJlZj1cIkVuZEV2ZW50XzA5M3dzeHdcIi8+PHRleHRB
bm5vdGF0aW9uIGlkPVwiVGV4dEFubm90YXRpb25fMWt4eGl5dFwiPjx0ZXh0PlN0YXJ0IHlvdXIg
d29ya2Zsb3cgaGVyZTwvdGV4dD48L3RleHRBbm5vdGF0aW9uPjxhc3NvY2lhdGlvbiBpZD1cIkFz
c29jaWF0aW9uXzFzZXVqNDhcIiBzb3VyY2VSZWY9XCJTdGFydEV2ZW50XzE1NWFzeG1cIiB0YXJn
ZXRSZWY9XCJUZXh0QW5ub3RhdGlvbl8xa3h4aXl0XCIvPjx0ZXh0QW5ub3RhdGlvbiBpZD1cIlRl
eHRBbm5vdGF0aW9uXzFvZG14MnhcIj48dGV4dD5SZXN1bHRzIGluIGJhc2U2NDwvdGV4dD48L3Rl
eHRBbm5vdGF0aW9uPjxhc3NvY2lhdGlvbiBpZD1cIkFzc29jaWF0aW9uXzFnM2g4bThcIiBzb3Vy
Y2VSZWY9XCJTZXJ2aWNlVGFza18wOG5wdW5kXCIgdGFyZ2V0UmVmPVwiVGV4dEFubm90YXRpb25f
MW9kbXgyeFwiLz48L3Byb2Nlc3M+PGJwbW5kaTpCUE1ORGlhZ3JhbSBpZD1cIkJQTU5EaWFncmFt
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
ZSBicG1uRWxlbWVudD1cIlNlcnZpY2VUYXNrXzA4bnB1bmRcIiBpZD1cIlNlcnZpY2VUYXNrXzA4
bnB1bmRfZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjgwXCIgd2lkdGg9XCIxMDBcIiB4PVwi
MjU4XCIgeT1cIjE2NlwiLz48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1ORWRnZSBicG1u
RWxlbWVudD1cIlNlcXVlbmNlRmxvd18wc3d6Nm9iXCIgaWQ9XCJTZXF1ZW5jZUZsb3dfMHN3ejZv
Yl9kaVwiPjxvbWdkaTp3YXlwb2ludCB4PVwiMTk4XCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwi
IHk9XCIyMDZcIi8+PG9tZ2RpOndheXBvaW50IHg9XCIyNThcIiB4c2k6dHlwZT1cIm9tZ2RjOlBv
aW50XCIgeT1cIjIwNlwiLz48YnBtbmRpOkJQTU5MYWJlbD48b21nZGM6Qm91bmRzIGhlaWdodD1c
IjEzXCIgd2lkdGg9XCIwXCIgeD1cIjIyOFwiIHk9XCIxODRcIi8+PC9icG1uZGk6QlBNTkxhYmVs
PjwvYnBtbmRpOkJQTU5FZGdlPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVtZW50PVwiRW5kRXZl
bnRfMDkzd3N4d1wiIGlkPVwiRW5kRXZlbnRfMDkzd3N4d19kaVwiPjxvbWdkYzpCb3VuZHMgaGVp
Z2h0PVwiMzZcIiB3aWR0aD1cIjM2XCIgeD1cIjQ0N1wiIHk9XCIxODhcIi8+PGJwbW5kaTpCUE1O
TGFiZWw+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIxM1wiIHdpZHRoPVwiMFwiIHg9XCI0NjVcIiB5
PVwiMjI3XCIvPjwvYnBtbmRpOkJQTU5MYWJlbD48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpC
UE1ORWRnZSBicG1uRWxlbWVudD1cIlNlcXVlbmNlRmxvd18wdnByNzl4XCIgaWQ9XCJTZXF1ZW5j
ZUZsb3dfMHZwcjc5eF9kaVwiPjxvbWdkaTp3YXlwb2ludCB4PVwiMzU4XCIgeHNpOnR5cGU9XCJv
bWdkYzpQb2ludFwiIHk9XCIyMDZcIi8+PG9tZ2RpOndheXBvaW50IHg9XCI0NDdcIiB4c2k6dHlw
ZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIwNlwiLz48YnBtbmRpOkJQTU5MYWJlbD48b21nZGM6Qm91
bmRzIGhlaWdodD1cIjEzXCIgd2lkdGg9XCIwXCIgeD1cIjQwMi41XCIgeT1cIjE4NFwiLz48L2Jw
bW5kaTpCUE1OTGFiZWw+PC9icG1uZGk6QlBNTkVkZ2U+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVs
ZW1lbnQ9XCJUZXh0QW5ub3RhdGlvbl8xb2RteDJ4XCIgaWQ9XCJUZXh0QW5ub3RhdGlvbl8xb2Rt
eDJ4X2RpXCI+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIzMVwiIHdpZHRoPVwiMTMzXCIgeD1cIjM3
NVwiIHk9XCI4M1wiLz48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1ORWRnZSBicG1uRWxl
bWVudD1cIkFzc29jaWF0aW9uXzFnM2g4bThcIiBpZD1cIkFzc29jaWF0aW9uXzFnM2g4bThfZGlc
Ij48b21nZGk6d2F5cG9pbnQgeD1cIjM1MlwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwi
MTcwXCIvPjxvbWdkaTp3YXlwb2ludCB4PVwiNDIzXCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwi
IHk9XCIxMTRcIi8+PC9icG1uZGk6QlBNTkVkZ2U+PC9icG1uZGk6QlBNTlBsYW5lPjwvYnBtbmRp
OkJQTU5EaWFncmFtPjwvZGVmaW5pdGlvbnM+IiwgInZlcnNpb24iOiA4fSwgImFjdGlvbnMiOiBb
XX1dLCAicm9sZXMiOiBbXSwgIndvcmtzcGFjZXMiOiBbXSwgImZ1bmN0aW9ucyI6IFt7ImlkIjog
MjMsICJuYW1lIjogImZuX2h0bWwycGRmIiwgImRpc3BsYXlfbmFtZSI6ICJIVE1MIHRvIFBERiIs
ICJkZXNjcmlwdGlvbiI6IHsiZm9ybWF0IjogInRleHQiLCAiY29udGVudCI6ICJDb252ZXJ0IGh0
bWwgdGV4dCBvciBhIHVybCByZWZlcmVuY2UgdG8gYSBiYXNlNjQgZW5jb2RlZCBwZGYgZG9jdW1l
bnQuIn0sICJkZXN0aW5hdGlvbl9oYW5kbGUiOiAiZm5faHRtbDJwZGYiLCAiZXhwb3J0X2tleSI6
ICJmbl9odG1sMnBkZiIsICJ1dWlkIjogImNhYmZhYTFiLTFlOTctNGY5Ni1iMDM0LTc1M2FkNmRh
NTEyYyIsICJ2ZXJzaW9uIjogMywgImNyZWF0b3IiOiB7ImlkIjogMSwgInR5cGUiOiAidXNlciIs
ICJuYW1lIjogImFAYi5jb20iLCAiZGlzcGxheV9uYW1lIjogIlJlc2lsaWVudCBTeXNhZG1pbiJ9
LCAibGFzdF9tb2RpZmllZF9ieSI6IHsiaWQiOiAxLCAidHlwZSI6ICJ1c2VyIiwgIm5hbWUiOiAi
YUBiLmNvbSIsICJkaXNwbGF5X25hbWUiOiAiUmVzaWxpZW50IFN5c2FkbWluIn0sICJsYXN0X21v
ZGlmaWVkX3RpbWUiOiAxNTQ1MjI3OTU3NjY4LCAidmlld19pdGVtcyI6IFt7InN0ZXBfbGFiZWwi
OiBudWxsLCAic2hvd19pZiI6IG51bGwsICJlbGVtZW50IjogImZpZWxkX3V1aWQiLCAiZmllbGRf
dHlwZSI6ICJfX2Z1bmN0aW9uIiwgImNvbnRlbnQiOiAiOWQwZTI4ODctOTFiYy00NWVjLTgzMWYt
YjUxOTk2ZTAxZmE2IiwgInNob3dfbGlua19oZWFkZXIiOiBmYWxzZX0sIHsic3RlcF9sYWJlbCI6
IG51bGwsICJzaG93X2lmIjogbnVsbCwgImVsZW1lbnQiOiAiZmllbGRfdXVpZCIsICJmaWVsZF90
eXBlIjogIl9fZnVuY3Rpb24iLCAiY29udGVudCI6ICIzYjAxZDYxZi1jZDkzLTQ3ZDctYWI0YS1i
MzJjMmI4ZTFiZmEiLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNlfSwgeyJzdGVwX2xhYmVsIjog
bnVsbCwgInNob3dfaWYiOiBudWxsLCAiZWxlbWVudCI6ICJmaWVsZF91dWlkIiwgImZpZWxkX3R5
cGUiOiAiX19mdW5jdGlvbiIsICJjb250ZW50IjogIjIxYWMyYWMwLWFiYzktNDg1YS1hNjZlLTVh
YjY4MDQxNWI0MCIsICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2V9XSwgIndvcmtmbG93cyI6IFt7
IndvcmtmbG93X2lkIjogMjAsICJuYW1lIjogIkV4YW1wbGU6IEhUTUwyUERGIiwgInByb2dyYW1t
YXRpY19uYW1lIjogImV4YW1wbGVfaHRtbDJwZGYiLCAib2JqZWN0X3R5cGUiOiAiYXJ0aWZhY3Qi
LCAiZGVzY3JpcHRpb24iOiBudWxsLCAidXVpZCI6IG51bGwsICJhY3Rpb25zIjogW119LCB7Indv
cmtmbG93X2lkIjogMjEsICJuYW1lIjogInRlc3QgaCB0IG0gbCIsICJwcm9ncmFtbWF0aWNfbmFt
ZSI6ICJ0ZXN0X2hfdF9tX2wiLCAib2JqZWN0X3R5cGUiOiAiaW5jaWRlbnQiLCAiZGVzY3JpcHRp
b24iOiBudWxsLCAidXVpZCI6IG51bGwsICJhY3Rpb25zIjogW119XX1dfQ==
"""
    )
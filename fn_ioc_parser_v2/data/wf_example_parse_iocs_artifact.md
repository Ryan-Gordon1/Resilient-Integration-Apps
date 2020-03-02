<!--
    DO NOT MANUALLY EDIT THIS FILE
    THIS FILE IS AUTOMATICALLY GENERATED WITH resilient-circuits codegen
-->

# Example: Parse IOCs (Artifact)


## Function - IOC Parser v2

### API Name
`func_ioc_parser_v2`

### Output Name
`None`

### Message Destination
`fn_ioc_parser_v2`

### Pre-Processing Script
```python
# Define Pre-Process Inputs
inputs.ioc_parser_v2_incident_id = incident.id
inputs.ioc_parser_v2_artifact_id = artifact.id
inputs.ioc_parser_v2_artifact_value = artifact.value
```

### Post-Processing Script
```python
import re

def get_artifact_type(artifact_value, artifact_type):
  """Use some regex expressions to try and identify
  from the Artifact's value, what Artifact type it is.
  Return original artifact_type if we cannot figure it out"""

  dns_name_regex = re.compile(r'^(([a-zA-Z]{1})|([a-zA-Z]{1}[a-zA-Z]{1})|([a-zA-Z]{1}[0-9]{1})|([0-9]{1}[a-zA-Z]{1})|([a-zA-Z0-9][a-zA-Z0-9-_]{1,61}[a-zA-Z0-9]))\.([a-zA-Z]{2,6}|[a-zA-Z0-9-]{2,30}\.[a-zA-Z]{2,3})$')
  
  if re.match(dns_name_regex, artifact_value):
    return "DNS Name"
  
  return artifact_type

# Map ioc.type to Resilient Artifact Type
ioc_type_to_artifact_type_map = {
    'uri': 'URI Path',
    'IP': 'IP Address',
    'md5': 'Malware MD5 Hash',
    'sha1': 'Malware SHA-1 Hash',
    'sha256': 'Malware SHA-256 Hash',
    'CVE': 'Threat CVE ID',
    'email': 'Email Sender',
    'filename': 'File Name',
    'file': 'File Name'
}

# Get the IOCs
iocs = results.iocs

if iocs:
    # Loop IOCs and add each on as an Artifact
    for ioc in iocs:
      
      # If attachment_file_name is not defined, use the ioc.value as in the Artifact's Description
      if results.attachment_file_name:
        artifact_description = u"This IOC occurred {0} time(s) in the artifact: {1}".format( unicode(ioc.count), unicode(results.attachment_file_name) )
      
      else:
        artifact_description = u"This IOC occurred {0} time(s) in the artifact: {1}".format( unicode(ioc.count), unicode(ioc.value) )

      artifact_value = ioc.value
      artifact_type = ioc_type_to_artifact_type_map.get(ioc.type, "String")
      
      # If the artifact_type is 'URI Path', call get_artifact_type to try intentify the type using regex
      if artifact_type == "URI Path":
        artifact_type = get_artifact_type(artifact_value, artifact_type)
      
      incident.addArtifact(artifact_type, artifact_value, artifact_description)

```

---

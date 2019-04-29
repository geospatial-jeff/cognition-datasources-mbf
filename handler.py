from datasources import Manifest

def MicrosoftBuildingFootprints(event, context):
    manifest = Manifest()
    manifest['MicrosoftBuildingFootprints'].search(**event)
    response = manifest.execute()
    return response



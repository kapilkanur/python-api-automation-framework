from endpoints import api_version

pet_endpoints = {
    "GET_UPDATE_OR_DELETE_PET_BY_ID": api_version.root + "/pet/{petId}",
    "UPLOAD_PET_IMAGE": api_version.root + "/pet/{petId}/uploadImage",
    "ADD_OR_UPDATE_PET": api_version.root + "/pet",
    "FIND_PETS_BY_STATUS": api_version.root + "/pet/findByStatus",
    "FIND_PETS_BY_TAGS": api_version.root + "/pet/findByTags",
}

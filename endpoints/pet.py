root = "/v2"
pet_endpoints = {
    "GET_UPDATE_OR_DELETE_PET_BY_ID": root + "/pet/{petId}",
    "UPLOAD_PET_IMAGE": root + "/pet/{petId}/uploadImage",
    "ADD_OR_UPDATE_PET": root + "/pet",
    "FIND_PETS_BY_STATUS": root + "/pet/findByStatus"
}

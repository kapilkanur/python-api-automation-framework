from endpoints import api_version

user_endpoints = {
    "CREATE_USER": api_version.root + "/user",
    "CREATE_USERS_IN_BULK": api_version.root + "/user/createWithList",
    "GET_UPDATE_DELETE_USER": api_version.root + "/user/{username}",
    "USER_LOGIN": api_version.root + "/user/login",
    "USER_LOGOUT": api_version.root + "/user/logout"
}